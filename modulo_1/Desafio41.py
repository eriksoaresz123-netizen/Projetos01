from datetime import date as d
ano = d.today().year
nascimento = int(input('Digite o ano em que você nasceu: '))
idade = ano - nascimento
if idade <= 9:
    print('Você é da categoria MIRIM! ')
elif idade <= 14:
    print('Você é da categoria INFANTIL! ')
elif idade <= 19:
    print('Você é da categoria JUNIOR! ')
elif idade <= 21:
    print('Você é da categoria Sênior! ')
else:
    print('Você é da categoria MASTER! ')


