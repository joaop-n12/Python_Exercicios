sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, Informe seu sexo: ')).strip().upper()[0]
if sexo == 'M':
    print('Sexo MASCULINO registrado cm sucesso')
else:
    print('Sexo FEMININO registrado com sucesso')