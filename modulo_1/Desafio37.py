num = int(input('Digite um número: '))
print('''Escolha uma das opções abaixo que deseja fazer a conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL ''')
escolhido = int(input('Sua escolha: '))
if escolhido == 1:
    print(f'{num} em binário é {bin(num)[2:]}')
elif escolhido == 2:
    print(f'{num} em octal é {oct(num)[2:]} ')
elif escolhido == 3:
    print(f'{num} em hexadecimal é {hex(num)[2:]} ')
else:
    print('Opção inválida! ')