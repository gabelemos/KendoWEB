import model.Database.connection as conexao

def CriarProduto(nome, valor, vendas):
    conexaoBD = conexao.criandoConexao()
    cursorBD = conexaoBD.cursor()
    
    query = "INSERT INTO Produtos (nome,valor_unid,vendidos) values (%s,%s,%s)"
    parametros = [nome,valor,vendas]
    
    cursorBD.execute(query,parametros)
    
    conexaoBD.commit()
    cursorBD.close()
    conexaoBD.close()
    
def ListarProdutos(company_id):
    conexaoBD = conexao.criandoConexao()
    cursorBD = conexaoBD.cursor()
    
    query = "SELECT p.name FROM products p JOIN companies c ON p.company_id = c.id WHERE c.id = %s"
    
    products = [row[0] for row in cursorBD.fetchall()]
    
    cursorBD.execute(query, (company_id,))
    
    conexaoBD.commit()
    cursorBD.close()
    conexaoBD.close()
    
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
    return produtos
    
def ExcluirProduto(nome):
    conexaoBD = conexao.criandoConexao()
    cursorBD = conexaoBD.cursor()
    
    query = "DELETE FROM produtos WHERE nome = %s"
    parametros = [nome]
    
    cursorBD.execute(query, parametros)
    
    conexaoBD.commit()
    print(f"Produto {nome} excluido com sucesso!")
    cursorBD.close()
    conexaoBD.close()
    

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

def ListarProdutosPeloId(id):
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

def EditandoProduto(novo_nome, novo_valor,id_produto):
    conexaoBD = conexao.criandoConexao()
    cursorBD = conexaoBD.cursor()
    
    query = "UPDATE produtos SET nome = %s, valor_unid = %s WHERE id = %s"
    parametros = [novo_nome,novo_valor,id_produto]
    
    cursorBD.execute(query, parametros)
    print(f"{novo_nome} editado com sucesso! {id_produto}")
    conexaoBD.commit()
    cursorBD.close()
    conexaoBD.close()
    
def AtribuirEmpresa(id_empresa,id_produto,valor_venda):
    conexaoBD = conexao.criandoConexao()
    cursorBD = conexaoBD.cursor()
    
    query = "INSERT INTO empresas_produtos (Fk_empresa,Fk_produto,valor_venda,valor_compra) values (%s,%s,%s,0)"
    parametros = [id_empresa,id_produto,valor_venda]
    
    cursorBD.execute(query,parametros)
    
    conexaoBD.commit()
    cursorBD.close()
    conexaoBD.close()