from math import factorial
num = int(input('Digite um número para\nCalcular seu fatorial: '))
c = num
f = 1
print('Calculando {}!'.format(c),end='= ')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))