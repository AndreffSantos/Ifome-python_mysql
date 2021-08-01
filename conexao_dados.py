import mysql.connector

def criar_conexao(host='localhost', usuario='root', senha='senha', banco='db_sistema'):
    return mysql.connector.connect(host=host, user=usuario, password=senha, database=banco)

def fechar_conexao(cursor, conexao):
    cursor.close()
    conexao.close()