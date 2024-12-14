lar = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
a = lar * alt
lit = a / 2
print('Sua parede tem dimensão de {} x {} e a sua área é de {},m².'.format(lar, alt, a))
print('Para pintar essa parede, você precisará de {}L de tinta.'.format(lit))
