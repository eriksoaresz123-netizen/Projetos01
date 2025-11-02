print(f'{"\033[30;41mLojas Stuart\033[m":=^40}')
valor = int(input('Digite o valor da compra: R$ '))
print('''
FORMAS DE PAGAMENTO
[ 1 ] à vista no dinheiro/pix com desconto de 15% 
[ 2 ] à vista no cartão com desconto de 5%
[ 3 ] em 2x no cartão sem juros
[ 4 ] em 3x no cartão com juros 
''')
escolhido = int(input('Selecione uma opção: '))
if escolhido == 1:
    total = valor - (valor * 15 / 100)
elif escolhido == 2:
    total = valor - (valor * 5 / 100)
elif escolhido == 3:
    total = valor
    valor = total / 2
    print(f'Sua compra foi parcelada em 2x de {valor:.2f}')
elif escolhido == 4:
    total = valor + (valor * 20 / 100 )
    parcelas = int(input('em quantas parcelas? '))
    parcela = valor / parcelas
    print(f'O valor da sua compra é de R${valor} em {parcelas}x com juros fica em R${parcela:.2f}')
print(f'O valor da sua compra é de R${valor} e o valor final é R${total} ')
