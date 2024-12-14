num = soma = qd = 0
while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    qd += 1
    soma += num
print('Você digitou {} números e a soma entre eles é de {}.'.format(qd - 1, soma - 999))