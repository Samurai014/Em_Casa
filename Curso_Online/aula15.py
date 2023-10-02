#Desafio 66
# s = cont = 0
# while True:
#     n = int(input('Digite um valor (999 para parar): '))
#     if n == 999:
#         break
#     cont += 1
#     s += n 
# print(f'A soma dos {cont} valores foi {s}!')

#Desafio 67
# while True:
#     n = int(input('Quer ver a tabuada de qual valor? '))
#     print('-'*30)
#     if n < 0:
#         break
#     for c in range(1, 11):
#         print(f'{n} x {c} = {n*c}')
#     print('-'*30)
# print('Programa tabuada encerrado. Volte sempre!')

#Desafio 68
# from random import randint

# v = 0

# while True:
#     Jogador = int(input('Diga um valor: '))
#     computador = randint(0, 11)
#     total = Jogador + computador
#     tipo = ' '

#     while tipo not in 'PI':
#         tipo = str(input('Par ou Ímpar? ')).strip().upper()[0]
    
#     print(f'Você jogou {Jogador} e o {computador}. Total de {total} ', end='')
#     print('deu par' if total % 2 == 0 else 'deu ímpar')

#     if tipo == 'P':
#         if total % 2 == 0:
#             print('você venceu!')
#             v += 1
#         else:
#             print('você perdeu!')
#             break
#     elif tipo == 'I':
#         if total % 2 == 1:
#             print('você venceu!')
#             v += 1
#         else:
#             print('você perdeu!')
#             break
#     print('Tente novamente...')
# print(f'Game over! você venceu {v} vezes!')

#Desafio 69
# tot18 = totH = totM20 = 0

# while True:
#     idade = int(input('Idade: '))
#     sexo = ' '

#     while sexo not in 'MF':
#         sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    
#     if idade >= 18:
#         tot18 += 1
#     if sexo == 'M':
#         totH += 1
#     if sexo == 'F' and idade < 20:
#         totM20 += 1

#     resp = ' '

#     while resp not in 'SN':
#         resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
#     if resp == 'N':
#         break

# print(f'Total de pessoas com mais de 18 anos {tot18}')
# print(f'Ao todo temos {totH} homens cadastrados')
# print(f'E temos {totM20} mulheres com menos de 20 anos')

#Desafio 70
# total = totmil = menor = cont = 0
# while True:
#     produto = str(input('Nome do Produto: '))
#     preço = float(input('Preço: R$'))
#     total += preço
#     cont += 1

#     if preço > 1000:
#         totmil += 1
#     if cont == 1 or preço < menor:
#         menor = preço
#         barato = produto
#     # else:
#     #     if preço < menor:
#     #         menor = preço
#     #         barato = produto


#     resp = ' '

#     while resp not in 'SN':
#         resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
#     if resp == 'N':
#         break
# print('{:-^40}'.format(' Fim do programa '))
# print(f'O total da compra foi R${total:.2f}')
# print(f'Temos {totmil} produtos custando mais de R$1000.00')
# print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')

#Desafio 71
# print('='*30)
# print('{:^30}'.format('Banco CEV'))
# print('='*30)

# valor = int(input('Que valor você quer sacar? R$'))

# total = valor 
# cedula = 50
# totcedula = 0

# while True:
#     if total >= cedula:
#         total -= cedula
#         totcedula += 1
#     else:
#         if totcedula > 0:
#             print(f'Total de {totcedula} cedulas de R${cedula}')
#         if cedula == 50:
#             cedula = 20
#         elif cedula == 20:
#             cedula = 10
#         elif cedula == 10:
#             cedula = 5
#         elif cedula == 5:
#             cedula = 1
        
#         totcedula = 0

#         if total == 0:
#             break
# print('='*30)
# print('Volte sempre ao Banco CEV! Tenha um bom dia!')