operacao = int(input("primeiro numero: "))

operacao2 = int(input("segundo numero: "))

operacao3 = int(input("terceiro numero: "))

if operacao > operacao2 >operacao3:
    print("Primeiro numero é maior: {}".format(operacao))

if operacao > operacao3 > operacao2:
    print("Primeiro numero é maior: {}".format(operacao))

if operacao2 > operacao > operacao3:
    print("Segundo numero é maior: {}".format(operacao2))

if operacao2 > operacao3 > operacao:
    print("Segundo numero é maior: {}".format(operacao2))

if operacao3 > operacao > operacao2:
    print("Terceiro numero é maior: {}".format(operacao3))

if operacao3 > operacao2 > operacao:
    print("Terceiro numero é maior: {}".format(operacao3))