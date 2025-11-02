peso = float(input('Digite seu peso: (Kg) '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)
print(f'O IMC dessa pessoa é de {imc:.1f}. ')
if imc < 18:
    print('Você está abaixo do peso. Cuidado! ')
elif 18 <= imc < 25:
    print('Parabéns você está no seu peso ideal! ')
elif 25 <= imc < 30:
    print('Você está em sobrepeso! ')
elif 30 <= imc < 40:
    print('Você está em obesidade! ')
else:
    print('Você está em obesidade mórbita! cuidado. ')