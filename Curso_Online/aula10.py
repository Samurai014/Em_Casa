#Desafio 28
#from random import randint
#from time import sleep
#computador = randint(0,5) #Faz o jogador 'pensar'
#
#print('-=-'*20)
#print('vou pensar em um numero entre 0 e 5. tente adivinhar...')
#print('-=-'*20)
#
#jogador = int(input('Em que numero eu pensei? ')) #jogador tenta adivinhar
#
#print('processando...')
#sleep(3)
#
#if jogador == computador:
#    print('parabéns você venceu!')
#else:
#    print('eu venci você! pensei no {} e não no {}'.format(computador,jogador))

#Desafio 29
#km = int(input('Quantos km o carro tava por hora? '))
#custo = (km-80)*7
#
#if km >= 81:
#    print('você deverar pagar uma multa de R${:.2f}'.format(custo))
#else:
#    print('você não foi multado.')

#Desafio 30
#n1 = int(input('Digite um numero: '))
#resultado = n1 % 2
#
#if resultado == 0:
#    print('o numero {} e par'.format(n1))
#else:
#    print('o numero {} e impar'.format(n1))

#Desafio 31
#viagem = int(input('Quanto km e a sua viagem? '))
#curta = viagem*0.50
#longa = viagem*0.45
#
#if viagem <= 200:
#    print('sua viagem ficou R${:.2f}'.format(curta))
#else:
#    print('sua viagem ficou R${:.2f}'.format(longa))

#Desafio 33
#a = int(input('Digite um numero: '))
#b = int(input('Digite outro numero: '))
#c = int(input('Digite mais um numero: '))
#menor = a
#maior = a
#
##verifica o menor
#if b<a and b<c:
#    menor = b
#if c<a and c<b:
#    menor = c
#
##verifica o maior
#if b>a and b>c:
#    maior = b
#if c>a and c>b:
#    maior = c
#
#print('O maior numero e {}'.format(maior))
#print('o menor numero e {}'.format(menor))

#Desafio 34
#salario = float(input('Quanto e o seu salario? '))
#
#if 1250 >= salario:
#    print('seu novo salario será R${:.2f}'.format(salario+salario*15/100))
#else:
#    print('seu novo salario será R${:.2f}'.format(salario+salario*10/100))

#Desafio 35
#n1 = int(input('Fale a primeira reta: '))
#n2 = int(input('Fale a segunda reta: '))
#n3 = int(input('Fale a terceira reta: '))
#
#if n1 < n2+n3 and n2 < n1+n3 and n3 < n1+n2:
#    print('as retas formam um triangulo')
#else:
#    print('as retas não formam um triangulo')