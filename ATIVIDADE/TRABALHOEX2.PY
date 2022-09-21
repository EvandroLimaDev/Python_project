cardapio = { #Declaração do cardápio
    21: ['Napolitana', 20, 26],
    22: ['Margherita', 20, 26],
    23: ['Calabresa', 25, 32.50],
    24: ['Toscana', 30, 39],
    25: ['Portuguesa', 30, 39]
}
def ImprimirCardapio(cardapio: dict): #função para impressão do cardapio
    cabecalho = f"| {'Código':^10s} | {'Descrição':^20s} | {'Pizza Média':^15s} | {'Pizza Grande':^15s} |"

    print(f"{'Cardápio':-^{len(cabecalho)}s}")
    print(cabecalho)
    print("-" * len(cabecalho))
    for codigo, produtos in cardapio.items():
        print(f"| {codigo:^10} | {produtos[0]:^20} | {f'R$ {produtos[1]:.2f}':^15} | {f'R$ {produtos[2]:.2f}':^15} |")
    print("-" * len(cabecalho))
def SelecionarTamanho():  #Função para selecionar o tamanho da pizza.
   while True:
       try:
          tamanho = input('Qual o tamanho da pizza que você deseja (M/G): ')
          if tamanho not in ['M', 'G']:
             print('\nTamanho inválido.\n')
             continue
          else:
              break
       except ValueError:
           print('\nDigite um código váldo.\n')
   return tamanho

def SelecionarSabor():  # Função para selecionar o sabor da pizza.
    while True:
        try:
          codigo = int(input('Qual o código do sabor da pizza que você deseja  '))
          if codigo not in cardapio.keys():
             print('\nCódigo informado inválido.\n')
             continue
          else:
              print(f'Você pediu uma pizza {cardapio[codigo][0]}')
              break
        except ValueError:
            print('\nDigite um código váldo.\n')
    return codigo
print('Bem-vindo a Pizzaria do Evandro Campos Lima') #identificador pessoal
ImprimirCardapio(cardapio.copy()) #imprimindo o cardápio
total = 0
while True:
    tamanho = SelecionarTamanho() #seleção tamanho
    sabor = SelecionarSabor() #seleção sabor
    if tamanho == 'M':
        total += cardapio[sabor][1]
    elif tamanho == 'G':
         total += cardapio[sabor][2]
    else:
        total += 0

    print('\nDeseja pedir mais alguma coisa?')#pergunta se deseja continuar
    print('1 - SIM')
    print('0 - NÃO')

    while True:#valida a opção informada
        try:
            continuar = int(input('Escolha:'))

            if continuar not in [0, 1]: #obriga o usuario escolher apenas 0 ou 1
                 print('\nOpção inválida.')
                 continue
            else:
                break
        except ValueError: #caso o usuario não siga a instrução
            print('\nOpção inválida')
    if continuar == 0: #se a escolha for 0, então encerra e imprimi o total
        print(f'\n O Total a ser pago é: R$ {total:.2f}')
        break





