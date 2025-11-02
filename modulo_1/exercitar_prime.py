nota = float(input('Digite sua nota: '))
nota2 = float(input('Digite sua segunda nota: '))
m = (nota + nota2) / 2
if m < 5:
    print('Reprovado! ')
elif 5 <= m < 7:
    print('Em recuperação! ')
elif m >= 7:
    print('Aprovado! ')
print(f'Sua média é {m:.2f}')