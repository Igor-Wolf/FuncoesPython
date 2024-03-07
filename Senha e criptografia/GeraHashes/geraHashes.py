import hashlib

string = input("Digite o texto a ser criptografado: ")


menu = int(input(''' MENU - ESCOLHA O TIPO DO HASH
             1 - MD5
             2 - SHA1
             3 - SHA256
             4 - SHA512
             Digite o número do hash a ser gerado: '''))


if menu == 1:
    resultado = hashlib.md5(string.encode('utf-8'))
    print("O hash MD5 da string é: ", resultado.hexdigest())
elif menu == 2:
    resultado = hashlib.sha1(string.encode('utf-8'))
    print("O hash sha1 da string é: ", resultado.hexdigest())
elif menu == 3:
    resultado = hashlib.sha256(string.encode('utf-8'))
    print("O hash sha256 da string é: ", resultado.hexdigest())
elif menu == 4:
    resultado = hashlib.sha512(string.encode('utf-8'))
    print("O hash sha512 da string é: ", resultado.hexdigest())
else:
    print("Algo de errado aconteceu")
