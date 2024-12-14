print(25 * '=')
print('      Gerador de PA')
print(25 * '=')
pri = int(input('Primeiro termo: '))
razão = int(input('Razão PA: '))
termo = pri
contador = 1
while contador <= 10:
    print('{} >'.format(termo), end=' ')
    termo += razão
    contador += 1
print('Acabou')