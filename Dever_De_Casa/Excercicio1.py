operacao = int(input("primeiro numero: "))

operacao2 = int(input("segundo numero: "))

if operacao > operacao2 :
    print("Primeiro numero é maior: {}".format(operacao))
elif operacao < operacao2:
    print("Segundo numero é maior: {}".format(operacao2))
else:
    print("Os numeros são iguas")