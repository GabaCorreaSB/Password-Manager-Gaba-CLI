import psycopg2

def guardar_senhas(senha, email_usuario, usuario, url, nome_app):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        postgres_insert_query = """ INSERT INTO contas (senha, email, usuario, url, nome_app) VALUES (%s, %s, %s, %s, %s)"""
        record_into_insert = (senha, email_usuario, usuario, url, nome_app)
        cursor.execute(postgres_insert_query, record_into_insert)
        conexao.commit()

    except (Exception, psycopg2.Error) as erro:
        print(erro)


def conectar():
    try:
        conexao = psycopg2.connect(user='root', password='root', host='127.0.0.1', database='password_manager')
        return conexao

    except (Exception, psycopg2.Error) as erro:
        print(erro)


def encontrar_app(nome_app):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        postgres_select_query = """ SELECT senha FROM contas WHERE nome_app = '""" + nome_app + "'"
        cursor.execute(postgres_select_query, nome_app)
        conexao.commit()
        resultado = cursor.fetchone()
        print("A senha é : ")
        print(resultado[0])

    except (Exception, psycopg2.Error) as erro:
        print(erro)

def encontrar_email(email_usuario):
    data = ('Senha: ', 'Email: ', 'usuario: ', 'url: ', 'Nome do App/Site: ')
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        postgres_select_query = """ SELECT * FROM contas WHERE email = '""" + email_usuario + "'"
        cursor.execute(postgres_select_query, email_usuario)
        conexao.commit()
        resultado = cursor.fetchall()
        print('')
        print('RESULTADO')
        print('')
        
        for fileira in resultado:
            for i in range(0, len(fileira) - 1):
                print(data[i] + fileira[i])
        print('')
        print('-'*30)

    except (Exception, psycopg2.Error) as erro:
        print(erro)    return input('Digite a opção que deseja: ')
KeyboardInterrupt

       



