from math import tan, cos, sin, radians
an = float(input('Digite o ângulo que você deseja: '))
se = sin(radians(an))
co = cos(radians(an))
tan = tan(radians(an))
print('O ângulo de {} tem o SENO de {:.2f}'.format(an, se))
print('O ângulo de {} tem como COSSENO de {:.2f}'.format(an, co))
print('O ângulo {} tem como TANGENTE de {:.2f}'.format(an, tan))