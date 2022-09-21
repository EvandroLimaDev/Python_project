km = float(input('Quantos km o carro rodou ?'))

days = float(input('Quantos dias o carro foi alugado ?'))

payment = 60 * days + 0.15 * km

print('Olá você rodou {} km por {} dias.'.format(km, days))
print('Você irá pagar R$ {}'.format(payment))