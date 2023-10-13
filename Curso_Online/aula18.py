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

# Desafio 86