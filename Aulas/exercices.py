valor = float(input('Qual o preço do produto?'))

p = float(input('Digite o percentual de desconto: (0-100)%: '))

desconto = valor * (p / 100)

final = valor - desconto

print('Olá, o preço é {} e o desconto é {}% '.format(valor, desconto))
print('Valor calculado de desconto: {}. Valor fina do produto: {}' .format(desconto,final))