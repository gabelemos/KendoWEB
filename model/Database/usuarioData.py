import model.Database.connection as conexao

def criandoUsuario(empresa,nome,email,senha,telefone):
    conexaoBD = conexao.criandoConexao()
    cursorBD = conexaoBD.cursor()
    
    query = "INSERT INTO Usuario (Fk_empresa, nome, saldo, senha, telefone, nivel, status, email) values(%s,%s,0,%s,%s, 'cliente', 'pendente' ,%s)"
    parametros = [empresa, nome, senha, telefone, email]
    
    cursorBD.execute(query,parametros)
    
    conexaoBD.commit()
    cursorBD.close()
    conexaoBD.close()
    
def buscandoUsuario(email, senha):
    conexaoBD = conexao.criandoConexao()
    query = "SELECT * FROM usuario u left join empresas e on e.id = u.Fk_empresa WHERE email = %s and senha = %s;"
    parametros = (email, senha)
    
    cursorBD = conexaoBD.cursor()
    cursorBD.execute(query, parametros)
    listaResultado = cursorBD.fetchone()
    
    cursorBD.close()
    conexaoBD.close()
    return listaResultado

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

def apagarUsuario(nome):
    conexaoBD = conexao.criandoConexao()
    cursorBD = conexaoBD.cursor()
    
    query = "DELETE FROM Usuario WHERE nome = %s"
    parametros = [nome]
    
    cursorBD.execute(query, parametros)
    
    conexaoBD.commit()
    print(f"Usuário {nome} excluido com sucesso!")
    cursorBD.close()
    conexaoBD.close()
    
def Depositar(saldo, nome):
    conexaoBD = conexao.criandoConexao()
    cursorBD = conexaoBD.cursor()
    
    query = "UPDATE Usuario SET saldo = saldo + %s WHERE nome = %s"
    parametros = [saldo, nome]
    
    cursorBD.execute(query, parametros)
    
    conexaoBD.commit()
    print(f"Usuario {nome} depositou R${saldo}")
    cursorBD.close()
    conexaoBD.close()
    
def editandoUsuario(novo_nome,photo,nome):
    print(photo)
    conexaoBD = conexao.criandoConexao()
    cursorBD = conexaoBD.cursor()
    
    query = "UPDATE Usuario SET nome = %s, foto = %s WHERE nome = %s"

    parametros = [novo_nome, photo, nome]
    
    cursorBD.execute(query, parametros)
    conexaoBD.commit()
    cursorBD.close()
    conexaoBD.close()

    
def buscandoEmpreUsuario(email):
    conexaoBD = conexao.criandoConexao()
    query = "SELECT * FROM usuario u left join empresas e on e.id = u.Fk_empresa WHERE email = %s;"
    parametros = [email]
    
    cursorBD = conexaoBD.cursor()
    cursorBD.execute(query, parametros)
    listaResultado = cursorBD.fetchone()

    cursorBD.close()
    conexaoBD.close()
    return listaResultado

buscandoEmpreUsuario("lemos@gmail.com")