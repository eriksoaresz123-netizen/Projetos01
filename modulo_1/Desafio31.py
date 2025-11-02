viagem = float(input('Quantos km irá percorrer essa viagem? '))
if viagem >= 200:
    valor = viagem * 0.50

else:
    valor = viagem * 0.45

print(f'Você irá percorrer {viagem}km/h e deverá pagar \033[34;40m R${valor} reais.\033[m ')
