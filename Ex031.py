dis = float(input('Qual a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {:.1f}Km'.format(dis))
if dis <= 200:
    print('E o preço da sua passagem será de R${:.2f}'.format(dis * 0.5))
else:
    print('E o preço da sua passagem será de R${:.2f}'.format(dis * 0.45))