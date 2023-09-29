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
#from datetime import date
#atual = date.today().year
#
#totmaior = 0
#totmenor = 0
#
#for pess in range(1,8):
#    nasc = int(input('Em que ano a pessoa nasceu? '))
#    idade = atual - nasc
#    if idade >= 21:
#        totmaior += 1
#    else:
#        totmenor += 1
#
#print('ao todo tivemos {} pessoas maiores de idade\ne tambem tivemos {} pessoas menores de idade'.format(totmaior, totmenor))

#Desafio 55
# maior = 0
# menor = 0
# for p in range(1,6):
#     peso = float(input('Peso da {} pessoa: '.format(p)))
#     if p == 1:
#         maior = peso
#         menor = peso
#     else:
#         if peso > maior:
#             maior = peso
#         if peso < menor:
#             menor = peso
# print('o maior peso lindo foi de {}Kg\no menor peso lido foi de {}Kg'.format(maior,menor))

#Desafio 56
# somaidade = 0
# mediaidade = 0
# maioridadehomem = 0
# nomevelho = ''
# totmulher20 = 0
# for p in range(1,5):
#     print('----- {} Pessoa -----'.format(p))
#     nome = str(input('Nome: ')).strip()
#     idade = int(input('Idade: '))
#     sexo = str(input('Sexo [M/F]: ')).strip()
#     somaidade += idade
#     if p == 1 and sexo in 'Mm':
#         maioridadehomem = idade
#         nomevelho = nome
#     if sexo in 'Mm' and idade > maioridadehomem:
#         maioridadehomem = idade
#         nomevelho = nome
#     if sexo in 'Ff' and idade < 20:
#         totmulher20 += 1

# mediaidade = somaidade/4
# print('a média de idade do grupo é de {} anos'.format(mediaidade))
# print('o homem mais velho tem {} anor e se chama {}.'.format(maioridadehomem, nomevelho))
# print('ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))