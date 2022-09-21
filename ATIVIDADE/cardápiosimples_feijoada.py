identificador_pessoal = 'Evandro Campos Lima' #Identificador pessoal

opcoesFeijoada = { #imprimir as opções
    'b': ['Básica (Feijão + Paiol + Costelinha)', 1],
    'p': ['Premium (Feijão + Paiol + Costelinha + Partes de porco)', 1.25],
    's': ['Suprema (Feijão + Paiol + Costeilinha + Partes do porco + Charque + Calabresa + Bacon)', 1.50]
}

acompanhamentos = { #imprimir os acompanhamentos
    0:['Não desejo mais acompanhamentos (encerrar pedido)', 0],
    1:['200g de arroz', 5],
    2:['150g de farofa especial', 6],
    3:['100g de couve cozida', 7],
    4:['1 laranja descascada', 3]
}

def volumeFeijoada(): #função que solicita e valia o volume da feijoada
    valor = 0

    while True:
        try:
            volume = float(input('Entre com a quantidade que deseja (ml): ').strip().upper())
            if volume < 300 or volume > 5000: #usuario tem que escolher um valor entre 300 a 5000
                    print('Não aceitamos porções menores que 300ml ou maior que 5l. tente novamente!')
            else:
                valor = volume * 0.08 #calculo
                break
        except ValueError: #Caso o usuario não siga a orientação
            print('Digite um volume válido. ')
    return valor #retornando o valor de volume solicitado pelo usuario

def opcaoFeijoada():#função que vai solicitar e validar o menu da feijoada
    multiplicador = None

    while True:
        try:
            print('Entre com a opção de Feijoada: ')
            for key, values in opcoesFeijoada.items():
                print(f'{key} - {values[0]}')

            opcao = input().strip().lower()

            if opcao not in opcoesFeijoada.keys():
                print('Opção inválida')
            else:
                multiplicador = opcoesFeijoada[opcao][1]
                break
        except ValueError:
            print('Digite uma opção válida.')
    return multiplicador
def acompanhamentoFeijoada():#funçaão que vai solicitar e validar os acompanhamentos

    total_acompanhamento = 0

    while True:
        try:
            print('Deseja mais algum acompanhamento: ')
            for key, values in acompanhamentos.items():
                print(f'{key} - {values[0]}')

            opcao = int(input())

            if opcao not in acompanhamentos.keys():
                print('Opção inválida')
            elif opcao == 0:
                break
            else:
                total_acompanhamento += acompanhamentos[opcao][1]
        except ValueError:
            print('Digite um acompanhamento válido.')
    return total_acompanhamento
print(f'Bem-vindos(as) ao Programa de Feijoada do(a) {identificador_pessoal}')

valor = volumeFeijoada()
opcao = opcaoFeijoada()
adicionais = acompanhamentoFeijoada()

total = (valor * opcao) + adicionais #calculo total a ser pago

print(f'No valor a ser pago é (R$): {total:.2f} (volume = {valor:.2f} * opcao = {opcao:.2f} + Acompanhamento = {adicionais:.2f})') #imprimir o resultado final