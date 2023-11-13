# Desafio 96
# def area(larg, comp):
#     a = larg * comp
#     print(f'A área de um terreno {larg}x{comp} é de {a}m².')

# print(' Controle de Terrenos')
# print('-'*20)

# l = float(input('Largura (m): '))
# c = float(input('Comprimento (m): '))
# area(l,c)

# Desafio 97
# def escreva(msg):
#     tam = len(msg)+4

#     print('~'*tam)
#     print(f'  {msg}')
#     print('~'*tam)

# escreva('Matheus de Jesus Marques')
# escreva('Estudando Python')
# escreva('To ficando picaxxs')

# Desafio 98
# from time import sleep
# def contador(i, f, p):
#     if p < 0:
#         p *= -1
#     if p == 0:
#         p = 1

#     print('-='*20)
#     print(f'Contagem de {i} até {f} em {p} em {p}')
#     sleep(1.5)

#     if i < f:
#         cont = i
#         while cont <= f:
#             print(f'{cont} ', end='', flush=True)
#             sleep(0.5)
#             cont += p
#         print('FIM')
#     else:
#         cont = i
#         while cont >= f:
#             print(f'{cont} ', end='', flush=True)
#             sleep(0.5)
#             cont -= p
#         print('FIM')

# contador(1, 10, 1)
# contador(10, 0, 2)
# print('-='*20)
# print('Agora e sua vez de personalizar a contagem!')

# ini = int(input('Inicio: '))
# fim = int(input('Fim: '))
# passo = int(input('Passo: '))

# contador(ini, fim, passo)

# Desafio 99
# from time import sleep

# def maior(* num):
#     cont = maior = 0
#     print('-='*30)
#     print('Analisando os valores passados... ')

#     for valor in num:
#         print(f'{valor} ', end='', flush=True)
    
#         sleep(0.5)

#         if cont == 0:
#             maior = valor
#         else:
#             if valor > maior:
#                 maior = valor
    
#         cont += 1
#     print(f'Foram informados {cont} valores ao todo.')
#     print(f'O maior valor informado foi {maior}')

# maior(2, 9, 4, 5, 7, 1)
# maior(4, 7, 0)
# maior(1, 2)
# maior(6)
# maior()

# Desafio 100
# from random import randint
# from time import sleep

# def sorteia(lista):
#     print('Sorteando 5 valores de lista: ', end='')

#     for cont in range(0,5):
#         n = randint(1, 10)
#         lista.append(n)
#         print(f'{n} ', end='', flush=True)
#         sleep(0.5)
#     print('PRONTO!')
# def somaPar(lista):
#     soma = 0
#     for valor in lista:
#         if valor % 2 == 0:
#             soma += valor
#     print(f'Somando o valores pares de {lista}, temos {soma}')

# numeros = list()
# sorteia(numeros)
# somaPar(numeros)