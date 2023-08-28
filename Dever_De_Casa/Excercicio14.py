operacao = float(input("primeira nota: "))

operacao2 = float(input("segunda nota: "))

media = (operacao+operacao2)/2

if media <=4:
    print("Conceito: E")
elif media <=6:
    print("Conceito: D")
elif media <= 7.5:
    print("Conceito: C")
elif media <= 9:
    print("Conceito: B")
elif media <= 10:
    print("Conceito: A")
else:
    print("Nota fora do sistema, tente novamente")