valor = float(input('O valor do produto é:'))
desconto = valor - (valor * 5 / 100)
print('O valor do produto é R${}. Com 5% de desconto o valor ficará R${:.2f}'.format(valor, desconto))