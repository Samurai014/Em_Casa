# Desafio 101
# def voto(ano):
#     from datetime import date 
#     atual = date.today().year
#     idade = atual - ano
    
#     if idade < 16:
#         return f'Com {idade} anos: NÃO VOTA.'
#     elif 16 <= idade < 18 or idade > 65:
#         return f'Com {idade} anos: VOTO OPCIONAL.'
#     else:
#         return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    
# nasc = int(input('Em que ano você nasceu? '))

# print(voto(nasc))

# Desafio 102
# def fatorial(n, show = False): 
#     f = 1
#     for c in range(n, 0, -1):
#         if show:
#             print(c, end='')
#             if c > 1:
#                 print(' x ', end='')
#             else:
#                 print(' = ', end='')
#         f *= c
#     return f

# print(fatorial(5, show = False))

# Desafio 103
# def ficha(jog= 'Desconhecido', gol = 0):
#     print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')

# n = str(input('Nome do Jogador: '))
# g = str(input('Número de Gols: '))

# if g.isnumeric():
#     g = int(g)
# else:
#     g = 0

# if n.strip() == '':
#     ficha(gol=g)
# else:
#     ficha(n,g)

# Desafio 104
