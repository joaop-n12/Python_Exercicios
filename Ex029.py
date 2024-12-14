velo = float(input('Qual a velocidade atual do carro? '))
if velo <= 80:
    print('Tenha ótimo dia! Dirija com segurança!')
else:
    print('''\033[1;31mMULTADO! Você excedeu o limite permitido que é de 80Km/h.
Você deve pagar uma multa de R${:.2f}!\033[m
Tenha um ótimo dia! Dirija com segurança!'''.format((velo-80) * 7))