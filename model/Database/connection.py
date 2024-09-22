import mysql.connector

def criandoConexao():
    conexaoBD = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="kendo_bd"
    )
    
    return conexaoBD