cardapio1 = ['-='*15, '1- X-Burger - R$11,50', '2- X-Salada - R$12,50', '3- X-Bacon - R$13,00', 
            '4- X-EGG - R$13,50', '5- X-Frango - R$13,50', '6- X-Tudo - R$14,50', 
            '7- X-Tudo de Frango - R$14,50', '-='*15]
valores1 = [0, 11.50, 12.50, 13.00, 13.50, 13.50, 14.50, 14.50]

bebidas2 = ['-='*16, '1- Refrigerante Lata - R$4,00', '2- Refrigerante 600ml - R$6,00', 
           '3- Refrigerante 1L - R$8,00', '4- Refrigerante 2L - R$11,00', '-='*16]
valores2 = [0, 4.00, 6.00, 8.00, 11.00]

total = 0
solicitados1 = ''
solicitados2 = ''

while True:
    pedido1 = str(input('Deseja pedir algo para comer ? [S/N] ')).strip().upper()[0]
    
    if pedido1 in 'S':
        for comida in range(0, 9):
            print(f'{cardapio1[comida]}')
        pedido01 = int(input('Qual Hambúrguer deseja ? '))
        
        if pedido01 == 1:
            total += valores1[1]
            solicitados1 += str(', ') + str(pedido01)
        elif pedido01 == 2:
            total += valores1[2]
            solicitados1 += str(', ') + str(pedido01)
        elif pedido01 == 3:
            total += valores1[3]
            solicitados1 += str(', ') + str(pedido01)
        elif pedido01 == 4:
            total += valores1[4]
            solicitados1 += str(', ') + str(pedido01)
        elif pedido01 == 5:
            total += valores1[5]
            solicitados1 += str(', ') + str(pedido01)
        elif pedido01 == 6:
            total += valores1[6]
            solicitados1 += str(', ') + str(pedido01)
        elif pedido01 == 7:
            total += valores1[7]
            solicitados1 += str(', ') + str(pedido01)
        else:
            print('Pedido inválido. Tente novamente')
    elif pedido1 in 'ABCDEFGHIJKLMOPQRTUVWXYZ1234567':
        print('Opção inválida. Tente novamente')

    pedido2 = str(input('Deseja pedir algo para beber ? [S/N] ')).strip().upper()[0]

    if pedido2 in 'S':
        for bebida in range(0, 6):
            print(f'{bebidas2[bebida]}')
        
        pedido02 = int(input('Qual e a Bebida que deseja ? '))

        if pedido02 == 1:
            total += valores2[1]
            solicitados2 += str(', ') + str(pedido02)
        elif pedido02 == 2:
            total += valores2[2]
            solicitados2 += str(', ') + str(pedido02)
        elif pedido02 == 3:
            total += valores2[3]
            solicitados2 += str(', ') + str(pedido02)
        elif pedido02 == 4:
            total += valores2[4]
            solicitados2 += str(', ') + str(pedido02)
        else:
            print('Pedido inválido. Tente novamente')
    elif pedido2 in 'ABCDEFGHIJKLMOPQRTUVWXYZ1234':
        print('Opção inválida. Tente novamente')

    erro = str(input('Caso tenha errado algum pedido. Deseja tirar algo que tenha pedido ? [S/N] ')).strip().upper()[0]

    if erro in 'S':
         print('')
         print(f'pedidos até agora foram. para comer{solicitados1} e para beber{solicitados2}.')
         print('Você deseja remover:\n1-Comida\n2-Bebida')
         
         opção = int(input('Qual das opções ? '))
         
         if opção == 1:
              solicitados1 - str(opção)
         elif opção == 2:
              solicitados2 - str(opção)
         elif opção != 1 or opção != 2:
              print('Opção inválida. tente novamente')

    finalização = str(input('Deseja continuar pedindo ? [S/N] ')).strip().upper()[0]

    if finalização in 'N':
        break
    elif finalização in 'ABCDEFGHIJKLMOPQRTUVWXYZ':
        print('Opção inválida. Tente novamente')

print('')
print('-='*25)
print(f'Você pediu para comer os itens do cardipio{solicitados1}.')
print(f'Você pediu para beber os itens do cardipio{solicitados2}.')
print(f'Sua conta total ficou R${total:.2f}')

for comida in range(0, 9):
            print(f'{cardapio1[comida]}')

for bebida in range(0, 6):
            print(f'{bebidas2[bebida]}')

print('')