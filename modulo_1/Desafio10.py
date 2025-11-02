nome = input('Digite seu nome:')
ano = int(input('Em que ano estamos?'))
nasc = int(input('Em que ano você nasceu?'))
idade = ano - nasc
real = float(input('Quanto de dinheiro você tem no momento? R$'))
dolar = real/5.58
euro = real/6.45
print('Olá {}! Seja bem-vindo! Você tem {} anos.\n Você tem {} reais. você pode comprar USD {:.2f} doláres e '
      'EUR {:.2f} euros! ''\n'
      .format(nome, idade, real, dolar, euro))
