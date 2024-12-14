print('{:=^40}'.format(' MERCEARIA NUNES '))
while True:
    cpf = str(input('CPF na nota? [S/N] ')).upper()
    if cpf == 'S':
        cpfs = int(input('Digite seu CPF: '))
        correto = str(input(f'O cpf está correto : [S/N] {cpfs} \n')).upper()
        if correto == 'SIM':
            break
        else:
            print('Digite seu CPF novamente: ')
    else:
        break
print(40*'=')
valor = float(input('Preço das compras? R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
op = int(input('Qual é a opção? '))
if op == 1:
    print('Sua compra de R${:.2f}, irá custar R${:.2f} no final.'.format(valor, valor - (valor * 10 / 100)))
elif op == 2:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor, valor - (valor * 5 / 100)))
elif op == 3:
    print('Sua compra será parcelada em 2x de R${:.2f}.'.format(valor / 2 ))
elif op == 4:
    par = int(input('Em quantas vezes? '))
    vf = valor + (valor * 20 / 100)
    qp = vf / par
    print('Sua compra será parcelada em {}x de R${:.2f}, com juros, o total passará a ser R${:.2f}'.format(par, qp, vf))
else:
    print('''\033[1;31mOpção de pagamento INVÁLIDA. Tente novamente!\033[m'
Sua compra vai ficar R${:.2f} vai custar {:.2f} no final.'''.format(valor, valor))