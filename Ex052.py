num = int(input('Digite um número: '))
cont = 0
for c in range(1, num + 1):
    if num % c == 0:
        cont += 1
        print('\033[34m', end='')
    else:
        print('\033[m', end='')
    print('{} '.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(num, cont))
if cont == 2:
    print('Por isso ele é primo!')
else:
    print('Por isso ele não é primo!')