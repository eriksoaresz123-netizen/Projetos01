d = int(input('Qual a quantidade de dias que o carro foi alugado?'))
km = float(input('Quantos km o carro percorreu?'))
pago = (d * 60) + (km * 0.15)
print(' O  total a pagar é de R${:.2f}'.format(pago))