print('Calculadora')
print('Escolha a operação: ')
print('+ somar')
print('- subtrair')
print('* multiplicar')
print('/ dividir')

operacao = (input('Qual operação você deseja realizar ?'))
if operacao == '+' or operacao == '-' or operacao == '*' or operacao == '/':
    num1 = int(input('Qual o valor ?'))
    num2 = int(input('Qual o valor ?'))

while (operacao != 's'):
        if (operacao == '+'):
                resultado = num1 + num2
                print('O resultado é {} + {} = {}'.format(num1, num2, resultado))
        elif (operacao == '-'):
                resultado = num1 - num2
                print('O resultado é {} - {} = {}'.format(num1, num2, resultado))
        elif (operacao == '*'):
                resultado = num1 * num2
                print('O resultado é {} * {} = {}'.format(num1, num2, resultado))
        elif (operacao == '/'):
                resultado = num1 / num2
                print('O resultado é {} / {} = {}'.format(num1, num2, resultado))

        operacao = (input('Qual operação você deseja realizar ?'))
        if operacao == '+' or operacao == '-' or operacao == '*' or operacao == '/':
            num1 = int(input('Qual o valor ?'))
            num2 = int(input('Qual o valor ?'))

        print('Encerrando programa')
