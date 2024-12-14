casa = float(input('Valor da casa: R$'))
sala = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prest = casa / (anos * 12)
mi = sala * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de \033[4mR${:.2f}\033[m.'.format(casa, anos, prest))
if prest <= mi:
    print('\033[1;32mEmpréstimo pode serer CONCEDIDO!\033[m')
else:
    print('\033[1;31mEmpréstimo NEGADO!\033[m')