#mochila = ('machado', 'camisa', 'bacon', 'abacate')
#print(mochila)

#print(mochila[0])  # print do elemento 1
#print(mochila[2])  # print do elemento 3
#print(mochila[0:2])  # print dos elementos 1 e 2 - indice 0 e 1
#print(mochila[2:])  # print do elemento a partir do indice 2
#print(mochila[-1])  # print do ultimo

#for item in mochila:
    #print('Na minha mochila tem: {}'.format(item))

#tam = len(mochila)
#for i in range(0, tam, 1):
 #print('Na minha mochila tem: {}'.format(mochila[1]))

#mochila = ('machado', 'camisa', 'bacon', 'abacate')
#upgrade = ('queijo', 'canivete')
#mochila_grande = mochila + upgrade

#print(mochila)
#print(upgrade)
#print(mochila_grande)


def soma(*num): # * desempacotamento
    soma = 0
    print('Tupla: {}'.format(num))
    for i in num:
      soma += i
    return soma
#programa principal
print('Resultado: {}\n'.format(soma(1,2)))
print('Resultado: {}\n'.format(soma(1,2,3,4,5,6,7,8,9)))