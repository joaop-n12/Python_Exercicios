n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))
if  n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n3:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if n1 == n2 == n3:
        print('EQUILÁTERO')
    elif n1 != n2 != n3:
        print('ESCALENO')
    else:
        print('ISÓCELES')
else:
    print('Os segmentos NÃO PODEM FORMAR um triângulo')