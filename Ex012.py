v = float(input('Qual o valor do produto? R$'))
des = v - ( v * 5 / 100)
print('O produto que custava R${}, na promoção com desconto de 5% vai custar R${:.2f}'.format(v, des))