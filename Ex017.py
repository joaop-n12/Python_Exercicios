from math import sqrt
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
soma = (co ** 2) + (ca ** 2)
print('A hipotenusa vai medir {:.2f}.'.format(sqrt(soma)))
