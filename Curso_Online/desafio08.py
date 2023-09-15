#Desafio 16
#from math import trunc
#n1 = float(input('Digite um numero: '))
#inteiro = trunc(n1)
#
#print('o numero {} porem sua parte inteiro é {}'.format(n1, inteiro))

#Desafio 17
#from math import hypot
#co = float(input('comprimento do cateto oposto: '))
#ca = float(input('comprimento do cateto adiacente: '))
#hi = hypot(co,ca)
#
#print('a hipotenusa vai medir {:.2f}'.format(hi))

#Desafio 18
#from math import radians, sin, cos, tan
#an = float(input('Digite um ângulo que você deseja: '))
#seno = sin(radians(an))
#cosseno = cos(radians(an))
#tangente = tan(radians(an))
#
#print('o angulo de {} tem o seno de {:.2f}'.format(an, seno))
#print('o angulo de {} tem o cosseno de {:.2f}'.format(an, cosseno))
#print('o angulo de {} tem o tangente de {:.2f}'.format(an, tangente))

#Desafio 19
#from random import choice
#n1 = str(input('Primeiro aluno: '))
#n2 = str(input('Segundo aluno: '))
#n3 = str(input('Terceiro aluno: '))
#n4 = str(input('Quarto aluno: '))
#
#lista = [n1, n2, n3, n4]
#escolhido = choice(lista)
#
#print('o aluno escolhido foi {}'.format(escolhido))

#Desafio 20
#from random import shuffle
#n1 = str(input('Primeiro aluno: '))
#n2 = str(input('Segundo aluno: '))
#n3 = str(input('Terceiro aluno: '))
#n4 = str(input('Quarto aluno: '))
#
#lista = [n1, n2, n3, n4]
#ordem = shuffle(lista)
#
#print('a ordem de apresentação sera {}'.format(lista))

#Desafio 21
#import pygame
#pygame.init()
#pygame.mixer.music.load('ex21.mp3')
#pygame.mixer.music.play()
#pygame.event.wait()