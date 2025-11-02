from math import sin, cos, radians, tan
angulo = float(input('Digite um ângulo qualquer:'))
seno = sin(radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('O Ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))