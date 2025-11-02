cont = 0
soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += c
        soma += 1
print(f'A soma de todos os  {cont} valores solicitados é {soma} ')