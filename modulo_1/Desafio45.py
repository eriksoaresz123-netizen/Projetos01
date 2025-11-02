from random import randint
from time import sleep
print(f'Vamos jogar JOKENPÔ!!!')
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print(''' Suas opções são:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
''')
jogador = int(input('Qual será sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('-=' * 11)
print(f'computador jogou \033[30;41m{itens[computador]}\033[m')
print(f'jogador jogou \033[30;41m{itens[jogador]}\033[m')
print('-=' * 11)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    else:
        print('JOGADOR PERDE')
if computador == 1:
    if jogador == 0:
        print('JOGADOR PERDE ')
    elif jogador == 1:
        print('EMPATE')
    else:
        print('JOGADOR VENCE')
if computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('JOGADOR PERDE')
    else:
        print('EMPATE')

