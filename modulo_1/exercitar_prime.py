n = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print(f'{n} x {c:2} = \033[30;41m{c*n:2}\033[m ')