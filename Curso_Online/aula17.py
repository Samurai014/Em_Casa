# Desafio 78
# listaN = []
# mai = 0
# men = 0

# for c in range(0,5):
#     listaN.append(int(input(f'Digite um valor para a Posição {c}: ')))
#     if c == 0:
#         mai = men = listaN[c]
#     else:
#         if listaN[c] > mai:
#             mai = listaN[c]
#         if listaN[c] < men:
#             men = listaN[c]

# print('=-'*30)
# print(f'Você digitou os valores {listaN}')
# print(f'O maior valor digitado foi {mai} nas posições ', end='')

# for i, v in enumerate(listaN):
#     if v == mai:
#         print(f'{i}... ', end='')

# print()
# print(f'O menor valor digitado foi {men} nas posições ', end='')

# for i, v in enumerate(listaN):
#     if v == men:
#         print(f'{i}... ', end='')

# print()

# Desafio 79
# n = list()

# while True:
#     n1 = int(input('Digite um valor: '))
    
#     if n1 not in n:
#         n.append(n1)
#         print('Valor adicionado com sucesso...')
#     else:
#         print('Valor duplicado! Não vou adicionar...')
    
#     r = str(input('Quer continuar? [S/N] '))

#     if r in 'Nn':
#         break

# print('-='*30)

# n.sort()

# print(f'Você digitou os valores {n}')

# Desafio 80
# lista = []
# for c in range(0, 5):
#     n = int(input('Digite um valor: '))
#     if c == 0 or n > lista[-1]:
#         lista.append(n)
#         print('Adicionado ao final da lista...')
#     else:
#         pos = 0
#         while pos < len(lista):
#             if n <= lista[pos]:
#                 lista.insert(pos,n)
#                 print(f'Adicionado na posição {pos} da lista...')
#                 break
#             pos += 1

# print('-='*30)
# print(f'Os valores digitados em ordem foram {lista}')

# Desafio 81
# valores = []

# while True:
#     valores.append(int(input('Digite um valor: ')))
#     resp = str(input('Quer continuar? [S/N] '))
#     if resp in 'Nn':
#         break

# print('-='*30)
# print(f'Você digitou {len(valores)} elementos.')

# valores.sort()

# print(f'Os valores em ordem decrescente são {valores}')

# if 5 in valores:
#     print('O valor 5 faz parte da lista!')
# else:
#     print('O valor 5 não foi encontrado na lista!')

# Desafio 82