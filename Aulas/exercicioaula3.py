num1 = int(input('Qual o valor ?'))
num2 = int(input('Qual o valor ?'))
print('Escolha a operação: ')
print('1 somar')
print('2 subtrair')
print('3 multiplicar')
print('4 dividir')
operacao = int(input('Qual operação você deseja realizar ?'))
while (operacao != 's'):
    if (operacao == 1):
        resultado = num1 + num2
        print('O resultado é {}!'.format(resultado))
    elif (operacao == 2):
        resultado = num1 - num2
        print('O resultado é {}!'.format(resultado))
    elif (operacao == 3):
        resultado = num1 * num2
        print('O resultado é {}!'.format(resultado))
    elif (operacao == 4):
        resultado = num1 / num2
        print('O resultado é {}!'.format(resultado))
else:
    print('Volte ao Menu.')

