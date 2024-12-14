import random
qp = 0
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue advinhar qual foi?''')
sor = random.randint(0, 10)
acertou = False
while not acertou:
    palp = int(input('Qual é o seu palpite? '))
    qp += 1
    if palp == sor:
        acertou = True
    else:
        if palp > sor:
            print('Menos... Tente mais uma vez')
        if palp < sor:
            print('Mais... Tente mais uma vez')

print(f'acertou com {qp} tentativas. Parabéns!')