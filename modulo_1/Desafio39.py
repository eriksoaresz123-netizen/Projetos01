from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano em que nasceu: '))
idade = atual - nasc
print(f' Quem nasceu em \033[31;40m{nasc}\033[m tem \033[34;40m{idade}\033[m anos em \033[36;40m{atual}\033[m. ')
if idade == 18:
    print('Você deve se alistar IMEDIATAMENTE! ')
elif idade < 18:
    print(f'Você ainda vai se alistar! ')
    saldo = 18 - idade
    print(f'Falta {saldo} anos para o seu alistamento militar! ')
    ano = atual + saldo
    print(f'Seu alistamento vai ser em {ano}! ')
else:
    print('Seu alistamento está ATRASADO! ')
    saldo = idade - 18
    print(f'Você deveria ter se alistado a {saldo} anos atrás. ')
    ano = atual - saldo
    print(f'Seu alistamento foi em {ano}! ')
