nume = int(input('Informe um número: '))
print('Analisando o {}'.format(nume))
u = nume // 1 % 10
d = nume // 10 % 10
c = nume // 100 % 10
m = nume // 100 % 10
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))