casa = float(input('Digite o valor da casa:R$ '))
salario = float(input('Digite o salário do comprador:R$ '))
anos = int(input('Digite os anos que vai ficar pagando: '))
parcelas = casa / (anos * 12)
minimo = salario * 50 / 100
if parcelas <= minimo:
    print(f'Empréstimo aprovado! \n O Valor das parcelas vai ser de R${parcelas:.2f} reais. Você ficará pagando por {anos} anos. ')
else:
    print('Empréstimo negado! ')