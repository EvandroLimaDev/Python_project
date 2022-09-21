print('Qual o tipo de instalação ?')
print('residencia')
print('industrial')
print('comercial')
inst = input('Qual o tipo ?')
if inst == 'residencia' or inst == 'industrial' or  inst == 'comecial':
 kwh = int(input('Qual a quantidade de KWH consumido ?'))

if inst == 'residencia' and kwh <= 500:
    valor = kwh * 0.40
    print('Você utilizou {} kwh, O valor a ser pago pela energia é R$ {}'.format(kwh, valor))
elif inst == 'residencia' and kwh > 500:
    valor = kwh * 0.65
    print('Você utilizou {} kwh, O valor a ser pago pela energia é R$ {}'.format(kwh, valor))
elif inst == 'comercial' and kwh <= 1000:
    valor = kwh * 0.55
    print('Você utilizou {} kwh, O valor a ser pago pela energia é R$ {}'.format(kwh, valor))
elif inst == 'comercial' and kwh > 1000:
    valor = kwh * 0.60
    print('Você utilizou {} kwh, O valor a ser pago pela energia é R$ {}'.format(kwh, valor))
elif inst == 'industrial' and kwh <= 5000:
    valor = kwh * 0.55
    print('Você utilizou {} kwh, O valor a ser pago pela energia é R$ {}'.format(kwh, valor))
elif inst == 'industrial' and kwh > 5000:
    valor = kwh * 0.60
    print('Você utilizou {} kwh, O valor a ser pago pela energia é R$ {}'.format(kwh, valor))






