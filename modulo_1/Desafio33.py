a = int(input('Digite um número: '))
b = int(input('Digite um número: '))
c = int(input('Digite um número: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print(f'O número {menor} é o menor. ')
maior = c
if b > a and b > c:
    maior = b
if a > c and a > b:
    maior = a