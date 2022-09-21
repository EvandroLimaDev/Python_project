print('Escolha qual fruta deseja comprar: ')
print('1 - maça')
print('2 - banana')
print('3 - laranja')
produto = int(input('Qual fruta voce escolheu ?'))
qtd = int(input('Quantidade ?'))
if (produto == 1):
    pagar = qtd * 2.3
    print('Voce comprou {} maça. total á pagar {}.'.format(qtd, pagar))
else:
    if (produto == 2):
        pagar = qtd * 3.6
        print('Voce comprou {} banana. total á pagar {}.'.format(qtd, pagar))
    else:
     if (produto == 3):
       pagar = qtd * 1.85
       print('Voce comprou {} laranja. total á pagar {}.'.format(qtd, pagar))
     else:
        print('Produto inexistente!')