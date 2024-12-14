tuple = (int(input('Digite um número: ')),
         int(input('Digite outro número: ')),
         int(input('Digite mais um número: ')),
         int(input('Digite um último número: ')))
print(15*'-=')
print(f'Você digitou os valores {tuple}')
if 9 in tuple:
    print(f'O número 9 apareceu {tuple.count(9)} vezes')
else:
    print('O valor 9 não foi digitado nenhuma vez')
if 3 in tuple:
    print(f'O valor 3 apareceu na {tuple.index(3)+1}ª posição')
else:
    print('O número 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ', end='')
for n in tuple:
    if n % 2 == 0:
        print(n, end=' ')