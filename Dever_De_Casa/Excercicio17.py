operacao = int(input("Diga um ano: "))

if (operacao%4 == 0 and operacao%100 != 0):
    print("Ano bissexto")
else:
    print("Esse ano não e bissexto")