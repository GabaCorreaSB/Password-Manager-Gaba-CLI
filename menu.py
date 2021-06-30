from create_hash import senha
import subprocess
from bd_manager import guardar_senhas, encontrar_email, encontrar_app
from termcolor import colored


def menu():
    barra()
    print(cyan('='*11) + ' Aqui você pode gerar uma senha para os sites e apps ' + cyan('='*11))
    print(cyan('='*11) + '                 1. Criar nova senha                 ' + cyan('='*11))
    print(cyan('='*11) + '     2. Encontre sites e apps que usam um E-mail     ' + cyan('='*11))
    print(cyan('='*11) + '        3. Encontre a senha de um site ou app        ' + cyan('='*11))
    print(cyan('='*11) + '                       Q. Sair                       ' + cyan('='*11))
    barra()
    return input('Digite a opção que deseja: ')

def cyan(parametro):
    cor = colored(parametro, 'cyan', attrs=['bold'])
    return cor
    
def barra():
    print(cyan('='*75))

def criar():
    barra()
    print('Digite o nome do app ou site que você deseja criar a senha')
    barra()
    nome_app = input(': ')
    barra()
    print('Digite o texto de exemplo para a senha')
    barra()
    texto = input(': ')
    barra()
    password = senha(texto, nome_app, 14)
    barra()
    print('')
    print('Sua senha foi criada e copiada para o seu clipboard')
    print('')
    barra()
    print('Por favor entre um e-mail para esse aplicativo ou site')
    barra()
    email_usuario = input(': ')
    barra()
    print('Digite o username que será utilizado nesse app ou site (caso não haja um deixe em branco')
    barra()
    usuario = input(': ')
    barra()
    if usuario == None:
        username = ''
    print('Digite a URL do site ou app')
    url = input(': ')
    barra()
    guardar_senhas(password, email_usuario, usuario, url, nome_app)

def achar():
    barra()
    print('Digite o nome do app ou site que deseja verificar a senha')
    nome_app = input(': ')
    barra()
    encontrar_app(nome_app)

def achar_conta():
    barra()
    print('Por favor entre o e-mail que quer encontrar a senha')
    email_usuario = input()
    barra()
    encontrar_email(email_usuario)

def achar_usuario():



