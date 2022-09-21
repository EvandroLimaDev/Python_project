cardapio = { #impressão cardapio
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