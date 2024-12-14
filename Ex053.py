frase = input('Digite uma frase: ').strip().upper()
divisão = frase.split()
junção = ''.join(divisão)
inverso = ''
for c in range(len(junção) - 1, -1, -1):
    inverso += junção[c]
print('o inverso de {} é {}'.format(junção, inverso))
if inverso == junção:
    print('Por isso É um POLÍNDROMO!')
else:
    print('Por isso NÃO é um POLÍNDROMO!')