from create_hash import senha
import subprocess
from bd_manager import guardar_senhas, encontrar_usuario, encontrar_senha
from termcolor import colored


def menu():
    barra()
    print(colored('='*6, 'cyan') + ' Aqui você pode gerar uma senha para os seus sites e apps ' + colored('='*6, 'cyan'))
    print('1. Criar nova senha')
    print('2. Encontre sites e apps que usam um E-mail')
    print('3. Encontre a senha de um site ou app')
    print('Q. Sair')
    barra()
    return input('Digite a opção que deseja: ')


def barra():
    print(colored('='*70, 'cyan', attrs=['blink']))

def criar():
    barra()
    print('Digite o nome do app ou site que você deseja criar a senha')
    nome_app = input(': ')
    barra()
    print('Digite o texto de exemplo para a senha')
    texto = input(': ')
    barra()
    password = senha(texto, nome_app, 14)
    subprocess.run('xclip', universal_newlines=True, input=password)
    barra()
    print('')
    print('Sua senha foi criada e copiada para o seu clipboard')
    print('')
    barra()
    print('Por favor entre um e-mail para esse aplicativo ou site')
    email_usuario = input(': ')
    barra()
    print('Digite o username que será utilizado nesse app ou site (caso não haja um deixe em branco')
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
    encontrar_senha(nome_app)

def achar_conta():
    barra()
    print('Por favor entre o e-mail que quer encontrar a senha')
    email_usuario = input()
    barra()
    encontrar_usuario(email_usuario)


