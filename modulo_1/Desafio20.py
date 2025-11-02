from random import shuffle
n1 = str(input('1 nome:'))
n2 = str(input('2 nome:'))
n3 = str(input('3 nome:'))
n4 = str(input('4 nome:'))
escolhido = [n1, n2, n3, n4]
shuffle(escolhido)
print('A ordem do cardápio vai ser: ')
print(escolhido)