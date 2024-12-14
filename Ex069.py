maiores = menores = homens = 0
while True:
    print(30 * '-')
    print('     CADASTRE UMA PESSOA')
    print(30 * '-')
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).upper()
    print(30*'-')
    continuar = str(input('Quer continuar? [S/N] ')).upper()
    if idade >= 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        menores += 1
    if continuar == 'N':
        break
print(f'''Total de pessoas com mais de 18 anos: {maiores}
Ao todo temos {homens} homens cadastrados
E temos {menores} mulheres com menos de 20 anos''')