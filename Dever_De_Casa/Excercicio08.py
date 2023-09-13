operacao = float(input("primeiro produto: "))

operacao2 = float(input("segundo produto: "))

operacao3 = float(input("Terceiro produto: "))

if operacao < operacao2 < operacao3:
    print("Primeiro produto é mais barato: {}".format(operacao))

if operacao < operacao3 < operacao2:
    print("Primeiro produto é mais barato: {}".format(operacao))

if operacao2 < operacao < operacao3:
    print("Segundo produto é mais barato: {}".format(operacao2))

if operacao2 < operacao3 < operacao:
    print("Segundo produto é mais barato: {}".format(operacao2))

if operacao3 < operacao < operacao2:
    print("Terceiro produto é mais barato: {}".format(operacao3))

if operacao3 < operacao2 < operacao:
    print("Terceiro produto é mais barato: {}".format(operacao3))