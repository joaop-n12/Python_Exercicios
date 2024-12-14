somaid = 0
mediaid = 0
maiorid = 0
nomevelho = ''
totalm = 0
for c in range(1, 6):
    print(f'\033[1m---------- {c + 0}ª PESSOA ----------\033[m')
    nome = str(input('\033[1mNome: \033[m')).capitalize()
    idade = int(input('\033[1mIdade: \033[m'))
    sexo = str(input('\033[1mSexo [M/F]: \033[m')).upper()
    somaid += idade
    if c == 1 and sexo == 'M':
        maiorid = idade
        nomevelho = nome
    if sexo == 'M' and idade > maiorid:
        maiorid = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
         totalm += 1
mediaid = somaid / 5
print('A média de idade do grupo é de {} anos'.format(mediaid))
print('O homem mais velho tem {} anos e se chama {}'.format(maiorid, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totalm))