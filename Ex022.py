nome = input('Digite seu nome completo: ').strip()
print('Analisando seu nome... ')
print('Seu nome em letras maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome ao todo tem {} letras'.format(len(nome) - nome.count(' ')))
retirar = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(retirar [0], len(retirar)))


#frase = nome
#mai = frase.upper()
#min = frase.lower()
#tl = len(frase) - nome.count(' ')
#separa = frase.split()
#pn = separa[0]
#pnl = len(separa)
#print('''Seu nome em maiúsculas é {}
#Seu nome em minúsculas é {}
#Seu nome tem ao todo {} letras
#Seu primeiro nome é {} e ele tem {} letras'''.format(mai, min, tl, pn, pnl))
