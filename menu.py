from create_hash import senha
import subprocess
from bd_manager import guardar_senhas, encontrar_email, encontrar_app, encontrar_usuario
from termcolor import colored


def menu():
    barra()
    print(cyan('='*11) + '           Aqui você pode gerar uma senha para os sites e apps          ' + cyan('='*11))
    print(cyan('='*11) + '                                                                        ' + cyan('='*11))
    print(cyan('='*11) + '                           1. Criar nova senha                          ' + cyan('='*11))
    print(cyan('='*11) + '                                                                        ' + cyan('='*11))
    print(cyan('='*11) + '         2. Encontre sites e apps que usam um E-mail especifico         ' + cyan('='*11))
    print(cyan('='*11) + '                                                                        ' + cyan('='*11))
    print(cyan('='*11) + '            3. Encontre a senha de um app ou site especifico            ' + cyan('='*11))
    print(cyan('='*11) + '                                                                        ' + cyan('='*11))
    print(cyan('='*11) + '         4. Econtre sites e apps que usam um Usuario especifico         ' + cyan('='*11))
    print(cyan('='*11) + '                                                                        ' + cyan('='*11))
    print(cyan('='*11) + '                                 Q. Sair                                ' + cyan('='*11))
    barra()
    return input('Digite a opção que deseja: ')

def cyan(parametro):
    cor = colored(parametro, 'cyan', attrs=['bold'])
    return cor
    
def barra():
    barra = print(cyan('='*94))
    return barra

def criar():
    barra()
    nome_app = input('Digite o nome do app ou site que você deseja criar a senha:  ')
    barra()
    texto = input('Digite o texto de exemplo para a senha:  ')
    barra()
    password = senha(texto, nome_app, 14)
    print('')
    print(f'Sua senha foi criada, sua senha é {password}')
    print('')
    barra()
    email_usuario = input('Por favor entre um e-mail para esse aplicativo ou site:  ')
    barra()
    usuario = input('Digite o username que será utilizado nesse app ou site (caso não haja um deixe em branco):  ')
    barra()
    if usuario == None:
        username = ''
    url = input('Digite a URL do site ou app:  ')
    barra()
    guardar_senhas(password, email_usuario, usuario, url, nome_app)

def achar_app():
    barra()
    nome_app = input('Digite o nome do app ou site que deseja verificar a senha:  ')
    barra()
    barra()
    encontrar_app(nome_app)

def achar_email():
    barra()
    email_usuario = input('Por favor entre o e-mail que quer encontrar a senha:  ')
    barra()
    encontrar_email(email_usuario)

def achar_usuario():
    barra()
    usuario = input('Por favor entre o usuario que quer encontrar a senha:  ')
    barra()
    encontrar_usuario(usuario)