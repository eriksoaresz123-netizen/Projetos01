velocidade = int(input('Digite a velocidade do carro: '))
if velocidade > 90:
    print('Você excedeu o limite de velocidade permitida. \n Tome mais cuidado! \n ')
    multa = (velocidade - 90) * 7
    print(f'Agora você deve pagar uma\033[1;31m multa\033[m no valor de \033[30;44mR${multa:.2f}\033[m! ')
else:
    print('Tenha um bom dia! Continue dirigindo com cuidado. ')


