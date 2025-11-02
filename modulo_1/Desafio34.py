salario = float(input('Digite seu salário: '))
if salario <= 1518:
    aumento = salario + (salario * 15 / 100)
else:
    aumento = salario + (salario * 10 / 100)
print(f'Quem ganhava {salario} agora ganha {aumento}. ')