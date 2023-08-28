operacao = float(input("Primeiro lado: "))

operacao2 = float(input("Segundo lado: "))

operacao3 = float(input("Terceiro lado: "))

if operacao == operacao2 == operacao3:
    print("Triangulo equilatero")
elif operacao == operacao2 != operacao3:
    print("Triangulo isosceles")
elif operacao != operacao2 == operacao3:
    print("Triangulo isosceles")
elif operacao == operacao3 != operacao2:
    print("Triangulo isosceles")
elif operacao != operacao2 != operacao3:
    print("Triangulo escaleno")
else:
    print("Erro, tente novamente")