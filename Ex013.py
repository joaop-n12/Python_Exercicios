sala = float(input('Qual o salário do funcionário? R$'))
novo = sala + (sala * 15 / 100)
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}.'.format(sala, novo))
