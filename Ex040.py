n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}.'.format(n1, n2, media))
if media < 5.0:
    print('O aluno está \033[1;31mREPROVADO\033[m')
elif media >= 7.0:
    print('O aluno está \033[1;32mAPROVADO\033[m')
else:
    print('O aluno está de \033[1;33mRECUPERAÇÃO\033[m')