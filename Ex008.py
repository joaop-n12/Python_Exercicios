print('Converter valor de metro em centímetros e em milímetros:')
me = float(input('Distância em metros? '))
cm = me * 1000
mm = me * 10000
print('{} metros, equivale a {:.0f} centímetros e {:.0f} milímetros'.format(me, cm, mm))