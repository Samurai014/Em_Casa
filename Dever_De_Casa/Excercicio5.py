operacao = int(input("Primeira nota: "))

operacao2 = int(input("Segunda nota: "))

media = ((operacao+operacao2)/2)

if media >= 10:
    print("Aprovado com Distinção")
elif media >=7:
    print("Aprovado")
else:
    print("reprovado")