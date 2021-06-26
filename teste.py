import psycopg2

def conectar():
    conexao = psycopg2.connect(user='root', password='root', host='127.0.0.1', database='password_manager')
    return conexao

senha = input("senha: ")
email_usuario = input("email: ")
usuario = input("usuario")
url = input("url")
nome_app = input("nome")

def guardar_senhas(senha, email_usuario, usuario, url, nome_app):
    conexao = conectar()
    cursor = conexao.cursor()
    postgres_insert_query = """ INSERT INTO contas (senha, email, usuario, url, nome_app) VALUES (%s, %s, %s, %s, %s)"""
    record_into_insert = (senha, email_usuario, usuario, url, nome_app)
    cursor.execute(postgres_insert_query, record_into_insert)
    conexao.commit()

guardar_senhas(senha, email_usuario, usuario, url, nome_app)

