n1 = float(input('Primeira nota do aluno:'))
n2  = float(input('Segunda nota do aluno:'))
m = (n1 + n2) / 2
print('A média da nota do aluno é {}!'.format(m))

if m >= 7:
    print('Está aprovado!')
else:
    print(' Que peninha, está reprovado!')