texto = input('Digite o que deseja criptografar ou descriptografar: ')
tam = int("13")
opcao = input('Digite 1 para criptografar ou 2 para descriptografar: ')

if opcao == '1':
    for i in range(len(texto)):
        print (chr(ord(texto[i]) + tam), end='')
print ('')

if opcao == '2':
    for i in range(len(texto)):
        print (chr(ord(texto[i]) - tam), end='')
print ('')
