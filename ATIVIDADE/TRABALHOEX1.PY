print('Bem Vindo ao Atacado do Evandro Campos Lima!')#Identificação
valor = float(input('Digite o valor do produto: '))
quantidade = int(input('Digite a quantidade que deseja comprar: '))
total = valor * quantidade

if quantidade <= 4:
    valorFinal = total #não ganha desconto
elif 5 <= quantidade <= 19:
    valorFinal = total - total * 0.03 #desconto de 3
    desconto = 3
elif 20 <= quantidade <= 99:
    valorFinal = total - total * 0.06 #desconto de 6
    desconto = 6
else: #maior ou igual a 100
    valorFinal = total - total * 0.10 #desconto de 10
    desconto = 10

print('O valor sem desconto é de: R$ {:.2f}'.format(total))
print('O valor com desconto é de: R$ {:.2f} | (Desconto de: {}%)'.format(valorFinal,desconto))


