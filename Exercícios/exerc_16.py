from math import tan, cos, sin, radians
angulo = float(input('Digite o ângulo: '))
seno = sin(radians(angulo))
con = cos(radians(angulo))
tan = tan(radians(angulo))
print('O ângulo de {} tem o seno de {:.2f}, o cosseno de {:.2f} e a tangente de {:.2f}'.format(angulo, seno, con, tan))
