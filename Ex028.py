import random
from time import sleep
print(20 * '-=-')
print('Vou pensar em um número entre 0 e 5. Tente advinhar... ')
print(20 * '-=-')
num = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
sor = random.randint(0,5)
if num == sor:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(sor, num))