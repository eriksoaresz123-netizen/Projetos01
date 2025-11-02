nome = str(input('Digite o nome do aluno: '))
nota1 = float(input('Digite a nota: '))
nota2 = float(input('Digite a nota: '))
media = (nota1 + nota2) / 2
print(f'Olá {nome}! Seja bem-vindo. ')
if nome == 'Erik':
    print('Esse aluno é o melhor que temos! ')
else:
    print('Ok esse não é o aluno que eu esperava')
if media >= 7:
    print('Você foi aprovado! ')

else:
    print('Você foi reprovado! ')
print('--fim--')