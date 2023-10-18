# Desafio 90
# aluno = dict()
# aluno['nome'] = str(input('Nome: '))
# aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))

# if aluno['média'] >=7:
#     aluno['situação'] = 'Aprovado'
# elif 5 <= aluno['média'] < 7:
#     aluno['situação'] = 'Recuperação'
# else:
#     aluno['situação'] = 'Reprovado'

# print('-='*30)

# for k, v in aluno.items():
#     print(f' - {k} é igual a {v}')

# Desafio 91
# from random import randint
# from time import sleep
# from operator import itemgetter

# jogo = {'jogador1': randint(1, 6),
#         'jogador2': randint(1, 6),
#         'jogador3': randint(1, 6),
#         'jogador4': randint(1, 6)}
# ranking = dict()

# print('Valores sorteados:')

# for k, v in jogo.items():
#     print(f'{k} tirou {v} no dado.')
#     sleep(1)

# ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

# print('-='*30)
# print('  == Ranking dos Jogadores ==')

# for i, v in enumerate(ranking):
#     print(f'    {i+1} lugar: {v[0]} com {v[1]}.')
#     sleep

# Desafio 92
# from datetime import datetime

# dados = dict()
# dados['nome'] = str(input('Nome: '))
# nasc = int(input('Ano de Nascimento: '))

# dados['idade'] = datetime.now().year - nasc
# dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

# if dados['ctps'] != 0:
#     dados['contratação'] = int(input('Ano de Contratação: '))
#     dados['salário'] = float(input('Salário: R$'))
#     dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)

# print('-='*30)

# for k, v in dados.items():
#     print(f' - {k} tem o valor {v}')

# Desafio 93
# jogador = dict()
# partidas = list()
# jogador['nome'] = str(input('Nome do Jogador: '))
# tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

# for c in range(0, tot):
#     partidas.append(int(input(f'    Quantos gols na partida {c+1} ? ')))

# jogador['gols'] = partidas[:]
# jogador['total'] = sum(partidas)

# print('-='*30)
# print(jogador)
# print('-='*30)

# for k, v in jogador.items():
#     print(f'O campo {k} tem o valor {v}')

# print('-='*30)
# print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')

# for i, v in enumerate(jogador['gols']):
#     print(f'    => Na partida {i+1}, fez {v} gols.')

# print(f'Foi um total de {jogador["total"]} gols.')

# Desafio 94
# pessoa = dict()
# galera = list()
# soma = media = 0

# while True:
#     pessoa['nome'] = str(input('Nome: '))

#     while True: 
#         pessoa['sexo'] = str(input('Sexo: [S/N] ')).upper()[0]
#         if pessoa['sexo'] in 'MF':
#             break
#         print('ERRO! Por favor, digite apenas M Ou F.')

#     pessoa['idade'] = int(input('Idade: '))

#     soma += pessoa['idade']

#     galera.append(pessoa.copy())

#     while True:
#         resp = str(input('Quer continuar? S ou N. ')).upper()[0]

#         if resp in 'SN':
#             break

#         print('ERRO! Responda apenas S ou N')
    
#     if resp == 'S':
#         break

# print('-='*30)
# print(f'Ao todo temos {len(galera)} pessoas cadastradas.')

# media = soma / len(galera)

# print(f'A média de idade é de {media:5.0f} anos.')
# print('As mulheres cadastradas foram ', end='')

# for p in galera:
#     if p['sexo'] in 'Ff':
#         print(f'{p["nome"]} ', end='')
    
# print()

# for p in galera:
#     if p['idade'] >= media:
#         print('     ', end='')

#         for k, v in p.items():
#             print(f'{k} = {v}; ', end='')
#         print()

# print('<< Encerrado >>')

# Desafio 95
# jogador = dict()
# partidas = list()
# time = list()

# while True:
#     jogador.clear()
#     jogador['nome'] = str(input('Nome do Jogador: '))
#     tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
#     partidas.clear()

#     for c in range(0, tot):
#         partidas.append(int(input(f'    Quantos gols na partida {c+1} ? ')))

#     jogador['gols'] = partidas[:]
#     jogador['total'] = sum(partidas)
#     time.append(jogador.copy())

#     while True:
#         resp = str(input('Quer continuar? [S/N] ')).upper()[0]

#         if resp in 'SN':
#             break
        
#         print('ERRO! Responda apenas com S ou N.')
#     if resp == 'N':
#         break

# print('-='*30)
# print('cod ', end='')

# for i in jogador.keys():
#     print(f'{i:<15}', end='')

# print()

# print('-'*40)
# for k, v in enumerate(time):
#     print(f'{k+1:>3} ', end='')

#     for d in v.values():
#         print(f'{str(d):<15}', end='')
#     print()
# print('-'*40)

# while True:
#     busca = int(input('Mostrar dados de qual jogador? (999 para parar ) '))-1

#     if busca == 998:
#         break

#     if busca >= len(time):
#         print(f'ERRO! Não existe jogador com código {busca}!')
#     else:
#         print(f' -- Levantamento do jogador {time[busca]["nome"]}:')

#         for i, g in enumerate(time[busca]['gols']):
#             print(f'    No jogo {i+1} fez {g} gols.')
    
#     print('-'*40)
# print('<< Volte Sempre >>')