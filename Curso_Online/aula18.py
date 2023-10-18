# Desafio 84
# temp = []
# princ = []
# mai = men = 0

# while True:
#     temp.append(str(input('Nome: ')))
#     temp.append(float(input('Peso: ')))
    
#     if len(princ) == 0:
#         mai = men = temp[1]
#     else:
#         if temp [1] > mai:
#             mai = temp[1]
#         if temp [1] < men:
#             men = temp[1]

#     princ.append(temp[:])
#     temp.clear()

#     resp = str(input('Quer continuar? [S/N] '))

#     if resp in 'Nn':
#         break

# print('-='*30)
# print(f'Ao todo, Você cadastrou {len(princ)} pessoas.')
# print(f'O maior peso foi de {mai}Kg. Peso de ', end='')

# for p in princ:
#     if p[1] == mai:
#         print(f'[{p[0]}] ', end='')

# print()
# print(f'O menor peso foi de {men}Kg. Peso de ', end='')

# for p in princ:
#     if p[1] == men:
#         print(f'[{p[0]}] ', end='')

# print()

# Desafio 85
# n = [], []
# valor = 0

# for c in range(1,8):
#     valor = int(input(f'Digite o {c}o. Valor: '))

#     if valor % 2 == 0:
#         n[0].append(valor)
#     else:
#         n[1].append(valor)

# print('-='*30)

# n[0].sort()
# n[1].sort()

# print(f'Os valores pares digitados foram: {n[0]}')
# print(f'Os valores ímpares digitados foram: {n[1]}')

# # Desafio 86
# matriz = [0,0,0], [0,0,0], [0,0,0]

# for l in range(0,3):
#     for c in range(0,3):
#         matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

# print('-='*30)

# for l in range(0,3):
#     for c in range(0,3):
#         print(f'{matriz[l][c]:^5}', end='')
#     print()

# Desafio 87
# matriz = [0,0,0], [0,0,0], [0,0,0]
# spar = mai = scol = 0

# for l in range(0,3):
#     for c in range(0,3):
#         matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

# print('-='*30)

# for l in range(0,3):
#     for c in range(0,3):
#         print(f'{matriz[l][c]:^5}', end='')
#         if matriz[l][c] % 2 == 0:
#             spar += matriz[l][c]
#     print()

# print('-='*30)
# print(f'A soma dos valores pares é {spar}.')

# for l in range(0,3):
#     scol += matriz[l][2]

# print(f'A soma dos valores da terceira coluna é {scol}.')

# for c in range(0,3):
#     if c == 0:
#         mai = matriz[l][c]
#     elif matriz[1][c] > mai:
#         mai = matriz[1][c]

# print(f'O maior valor da segunda linha é {mai}') 

# Desafio 88
# from random import randint
# from time import sleep

# lista = list()
# jogos = list()

# print('-'*30)
# print('     JOGA NA MEGA SENA     ')
# print('-'*30)

# quant = int(input('Quantos jogos você quer que eu sorteie? '))

# tot = 1

# while tot <= quant:
#     cont = 0
#     while True:
#         num = randint(1,60)
#         if num not in lista:
#             lista.append(num)
#             cont += 1
#         if cont >= 6:
#             break
#     lista.sort()
#     jogos.append(lista[:])
#     lista.clear()
#     tot += 1

# print('-='*3, f'Sorteando {quant} Jogos ', '-='*3)

# for i, l in enumerate(jogos):
#     print(f'Jogo {i+1}: {l}')
#     sleep(1)

# print('-='*5, '< Boa Sorte >', '-='*5)

# Desafio 89
# ficha = list()

# while True:
#     nome = str(input('Nome: '))
#     nota1 = int(input('Nota 1: '))
#     nota2 = int(input('Nota 2: '))
#     media = (nota1+nota2)/2
#     ficha.append([nome, [nota1, nota2], media])
#     resp = str(input('Quer continuar? [S/N] '))

#     if resp in 'Nn':
#         break
# print('-='*30)
# print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
# print('-='*26)

# for i, a in enumerate(ficha):
#     print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
    
# while True:
#     print('-'*35)
#     opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))

#     if opc == 999:
#         print('Finalizando...')
#         break
#     if opc <= len(ficha) -1:
#         print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
# print('<<< Volte Sempre >>>')