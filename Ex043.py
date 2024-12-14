peso = float(input('Qual o seu peso? (kg) '))
altura = float(input('Qual a sua altura? (m) '))
imc = peso / (altura ** 2 )
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print('PARABÉNS!, você está no PESO IDEAL')
elif 25 <= imc < 30:
    print('Você está com SOBREPESO, cuidado!')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE, cuidado!')
else:
    print('Você está em OBESIDADE MÓRBIDA')