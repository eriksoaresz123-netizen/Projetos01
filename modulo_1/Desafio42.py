print('Formando um triângulo ')
r1 = float(input('Digite um número: '))
r2 = float(input('Digite um número: '))
r3 = float(input('Digite um número: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Da para formar um triângulo! ')
if r1 == r2 and r2 == r3 and r3 == r1:
    print('Formará o triângulo Equilátero! ')
if r1 == r2 or r1 == r3 or r2 == r3 or r3 == r1:
    print('Formará o triângulo Isósceles! ')
if r1 != r2 and r1 != r3 and r2 != r3 and r3 != r1:
    print('Formará o triângulo Escaleno!')

