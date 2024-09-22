#IMPORTANDO AS BIBLIOTECAS NECESSÁRIAS
from flask import Flask, request, session, render_template, redirect, url_for, flash
import model.Database.usuarioData as usuarioData
import model.Database.empresaData as empresaData
import model.Database.produtosData as produtoData
import os
from werkzeug.utils import secure_filename

webapp = Flask(__name__)
webapp.secret_key = "k3nd0"
webapp.config["UPLOAD_FOLDER"] = "static/usr_img"
webapp.config["UPLOAD_FOLDER2"] = "static/qrPIX"

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#ROTAS
@webapp.route("/")
def HomeScreen():
        #usr_data = usuarioData.buscandoUsuario("lemos@gmail.com","1234")
        if 'logado' in session:
                vendas = empresaData.ListandoVendas()
                empresas = empresaData.verEmpresa()
                print(empresas)
                produtos = produtoData.listarTodosProdutos()
                userData = usuarioData.buscandoEmpreUsuario(session['email'])
                return render_template("index.html", userData = userData, fileName = f"usr_img/{userData[5]}", vendas=vendas, empresas=empresas, produtos=produtos)
        else:
                return redirect(url_for('LoginScreen_get'))#, usuario=usr_data)
        #else:
        
@webapp.get("/login")
def LoginScreen_get():
        empresa_dados = empresaData.verEmpresa()
        return render_template("loginscreen.html", nome_empresa = empresa_dados)

@webapp.post("/login")
def LoginScreen_post():
        usuario = usuarioData.buscandoUsuario(request.form["email"], request.form["senha"])
        empresa_dados = empresaData.verEmpresa()
        if (usuario != None and usuario[8] == "ativo"):
                if request.form["email"] == usuario[1] and request.form["senha"] == usuario[2]:
                        session['logado'] = True
                        session['status'] = usuario[8]
                        session['nivel'] = usuario[7]
                        session['saldo'] = usuario[4]
                        session['nome'] = usuario[3]
                        session['empre'] = usuario[11]
                        session['email'] = usuario[1]
                        session['id_empre'] = usuario[10]
                        Logado = True
                        return redirect(url_for('HomeScreen'))
                else:
                        return render_template("loginscreen.html", nome_empresa = empresa_dados, Erro=True)
        elif(usuario != None and usuario[8] == "pendente"):
                        return render_template("wait.html")
        else:
                return render_template("loginscreen.html", nome_empresa = empresa_dados, Erro=True)


#ROTA CRIADA PARA REGISTRAR USUÁRIO NA PLATAFORMA
@webapp.post("/registrar")
def Registrar_post():
        nome = request.form["NOME"]
        email = request.form["EMAIL"]
        empresa = request.form["EMPRE"]
        telefone = request.form["TEL"]
        senha = request.form["KEY"]
        Logado = True
        #PEGANDO OS DADOS DO REGISTER E CRIANDO O USUARIO
        empresa_dados = empresaData.verEmpresa()
        usuarioData.criandoUsuario(empresa,nome,email,senha,telefone)
        return render_template("loginscreen.html", Logado=True, nome_empresa = empresa_dados)
        

@webapp.get("/logout")
def Logout():
        session.pop("usuario", None)
        Logado = False
        return redirect(url_for("LoginScreen_get"))

@webapp.get("/funcionarios")
def FuncioScreen():
        lista_funcionarios = usuarioData.ListarUsers()
        return render_template("funcionarios.html", funcionarios = lista_funcionarios, usuario="adm") # ("empresas.html", usuario=VARIAVEL DO USUARIO)

@webapp.get("/produtos")
def ProductScreen():
        produtos_lista = produtoData.listarTodosProdutos()
        empresa_dados = empresaData.verEmpresa()
        return render_template("produtos.html", produtos_lista = produtos_lista, nome_empresa=empresa_dados)

@webapp.post("/produto/add")
def CadastrandoProduto():
        nome = request.form["nome_produto"]
        valor = request.form["valor_produtos"]
        
        produtoData.CriarProduto(nome,valor,0)
        return redirect(url_for("ProductScreen"))

@webapp.post("/produto/edit")
def EditandoProduto():
        novo_nome = request.form["nome_produto"]
        novo_valor = request.form["valor_produtos"]
        id_produto = request.form["id_produto"]
        id_empresa = request.form["empre_prod"]
        
        produtoData.EditandoProduto(novo_nome, novo_valor, id_produto)
        produtoData.AtribuirEmpresa(id_empresa,id_produto,novo_valor)
        return redirect(url_for("ProductScreen"))
        
@webapp.post("/removerProd")
def removerProduto():
        nome_prod = request.form["nome_prod"] 
        produtoData.ExcluirProduto(nome_prod)
        
        return redirect(url_for("ProductScreen"))
        
