soma = 0
cont = 1
while (cont <= 5):
    x = float(input('Digite a {}° nota: '.format(cont)))
    soma += x #equivalente: soma = soma + x
    cont += 1 #equivalente: cont = cont + x
media = soma / 5
print('Media final: {}'.format(media))