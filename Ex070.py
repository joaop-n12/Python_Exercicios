print(32*'-')
print('      LOJA SUPER BARATÃO')
print(32*'-')
soma = caro = menor = cont = 0
barato = ''
while True:
    nome = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    continuar = str(input('Quer continuar? [S/N] ')).upper()
    soma += preço
    if preço >= 1000:
        caro += 1
    if cont == 1:
        menor = preço
        barato = nome
    else:
        if preço < menor:
            menor = preço
            barato = nome
    if continuar == 'N':
        break
print('------- FIM DO PROGRAMA --------')
print(f'''O total da compra foi R${soma:.2f}
Temos {caro} produtos custando mais de R$1000.00
O produto mais barato foi {barato} que custa R${menor:.2f}''')