from secret import get_secret_key
from menu import menu, criar, achar_usuario, achar_email, achar_app, barra, cyan
import getpass
secret = get_secret_key()

barra()
senha = getpass.getpass('Digite a senha principal para começar a utilizar o Password Manager: ')
barra()
print('')
print('')
print('')
print('')


if senha == secret:
    barra()
    print(cyan('='*30) + '  Bem vindo ao Password Manager  ' + cyan('='*31))


else:
    barra()
    print('Você errou a senha, vaza !')
    exit()

escolha = menu()

while escolha != 'Q':  
    if escolha == '1':
        criar()
    if escolha == '2':
        achar_email()
    if escolha == '3':
        achar_app()
    if escolha == '4':
        achar_usuario()
    else:
        escolha = menu()

exit()

