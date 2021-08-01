from conexao_dados import criar_conexao, fechar_conexao

def inserir_dados(values_nome, values_senha):
    inserir = f'insert into usuarios (nome, senha) values ("{values_nome}", "{values_senha}");'
    con = criar_conexao()
    cursor = con.cursor()
    cursor.execute(inserir)
    con.commit()
    fechar_conexao(cursor, con)

def recupera_senha_usuario(values_nome):
    requisicao = f'select * from usuarios where nome="{values_nome}";'
    con = criar_conexao()
    cursor = con.cursor()
    cursor.execute(requisicao)
    resposta = cursor.fetchall()
    fechar_conexao(cursor, con)
    return resposta[0][1]