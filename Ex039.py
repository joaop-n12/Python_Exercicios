from datetime import date
print('\033[4;31mFormulário de Alistamento\033[m')
print(36 * '-=')
atual = date.today().year
print('''Qual o seu sexo?
[ 1 ] Masculino 
[ 2 ] Feminino''')
sexo = int(input('R: '))
if sexo == 2:
    print('Você não precisa participar!')
    exit()
else:
    print('Iniciando formulário...')
nasc = int(input('Ano de nascimento: '))
id = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, id, atual))
if id > 18:
    print('''Você já deveria ter se alistado há {} anos.
Seu alistamento foi em {}.'''.format(id - 18, atual - (id - 18)))
elif id == 18:
    print('Você deve se alistar \033[1;31mIMEDIATAMENTE\033[m.')
else:
    print('''Ainda faltam {} anos para o alistamento.
Seu alistamento será em {}.'''.format(18 - id, atual + (18 - id)))