from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
sair = False
while not sair:
    print('''    [ 1 ] somar\n    [ 2 ] multiplicar\n    [ 3 ] maior\n    [ 4 ] novos números\n    [ 5 ] sair do programa''')
    opi = int(input('>>>> Qual é a sua opção? '))
    if opi == 5:
        sair = True
        print('Finalizando...')
    else:
        if opi == 1:
            print('A soma entre {} e {} é {}'.format(n1, n2, n1 + n2))
        elif opi == 2:
            print('O resultado de {} x {} é {}'.format(n1, n2, n1 * n2))
        elif opi == 3:
            if n1 > n2:
                maior = n1
            else:
                maior = n2
            print('Entre {} e {}, o maior valor é {}'.format(n1, n2, maior))
        elif opi == 4:
            print('Informe os números novamente:')
            n1 = int(input('Primeiro valor: '))
            n2 = int(input('Segundo valor: '))
        else:
            print('Informação inválida. Tente Novamente')
    print(17 * '\033[1m-=\033[m')
    sleep(2)
print('Fim do programa! Volte sempre')