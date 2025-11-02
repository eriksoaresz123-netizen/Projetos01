from random import choice
n1 = str(input('Produto 1:'))
n2 = str(input('Produto 2:'))
n3 = str(input('Produto 3:'))
n4 = str(input('Produto 4:'))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print(f'O escolhido foi {escolhido}')