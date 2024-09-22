import model.Database.connection as conexao

#Função para criar a empresa
def CriandoEmpresa(nome, categoria, produtos, funcionarios, caixa):
    conexaoBD = conexao.criandoConexao()
    cursorBD = conexaoBD.cursor()
    
    query = "INSERT INTO Empresas (nome, categoria, produtos, funcionarios, caixa) values (%s,%s,%s,%s,%s)"
    parametros = [nome, categoria, produtos, funcionarios, caixa]
    
    cursorBD.execute(query, parametros)
    
    conexaoBD.commit()
    cursorBD.close()
    conexaoBD.close()
    
def verEmpresa():
    conexaoBD = conexao.criandoConexao()
    cursorBD = conexaoBD.cursor()
    
    query = "select * from empresas"
    #parametros = [nome]
    
    cursorBD.execute(query)
    
    empresa = cursorBD.fetchall()
    cursorBD.close()
    conexaoBD.close()
    return empresa

def listarProdutosEmpresa(nome):
    conexaoBD = conexao.criandoConexao()
    cursorBD = conexaoBD.cursor()
    
    query = "select * from empresas where nome = (%s)"
    parametros = [nome]
    
    cursorBD.execute(query, parametros)
    
    nome_empre = cursorBD.fetchone()
    
    #PEGANDO PRODUTOS DO BANCO DE DADOS
    string_empre = str(nome_empre[3:-2])
    #SEPARANDO PRODUTOS EM LISTA E TIRANDO AS ASPAS, PARENTESIS E VIRGULAS
    empre_nome = string_empre.replace("(", "").replace(")", "").replace("'", "").replace('"', "").replace(",", "").split()
    cursorBD.close()
    conexaoBD.close()
    print(empre_nome[1])
   
#listarProdutosEmpresa("Gago's Enterprise")
    
def atualizandoFoto(nome,photo):
    print(photo)
    conexaoBD = conexao.criandoConexao()
    cursorBD = conexaoBD.cursor()
    
    query = "UPDATE empresas SET QrPIX = %s WHERE nome = %s"

    parametros = [photo, nome]
    
    cursorBD.execute(query, parametros)
    conexaoBD.commit()
    cursorBD.close()
    conexaoBD.close()
    

def listarEMPRESANOME(nome):
    conexaoBD = conexao.criandoConexao()
    cursorBD = conexaoBD.cursor()
    
    query = "select * from empresas where nome = (%s)"
    parametros = [nome]
    
    cursorBD.execute(query, parametros)
    
    nome_empre = cursorBD.fetchone()

    cursorBD.close()
    conexaoBD.close()
    return nome_empre

def registrandoVenda(id_empresa,id_produto,quantidade,valor_unid,valor_total):
    conexaoBD = conexao.criandoConexao()
    cursorBD = conexaoBD.cursor()
    
    query = "INSERT INTO empresa_extrato (Fk_empresa, Fk_produto, quantidade_vendida, valor_unita, valor_total) values (%s,%s,%s,%s,%s)"
    parametros = [id_empresa,id_produto,quantidade,valor_unid,valor_total]

    
    cursorBD.execute(query, parametros)
    
    conexaoBD.commit()
    cursorBD.close()
    conexaoBD.close()
    
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
    
def ValorTotalVendido():
    conexaoBD = conexao.criandoConexao()
    cursorBD = conexaoBD.cursor()
    
    query = "select * from empresas where nome = (%s)"
    #parametros = [nome]
    
    #cursorBD.execute(query, parametros)
    
    nome_empre = cursorBD.fetchone()

    cursorBD.close()
    conexaoBD.close()
    return nome_empre