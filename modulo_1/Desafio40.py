nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
media = (nota1 + nota2) / 2
if media >= 7:
    print(f'A média do aluno foi {media} e ele foi aprovado! ')
elif media < 5:
    print('Reprovado! ')
else:
    print('Está de recuperação! ')