#Desafio 36
#casa = float(input('Valor da casa: R$'))
#salario = float(input('Seu salario: R$'))
#anos = int(input('Em quantos anos planeja pagar a casa? '))
#
#prestação = casa/(anos*12)
#minimo = salario*30/100
#
#print('para pagar a cada de R${:.2f} em {} anos'.format(casa,anos), end='')
#print('a prestação será de R${:.2f}'.format(prestação))
#if prestação <= minimo:
#    print('seu emprestimo pode ser concedido')
#else:
#    print('emprestimo negado')

#Desafio 37
#n = int(input('Digite um numero inteiro: '))
#
#print(''' Escolha uma das bases para conversão
#[ 1 ] converter para binario
#[ 2 ] converter para octal
#[ 3 ] converter para hexadecimal''')
#
#opçao = int(input('sua opção: '))
#
#if opçao == 1:
#    print('{} convertido para binario é igual a {}'.format(n, bin(n)[2:]))
#elif opçao == 2:
#    print('{} convertido para octal é igual a {}'.format(n, oct(n)[2:]))
#elif opçao == 3:
#    print('{} convertido para hexadecimal é igual a {}'.format(n, hex(n)[2:]))
#else:
#    print('opção inválida. tente novamente')

#Desafio 38
#n1 = int(input('Primeiro numero: '))
#n2 = int(input('Segundo numero: '))
#
#if n1 > n2:
#    print('o primeiro numero e maior')
#elif n2 > n1:
#    print('o segundo numero e maior')
#else:
#    print('os valores numericos são iguais')

#Desafio 39
#from datetime import date
#atual = date.today().year
#nasceu =  int(input('ano que nasceu? '))
#
#idade = atual - nasceu
#
#print('quem nasceu em {} tem {} anos em {}'.format(nasceu, idade, atual))
#if idade < 18:
#    saldo = 18 - idade
#    print('você tem que se alistar em {} anos'.format(saldo))
#elif idade == 18:
#    print('você deve se alistar esse ano')
#elif idade > 18:
#    saldo = idade - 18
#    print('você já deveria ter se alistado há {}'.format(saldo))
#    ano = atual - saldo
#    print('seu alistamento foi em {}'.format(ano))

#Desafio 40
#nota1 = float(input('Primeira nota: '))
#nota2 = float(input('Segundo nota: '))
#
#media = (nota1+nota2)/2
#
#print('tirando {:.1f} e {:.1f}, a media do aluno é {:.1f}'.format(nota1, nota2, media))
#if media < 5:
#    print('aluno está reprovado')
#elif 7 > media >= 5:
#    print('aluno está em recuperação')
#elif media >= 7:
#    print('aluno está aprovado')

#Desafio 41
#from datetime import date
#nasceu = int(input('Ano que nasceu: '))
#atual = date.today().year
#idade = atual - nasceu
#
#print('sua idade e {}'.format(idade))
#if idade <= 9:
#    print('mirim')
#elif idade <= 14:
#    print('infantil')
#elif idade <= 19:
#    print('junior')
#elif idade <= 25:
#    print('sênior')
#else:
#    print('master')

#Desafio 42
#reta1 = float(input('Primeira reta: '))
#reta2 = float(input('Segunda reta: '))
#reta3 = float(input('Terceira reta: '))
#
#if reta1<reta2+reta3 and reta2<reta1+reta3 and reta3<reta1+reta2:
#    print('as retas podem formar um triangulo ')
#    if reta1 == reta2 == reta3:
#        print('equilatero')
#    elif reta1 != reta2 != reta3 != reta1:
#        print('escaleno')
#    else:
#        print('isosceles')
#else:
#    print('as retas não podem formar um triangulo')

#Desafio 43
#peso = float(input('Seu peso? (kg) '))
#altura = float(input('Sua altura? (m) '))
#
#imc = peso/(altura**2)
#
#print('o imc dessa pessoa é de {:.1f}'.format(imc))
#if imc < 18.5:
#    print('você esta abaixo do peso')
#elif 18.5 <= imc < 25:
#    print('você esta peso ideal')
#elif 25 <= imc < 30:
#    print('você esta sobrepeso')
#elif 30 <= imc < 40:
#    print('você esta obesidade')
#elif imc >= 40:
#    print('você esta obesidade morbida, cuidado!')

#Desafio 44
#print('{:=^40}'.format(' Lojas guanabara '))
#
#preço = float(input('Preço das compras: R$'))
#
#print('''Formas de pagamento
#[ 1 ] á vista dinheiro/cheque
#[ 2 ] á vista no cartão
#[ 3 ] 2x no cartão
#[ 4 ] 3x ou mais no cartão''')
#
#opção = int(input('Qual é a opção? '))
#
#if opção == 1:
#    total = preço-(preço*10/100)
#elif opção == 2:
#    total = preço-(preço*5/100)
#elif opção == 3:
#    total = preço
#    parcela = total/2
#    print('sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
#elif opção == 4:
#    total = preço+(preço*20/100)
#    parcelas = int(input('Quantas parcelas? '))
#    parcela = total/parcelas
#    print('sua compra será parcelada em {}x de R${:.2f} com juros'.format(parcelas, parcela))
#else:
#    total = 0
#    print('opção inválida de pagamento. tente novamento!')
#print('sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preço, total))

#Desafio 45
#from random import randint
#from time import sleep
#itens = ('Pedra', 'Papel', 'Tesoura')
#computador = randint(0, 2)
#
#print('-=-'*10)
#print('0-Pedra\n1-Papel\n2-Tesoura')
#print('-=-'*10)
#
#jogador = int(input('escolha sua jogada: '))
#
#print('Jo')
#sleep(1)
#print('ken')
#sleep(1)
#print('po!!!')
#
#print('-='*14)
#print('Computador jogou {}'.format(itens[computador]))
#print('Jogador jogou {}'.format(itens[jogador]))
#print('-='*14)
#
#if computador ==0: #computador jogou pedra
#    if jogador == 0:
#        print('empate')
#    elif jogador == 1:
#        print('jogador venceu')
#    elif jogador == 2:
#        print('computador vence')
#    else:
#        print('jogada inválida')
#elif computador ==1: #computador jogou papel
#    if jogador == 0:
#        print('computador vence')
#    elif jogador == 1:
#        print('empate')
#    elif jogador == 2:
#        print('jogador venceu')
#    else:
#        print('jogada inválida')
#elif computador == 2: #computador jogou tesoura
#    if jogador == 0:
#        print('jogador venceu')
#    elif jogador == 1:
#        print('computador vence')
#    elif jogador == 2:
#        print('empate')
#    else:
#        print('jogada inválida')