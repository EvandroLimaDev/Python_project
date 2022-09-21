nome = input('Qual o nome da pessoa ?')
idade = int(input('Qual a idade ?'))

if nome == 'vinicius':
    print('Olá vinicius!')
elif idade <= 18:
    print('Você não é vinicius!E é Menor de idade')
elif idade >= 100:
    print('Está pessoa não existe!')