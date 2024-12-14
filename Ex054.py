from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for c in range(1, 8):
    nascimento = int(input(f'Em que ano a {c + 0}ª pessoa nasceu? '))
    idade = atual - nascimento
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print('''Ao todo tivemos {} pessoas maiores de idade
E também tivemos {} pessoas menores de idade'''.format(totmaior, totmenor))