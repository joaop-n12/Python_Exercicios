import random
n1 = input('Nome do aluno 1: ')
n2 = input('Nome do aluno 2: ')
n3 = input('Nome do aluno 3: ')
n4 = input('Nome do aluno 4: ')
lis = [n1, n2, n3, n4]
alu = random.choice(lis)
print('O aluno sorteado foi {}.'.format(alu))
