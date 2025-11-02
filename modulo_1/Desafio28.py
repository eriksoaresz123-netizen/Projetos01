from random import randint
computador = randint(1, 5 )
print('\033[37;40m-=-\033[m' * 20)
print('\033[30;43mEstou pensando em um número...                              \033[m ')
print('\033[37;40m-=-\033[m' * 20)
jogador = int(input('Tente adivinhar o número que a \033[34mCPU\033[m está pensando: '))
if jogador == computador:
    print('Parabéns você acertou o número que eu estava pensando! :) ')
else:
    print(f'Ops... não foi dessa vez! o número que eu estava pensando era \033[32m{computador}\033[m e não \033[31m{jogador}.\033[m ')
print('\033[34m---FIM DE JOGO---\033[m')
