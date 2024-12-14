print(30 * '=')
print('    10 TERMOS DE UMA PA')
print(30 * '=')
pri = int(input('Primeiro termo: '))
ra = int(input('Razão: '))
deci = pri + (10 - 1) * ra
for c in range(pri, deci + ra, ra):
    print('{} '.format(c), end='> ')
print('Acabou')