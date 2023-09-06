def maior(a,b,c,d,e):
    maior = a

    if b > maior:
        maior = b
    if c > maior:
        maior = c
    if d > maior:
        maior = d
    if e > maior:
        maior = e

    return maior

def menor(a,b,c,d,e):
    menor= a

    if b < menor:
        menor = b
    if c < menor:
        menor = c
    if d < menor:
        menor = d
    if e < menor:
        menor = e

    return menor

def operacao():
    a = int(input("Primeiro numero: "))
    b = int(input("Segundo numero : "))
    c = int(input("Terceiro numero: "))
    d = int(input("Quarto numero: "))
    e = int(input("Quinto numero: "))

    print("Maior: ", maior(a,b,c,d,e))
    print("Menor: ", menor(a,b,c,d,e))
    print()
    
while True:
    operacao()