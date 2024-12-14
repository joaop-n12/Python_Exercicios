from random import randint
qnt = 0
print(15*'=-')
print('Vamos JOGAR PAR OU ÍMPAR')
print(15*'=-')
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(1, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
        print(15*'--')
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total} ', end= '')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    print(15*'--')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            qnt += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            qnt += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(15*'=-')
print(f'GAME OVER! Você ganhou {qnt} vezes.')