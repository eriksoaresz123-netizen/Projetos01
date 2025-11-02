from random import randint
print(f'{"Vamos jogar JOKENPÔ!!!":=^40}')
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções são
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura ''')
jogador = int(input('Qual será sua jogada ? '))
print(f'O computador jogou {itens[computador]}')
print(f'O jogador jogou {itens[jogador]}')
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    else:
        print('COMPUTADOR VENCE')
if computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    else:
        print('JOGADOR VENCE')
if computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    else:
        print('EMPATE')
print('====fim de jogo====')


