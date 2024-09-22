import model.Database.connection as conexao

def buscandoUsuario(email, senha):
    conexaoBD = conexao.criandoConexao()
    query = "SELECT * FROM usuario u left join empresas e on e.id = u.Fk_empresa WHERE email = %s and senha = %s;"
    parametros = (email, senha)
    
    cursorBD = conexaoBD.cursor()
    cursorBD.execute(query, parametros)
    listaResultado = cursorBD.fetchone()
    
    cursorBD.close()
    conexaoBD.close()
    print(listaResultado) 

buscandoUsuario("lemos@gmail.com","1234")

def verEmpresa(nome):
    conexaoBD = conexao.criandoConexao()
    cursorBD = conexaoBD.cursor()
    
    query = "select * from empresas where nome = (%s)"
    parametros = [nome]
    
    cursorBD.execute(query, parametros)
    
    nome_empre = cursorBD.fetchone()
    
    #PEGANDO PRODUTOS DO BANCO DE DADOS
    string_empre = str(nome_empre[3:-2])
    #SEPARANDO PRODUTOS EM LISTA E TIRANDO AS ASPAS, PARENTESIS
    empre_nome = string_empre.replace("(", "").replace(")", "").replace("'", "").replace('"', "").replace(",", "").split()
    cursorBD.close()
    conexaoBD.close()
    print(empre_nome[0])
    
#verEmpresa("Salgadinhos")

def apagarUsuario(nome):
    conexaoBD = conexao.criandoConexao()
    cursorBD = conexaoBD.cursor()
    
    query = "DELETE FROM `usuario` WHERE (`nome` = %s)"
    parametros = (nome)
    
    cursorBD.execute(query, parametros)
    
    conexaoBD.commit()
    print(f"Usuário {nome} excluido com sucesso!")
    cursorBD.close()
    conexaoBD.close()
    
#apagarUsuario("matheus")

def ListarUsers():
    conexaoBD = conexao.criandoConexao()
    cursorBD = conexaoBD.cursor()
    
    query = """
            select * from usuario u
            
            left join empresas e
            on e.id = u.Fk_empresa
            """
    #parametros = [nome]
    
    cursorBD.execute(query)
    
    usuarios = cursorBD.fetchall() 
    cursorBD.close()
    conexaoBD.close()
    return usuarios

#ListarUsers()
    
#apagarUsuario("Carlinhoss")

def listarTodosProdutos():
    conexaoBD = conexao.criandoConexao()
    cursorBD = conexaoBD.cursor()
    
    query = """
            select * from produtos
            """
    
    cursorBD.execute(query)
    
    produtos = cursorBD.fetchall() 
    cursorBD.close()
    conexaoBD.close()
    print(len(produtos))
    
#listarTodosProdutos()

def ListarProdutos(company_id):
    conexaoBD = conexao.criandoConexao()
    cursorBD = conexaoBD.cursor()
    
    query = "SELECT p.name FROM products p JOIN companies c ON p.company_id = c.id WHERE c.id = %s"
    
    products = [row[0] for row in cursorBD.fetchall()]
    
    cursorBD.execute(query, (company_id,))
    
    conexaoBD.commit()
    cursorBD.close()
    conexaoBD.close()

#ListarProdutos(01)

def buscandoEmpreUsuario(email):
    conexaoBD = conexao.criandoConexao()
    query = "SELECT * FROM usuario u left join empresas e on e.id = u.Fk_empresa WHERE email = %s;"
    parametros = [email]
    
    cursorBD = conexaoBD.cursor()
    cursorBD.execute(query, parametros)
    listaResultado = cursorBD.fetchone()
    print(listaResultado)
    cursorBD.close()
    conexaoBD.close()
    return listaResultado

#buscandoEmpreUsuario("lemos@gmail.com")

def listarProdutosEmpresa(nome):
    conexaoBD = conexao.criandoConexao()
    cursorBD = conexaoBD.cursor()
    
    query = "select * from empresas where nome = (%s)"
    parametros = [nome]
    
    cursorBD.execute(query, parametros)
    
    nome_empre = cursorBD.fetchone()

    cursorBD.close()
    conexaoBD.close()
    print(nome_empre)
    
#listarProdutosEmpresa("Salgadinhos")

def ListarProdutosEmpresa():
    conexaoBD = conexao.criandoConexao()
    cursorBD = conexaoBD.cursor()
    #where emp.id = %s
    query = """
            select *
            from empresas emp

            left join empresas_produtos ep
            on ep.Fk_empresa = emp.id

            left join produtos prod
            on prod.id = ep.Fk_produto
            
            """
            
    cursorBD.execute(query)
    
    produtos_empresa = cursorBD.fetchall() 
    print(f"Produtos listados com sucesso! {produtos_empresa}")
    cursorBD.close()
    conexaoBD.close()
    return produtos_empresa

#ListarProdutosEmpresa()

def ListarUsers():
    conexaoBD = conexao.criandoConexao()
    cursorBD = conexaoBD.cursor()
    
    query = """
            select * from usuario u
            
            left join empresas e
            on e.id = u.Fk_empresa
            """
    #parametros = [nome]
    
    cursorBD.execute(query)
    
    usuarios = cursorBD.fetchall() 
    cursorBD.close()
    conexaoBD.close()
    return usuarios

#ListarUsers()

def ListarProdutosEmpresa():
    conexaoBD = conexao.criandoConexao()
    cursorBD = conexaoBD.cursor()
    #where emp.id = %s
    query = """
            select *
            from empresas emp

            left join empresas_produtos ep
            on ep.Fk_empresa = emp.id

            left join produtos prod
            on prod.id = ep.Fk_produto
            
            """
            
    cursorBD.execute(query)
    
    produtos_empresa = cursorBD.fetchall() 
    print(f"Produtos listados com sucesso! {produtos_empresa}")
    cursorBD.close()
    conexaoBD.close()
    return produtos_empresa

#ListarProdutosEmpresa() 

def ListarProdutosPeloNome(id):
    conexaoBD = conexao.criandoConexao()
    cursorBD = conexaoBD.cursor()
    
    query = "SELECT * FROM produtos WHERE id = %s"
    parametros = [id]
    
    cursorBD.execute(query, parametros)
    
    products = cursorBD.fetchone()
    conexaoBD.commit()
    cursorBD.close()
    conexaoBD.close()
    print(products)
    return products

#ListarProdutosPeloNome(1)

def ListandoVendas():
    conexaoBD = conexao.criandoConexao()
    cursorBD = conexaoBD.cursor()
    
    query = "select * from empresa_extrato"
    #parametros = [nome]
    
    cursorBD.execute(query)
    
    vendas = cursorBD.fetchall()
    cursorBD.close()
    conexaoBD.close()
    print(vendas)
    return vendas

ListandoVendas()