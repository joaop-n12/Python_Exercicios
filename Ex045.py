from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogada = int(input('Qual a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('POO!!!!!')
sleep(1)
print(11 * '=-')
print('O computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogada]))
print(11 * '=-')
if computador == 0:
    if jogada == 0:
        print('EMPATE')
    elif jogada == 1:
        print('JOGADOR VENCEU')
    elif jogada == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1:
    if jogada == 0:
        print('COMPUTADOR VENCE')
    elif jogada == 1:
        print('EMPATE')
    elif jogada == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2:
    if jogada == 0:
        print('JOGADOR VENCE')
    elif jogada == 1:
        print('COMPUTADOR VENCE')
    elif jogada == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
else:
    print('OPÇÃO INVÁLIDA')