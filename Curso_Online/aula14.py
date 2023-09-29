#Desafio 57
# sexo = str(input('Digite seu sexo: [M/F] ')).strip().upper()[0]
# while sexo not in 'MmFf':
#     sexo = str(input('Dados inválidos. Por Favor, informe seu sexo: ')).strip().upper()[0]
# print('sexo {} registrado com sucesso'.format(sexo)) 

#Desafio 58
# from random import randint

# computador = randint(0, 10) #Faz o jogador 'pensar'

# print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
# print('Será que você consegue adivinhar qual foi? ')

# acertou = False
# palpite = 0

# while not acertou:
#     jogador = int(input('Qual é seu palpite? '))
#     palpite += 1
#     if jogador == computador:
#         acertou = True
#     else:
#         if jogador < computador:
#             print('Mais... Tente mais uma vez.')
#         elif jogador > computador:
#             print('Menos... Tente mais uma vez.')

# print('Acertou com {} tentativas. Parabéns!'.format(palpite))

#Desafio 59
# from time import sleep
# n1 = int(input('Primeiro valor: '))
# n2 = int(input('Segundo valor: '))

# opção = 0
# while opção != 5:
#     print('''[ 1 ]somar
#     [ 2 ]multiplicar
#     [ 3 ]maior
#     [ 4 ]novos números
#     [ 5 ]sair do programa''')
#     opção = int(input('>>>>> Qual é a sua opção? '))
#     if opção == 1:
#         soma = n1+n2
#         print('A soma entre {} + {} é {}'.format(n1, n2, soma))
#     elif opção == 2:
#         produto = n1*n2
#         print('O resultado de {} x {} é {}'.format(n1, n2, produto))
#     elif opção == 3:
#         if n1 > n2:
#             maior = n1
#         else:
#             maior = n2
#         print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
#     elif opção == 4:
#         print('Informe os números novamente: ')
#         n1 = int(input('Primeiro valor: '))
#         n2 = int(input('Segundo valor: '))
#     elif opção == 5:
#         print('Finalizando...')
#     else:
#         print('Opção inválida. Tente novamente.')
#     print('=-='*10)
#     sleep(2)
# print('Fim do programa! Volte sempre!')

#Desafio 60
# n = int(input('Digite um número para calcular seu fatorial: '))
# c = n
# f = 1

# print('Calculando {}! = '.format(n), end='')
# while c > 0:
#     print('{}'.format(c), end='')
#     print(' x ' if c > 1 else ' = ', end='')
#     f *= c
#     c -= 1
# print('{}'.format(f))

#Desafio 61
# print('Gerador de PA')
# print('-='*10)

# primeiro = int(input('Primeiro termo: '))
# razão = int(input('Razão da PA: '))
# termo = primeiro
# cont = 1

# while cont <= 10:
#     print('{} -> '.format(termo), end='')
#     termo += razão
#     cont += 1
# print('FIM')

#Desafio 62
# print('Gerador de PA')
# print('-='*10)

# primeiro = int(input('Primeiro termo: '))
# razão = int(input('Razão da PA: '))
# termo = primeiro
# cont = 1
# total = 0
# mais = 10
# while mais != 0:
#     total = total + mais
#     while cont <= total:
#         print('{} -> '.format(termo), end='')
#         termo += razão
#         cont += 1
#     print('PAUSA')
#     mais = int(input('Quantos termos você quer mostrar a mais? '))
# print('progressão finalizada com {} termos mostrados'.format(total))

#Desafio 63
# print('-'*30)
# print('Sequência de Fibonacci')
# print('-'*30)

# n = int(input('Quantos termos você quer mostrar? '))
# t1 = 0
# t2 = 1

# print('~'*30)
# print('{} -> {}'.format(t1, t2), end='')

# cont = 3

# while cont <= n:
#     t3 = t1 + t2
#     print('-> {}'.format(t3), end='')
#     t1 = t2
#     t2 = t3
#     cont += 1
# print('-> FIM')

#Desafio 64
# n = cont = soma =0
# n = int(input('Digite um número [999 para parar]: '))

# while n != 999:
#     soma += n
#     cont += 1
#     n = int(input('Digite um número [999 para parar]: '))
# print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))

#Desafio 65
# resp = 'S'
# soma = quant = media = maior = menor = 0

# while resp in 'Ss':
#     n = int(input('Digite um número: '))

#     soma += n
#     quant += 1

#     if quant == 1:
#         maior = menor = n
#     else:
#         if n > maior:
#             maior = n
#         if n < menor:
#             menor = n
#     resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

# media = soma/quant

# print('Você digitou {} números e a média foi {:.1f}'.format(quant, media))
# print('O maior valor foi {} e o menor foi {}'.format(maior, menor))