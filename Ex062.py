print(25 * '=')
print('      Gerador de PA')
print(25 * '=')
pri = int(input('Primeiro termo: '))
razão = int(input('Razão PA: '))
termo = pri
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print('{} >'.format(termo), end=' ',)
        termo += razão
        contador += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(contador))