@webapp.get("/empresas")
def EmpScreen():
        empresa_dados = empresaData.verEmpresa()
        lista_funcionarios = usuarioData.ListarUsers()
        lista_produtos = produtoData.ListarProdutosEmpresa()
        
        #PEGANDO PRODUTOS DO BANCO DE DADOS
        string_empre = str(empresa_dados[3:-2])
        #SEPARANDO PRODUTOS EM LISTA E TIRANDO AS ASPAS, PARENTESIS
        empre_nome = string_empre.replace("(", "").replace(")", "").replace("'", "").replace('"', "").replace(",", "").split()
        
        return render_template("users.html", nome_empresa = empresa_dados, funcionarios = lista_funcionarios, empresaProdutos = lista_produtos)

#ROTA CRIADA PARA REGISTRAR EMPRESAS NA PLATAFORMA
@webapp.post("/empresa")
def criandoEmpresa():
        nome = request.form["nome_empresa"]
        categoria = request.form["categoria"]
        produtos = request.form["nome_produtos"]
        funcionarios = request.form["nome_funcio"]
        caixa = request.form["valor_caixa"]
        
        empresaData.CriandoEmpresa(nome,categoria,produtos,funcionarios,caixa)
        return redirect(url_for("EmpScreen"))

@webapp.post("/deleteUser")
def deleteUser():
        nome_user = request.form["nome_user"]
        usuarioData.apagarUsuario(nome_user)
        
        return redirect(url_for("FuncioScreen"))
        

#def verificandoLogin(niveisNecessarios):
#        if (('logado' in session) and (session['logado'] == True) and ("nivel" in session)):
#                for nivelNecessario in niveisNecessarios:
#                        if(session["nivel"] == nivelNecessario):
#                                return True
#                return False
#        else:
#                return False

@webapp.get("/financeiro")
def Pagamentos():
        userData = usuarioData.buscandoEmpreUsuario(session['email'])
        empresaDados = empresaData.listarEMPRESANOME(session['empre'])
        lista_produtos = produtoData.ListarProdutosEmpresa()
        vendas = empresaData.ListandoVendas()
        
        todos_produtos = produtoData.listarTodosProdutos()
        print(todos_produtos)
        return render_template("payscreen.html", userData = userData, fileName = f"qrPIX/{empresaDados[6]}", empresaProdutos = lista_produtos, produtos = todos_produtos, vendas=vendas)

@webapp.post("/financeiro/venda")
def Depositar():
        #nome = request.form["nome_deposito"]
        item = request.form['PROD']
        quantidade = request.form['quantidade_venda']
        empresa = session['id_empre']
        unidProdutoData = produtoData.ListarProdutosPeloId(item)
        valor_unid = unidProdutoData[3]
        valor_total = float(unidProdutoData[3]) * float(quantidade)
        
        empresaData.registrandoVenda(empresa,item,quantidade,valor_unid,valor_total)
        #empresaData.ListandoVendas()
        return redirect(url_for("Pagamentos"))

@webapp.post("/financeiro/qrCODE")
def enviandoQR():
        nome_empresa = session['empre']
        
        if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
                flash('No image selected for uploading')
                return redirect(request.url)
        if os.listdir(webapp.config['UPLOAD_FOLDER2']):
                return redirect(url_for("Pagamentos"))
        if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                caminhoCorreto = os.path.join(webapp.config['UPLOAD_FOLDER2'], filename)                
                file.save(caminhoCorreto)
                empresaData.atualizandoFoto(nome_empresa,filename)
                #print('upload_image filename: '+ filename)
                flash('Image successfully uploaded and displayed below')
                return redirect(url_for("Pagamentos"))
        else:
                flash('Allowed image types are - png, jpg, jpeg, gif')
        
@webapp.post("/perfil")
def editandoUsuario():
        novo_nome = request.form["novo_nome"]
        nome = session['nome']
        
        if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
                flash('No image selected for uploading')
                return redirect(request.url)
        if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                caminhoCorreto = os.path.join(webapp.config['UPLOAD_FOLDER'], filename)
                file.save(caminhoCorreto)
                
                usuarioData.editandoUsuario(novo_nome,filename,nome)
                session['nome'] = novo_nome
                print(usuarioData.buscandoEmpreUsuario(session['email']))
                #print('upload_image filename: ' + filename)
                flash('Image successfully uploaded and displayed below')
                return redirect(url_for("HomeScreen"))
        else:
                flash('Allowed image types are - png, jpg, jpeg, gif')

        #usuarioData.editandoUsuario(novo_nome, nova_foto, nome)
        
@webapp.get("/analises")
def Analises():
        empresa_dados = empresaData.verEmpresa()
        return render_template("analise.html",nome_empresa = empresa_dados)

webapp.run(debug=True)