# Desafio 72
# cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 
#         'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 
#         'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 
#         'dezessete', 'dezoito', 'dezenove', 'vinte')

# while True:
#     n = int(input('Digite um número entre 0 a 20: '))
#     if 0 <= n <=20:
#         break
#     print('Tente novamente. ', end='')
# print(f'Você digitou o número {cont[n]}')

# Desafio 73
# times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 
#          'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 
#          'Atlético', 'BotaFogo', 'Atlético-PR', 'Bahia', 
#          'São Paulo', 'Fluminense', 'Sport Recife', 
#          'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 
#          'Atlético-GO')

# print('-='*15)
# print(f'Lista de times do Brazileirão: {times}')
# print('-='*15)
# print(f'Os 5 primeiros são {times[0:5]}')
# print('-='*15)
# print(f'Os 4 últimos são {times[-4:]}')
# print('-='*15)
# print(f'Times em ordem alfabética: {sorted(times)}')
# print('-='*15)
# print(f'O chapecoense está na {times.index("Chapecoense")+1}ª posição')

# Desafio 74
# from random import randint

# n = (randint(1, 10), randint(1, 10), randint(1, 10), 
#      randint(1, 10), randint(1, 10))

# print(f'Os valores sorteados foram: ', end='')

# for n1 in n:
#     print(f'{n1} ', end='')
# print(f'\nO maior valor sorteado foi {max(n)}')
# print(f'O menor valor sorteado foi {min(n)}')

# Desafio 75
# n = (int(input('Digite um número: ')), 
#      int(input('Digite outro número: ')), 
#      int(input('Digite mais um número: ')), 
#      int(input('Digite o último número: ')))

# print(f'Você digitou os valores {n}')
# print(f'O valor 9 apareceu {n.count(9)} vezes')

# if 3 in n:
#     print(f'O valor 3 apareceu na {n.index(3)+1}ª posição')
# else:
#     print('O valor 3 não foi digitado em nenhuma posição')

# print('Os valores pares digitados foram ', end='')
# for n1 in n:
#     if n1 % 2 == 0:
#         print(n1, end=' ')

# Desafio 76
# listagem = ('Lápis', 1.75, 
#             'Borracha', 2, 
#             'Caderno', 15.90, 
#             'Estojo', 25, 
#             'Transferidor', 4.20, 
#             'Compasso', 9.90, 
#             'Mochila', 120.32, 
#             'Canetas', 22.30, 
#             'Livro', 34.90)

# print('-'*40)
# print(f'{"Lista de Preços":^40}')
# print('-'*40)

# for pos in range(0, len(listagem)):
#     if pos % 2 == 0:
#         print(f'{listagem[pos]:.<30}', end='')
#     else:
#         print(f'R${listagem[pos]:>7.2f}')

# Desafio 77
# palavras = ('aprender', 'programar', 'linguagem', 'python', 
#             'curso', 'gratis', 'estudar', 'praticar', 
#             'trabalhar', 'mercado', 'programador', 'futuro')

# for p in palavras:
#     print(f'\nNa palavra {p.upper()} temos ', end='')
#     for letra in p:
#         if letra.lower() in 'aeiou':
#             print(letra, end=' ')