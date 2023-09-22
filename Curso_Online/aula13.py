#Desafio 46
#from time import sleep
#import emoji
#for c in range(10, 0, -1):
#    print(c)
#    sleep(1)
#print('lançar!!!🎇🎇🎇🎇🎇🎇')

#Desafio 47
#for c in range(0, 51, 2):
#    print(c, end=' ')
#print('acabou')

#Desafio 48
#soma = 0
#cont = 0
#for c in range(1, 501, 2):
#    if c % 3 == 0:
#        cont += 1
#        soma += c
#print('a soma de todos os {} valores solicitados é {}'.format(cont, soma))

#Desafio 49
#tabuada = int(input('Qual tabuada deseja? '))
#
#for c in range(1, 11):
#    multi = tabuada*c
#    print('{}x{} = {}'.format(tabuada,c,multi))

#Desafio 50
#soma = 0
#cont = 0
#for c in range(1,7):
#    n = int(input('digite algum numero inteiro: '))
#    if n % 2 == 0:
#        soma += n
#        cont += 1
#print('você informou {} numeros pares e a soma foi {}'.format(cont, soma))

#Desafio 51
#primeiro = int(input('Primeiro termo: '))
#razão = int(input('Razão: '))
#decimo = primeiro+(10 - 1)*razão
#
#for c in range(primeiro, decimo+razão, razão):
#    print('{}'.format(c), end='-> ')
#print('acabou!')

#Desafio 52
#n = int(input('Digite um numero: '))
#total = 0
#for c in range(1, n+1):
#    if n % c ==0:
#        print('\033[33m', end=' ')
#        total += 1
#    else:
#        print('\033[31m', end=' ')
#    print('{}'.format(c), end=' ')
#print('\n\033[mo numero {} foi divísivel {} vezes'.format(n, total))
#if total == 2:
#    print('é por isso ele e primo!')
#else:
#    print('e por isso que ele não e primo!')

#Desafio 53
#frase = str(input('Digite uma frase: ')).strip().upper()
#palavras = frase.split()
#junto = ''.join(palavras)
#inverso = ''
#
## poderia ser tambem com fatiamento (inverso = junto[::-1])
#
#for letra in range(len(junto)-1,-1,-1):
#    inverso += junto[letra]
#
#print('o inverto de {} é {}'.format(junto, inverso))
#
#if inverso == junto:
#    print('temos um palíndromo!')
#else:
#    print('a frase digitada não e um palíndromo!')

#Desafio 54

#Desafio 55

#Desafio 56