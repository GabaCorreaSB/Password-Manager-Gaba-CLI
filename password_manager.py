from secret import get_secret_key
from menu import menu, criar, achar, achar_conta, barra, cyan
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
    print(cyan('='*21) + '  Bem vindo ao Password Manager  ' + cyan('='*21))


else:
    barra()
    print('Você errou a senha, vaza !')
    exit()

escolha = menu()

while escolha != 'Q':
    if escolha == '1':
        criar()
    if escolha == '2':
        achar_conta()
    if escolha == '3':
        achar()
    else:
        escolha = menu()

exit()

