ni = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão: ')
print('''[ 1 ] converter para BINÁRIO 
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
op = int(input('Sua opção: '))
if op == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(ni, bin(ni)[2:]))
elif op == 2:
    print('{} convertido para OCTAL é igual a {}'.format(ni, oct(ni)[2:]))
elif op == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(ni, hex(ni)[2:]))
else:
    print('Opção inválida. Tente novamente')