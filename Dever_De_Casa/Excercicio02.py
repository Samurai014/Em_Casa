operacao = int(input("Seu numero e: "))

if operacao > 0:
    print("seu numero e positivo: {}".format(operacao))
elif operacao < 0:
    print("seu numero e negativo: {}".format(operacao))
else:
    print("numero neutro")