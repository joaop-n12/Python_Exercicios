soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite {} valor: '.format(c)))
    if num % 2 == 0:
        cont += 1
        soma += num
print('Você informou {} números PARES, e a soma é de {}.'.format(cont, soma))