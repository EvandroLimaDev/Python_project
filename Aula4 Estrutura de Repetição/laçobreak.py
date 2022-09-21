
words = input("Escreva uma frase: ")

while words != "sair":
    words = input('Escreva novamente uma frase: ')
print("Saindo do programa!")
#outra forma abaixo

print('Digite uma frase: ')
print('Digite "sair" para finalizar!')
while True:
    texto = input('')
    print(texto)
    if texto == 'sair':
        break
print('Encerrando programa!')
