sa= float(input('Qual o salário do funcionário? R$'))
if sa <= 1250.00:
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(sa, sa + (sa * 15 / 100)))
else:
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(sa, sa + (sa * 10 / 100)))