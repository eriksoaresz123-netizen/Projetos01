frase = str(input('Digite uma frase: ')).upper().strip()
print(f'A frase tem {frase.count('A')} letras A ')
print(f'A primeira vez que apareceu a letra A foi na posição {frase.find('A')+1}')
print(f'A última vez que apareceu a letra A foi na posição {frase.rfind('A')+1}')