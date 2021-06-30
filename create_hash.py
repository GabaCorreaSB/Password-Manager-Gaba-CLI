from hashlib import sha256
import random
from secret import get_secret_key

SECRT_KEY = get_secret_key()

# função para a criação da senha utilizando metodo de retorno de string em
# digitos hexadecimal junto com a função get_hexdigest
def criar_senha(texto, nome_app):
    salt = get_hexdigest(SECRT_KEY, nome_app)[:20]
    hsh = get_hexdigest(salt, texto)
    return ''.join((salt,hsh))

# função de criação do hash da senha utilizando encriptação SHA-256 
def get_hexdigest(salt, texto):
    return sha256((salt + texto).encode('utf-8')).hexdigest()

# função para a criação da senha final, com os caracteres do alfabeto
# criado nessa função, com os parametros estabelecidos pelo utilizador 
# do programa
def senha(texto, nome_app, comprimento):
    hex_bruto = criar_senha(texto, nome_app)
    ALPHABET = ('abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', '0123456789', '(,._-*~"<>/|!@#$%^&)+=')

    numero = int(hex_bruto, 16)

    caracteres = []

    while len(caracteres) < comprimento:
        x = random.randint(0, len(ALPHABET) - 1)
        alpha = ALPHABET[x]
        x = random.randint(0, len(alpha) - 1)
        caracteres.append(alpha[x])

    return ''.join(caracteres)

