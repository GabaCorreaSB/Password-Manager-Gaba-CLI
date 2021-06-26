from secret import get_secret_key
from menu import menu, criar, achar, achar_conta

secret = get_secret_key()

senha= input('Defina a senha principal para começar a utilizar o Password Manager.')

if senha== secret:
    print('Bem vindo ao Password Manager')

else:
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

