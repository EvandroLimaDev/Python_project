#----------COMEÇO DA FUNÇÃO SERVIÇOCÃO----------
def servicoCao():
   while True:
      servicoC = input('Escolha o serviço desejado: \nBA - Banho\nTO - Tosa\nBT - Banho e Tosa\n>>')
      if servicoC == 'BA':
            return 10.00
      elif servicoC == 'TO':
            return 20.00
      elif servicoC == 'BT':
            return 25.00
      else:
            print('Para de Digitar serviços que não existem.')
            continue

#----------FIM DA FUNÇÃO SERVIÇOCÃO-------------
#----------COMEÇO DA FUNÇÃO PESOCÃO-------------
def pesoCao():
       while True:
           try:
              pesoC = float(input('Entre com o peso do cachorro(KG): '))
              if  0 <= pesoC <= 10:
                    return 1.5
              elif (pesoC > 10) and (pesoC <= 20):
                    return 2.0
              elif (pesoC > 20) and (pesoC <= 30):
                    return 2.5
              elif (pesoC > 30) and (pesoC <= 40):
                    return 3.0
              elif (pesoC > 40):
                    return 4.0
              else:
                    print('Não aceitamos cachorro com peso negativo, tente de novo!')
              return pesoC
           except ValueError:
               print('Pare de digitar valores não númericos. tente novamente')
               continue

#----------FIM DA FUNÇÃO PESOCÃO----------------
#----------COMEÇO DA FUNÇÃO PELOCÃO-------------
def peloCao():
    while True:
            peloC = input('Entre com o pelo do cachorro: \nC - Curto\nM - Médio\nG - Grande\n>>')
            if peloC == 'C':
                return 1.5
            elif peloC == 'M':
                return 2.0
            elif peloC == 'G':
                return 2.5
            else:
                print('tente de novo!')
            print('Pare de digitar pelos que não existem. tente novamente')
            continue

#----------FIM DA FUNÇÃO PELOCÃO----------------
#----------COMEÇO DA MAIN-----------------------
print('Bem-vindo ao PetShop do Evandro Lima!')
print('O valor total foi de: R$ {:.2f}'.format(servicoCao() * pesoCao() * peloCao()))

#----------FIM DA MAIN--------------------------