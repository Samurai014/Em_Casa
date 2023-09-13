dia = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
pagar = (60*dia)+(0.15*km)

print('Total a pagar será R${:.2f}'.format(pagar))