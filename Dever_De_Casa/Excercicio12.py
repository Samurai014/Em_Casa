operacao = int(input("Quanto você receber por hora? "))

operacao2 = int(input("Quantas horas você trabalhou nesse mês? "))

salario_bruto = operacao*operacao2
inss = salario_bruto*10/100
imposto1 = salario_bruto*0/100
imposto2 = salario_bruto*5/100
imposto3 = salario_bruto*10/100
imposto4 = salario_bruto*20/100
fgts = salario_bruto*11/100

if salario_bruto <= 900:
    print("Imposto de Renda: ", imposto1)
    print("INSS: ", inss)
    print("FGTS: ", fgts)
    print("Total dos descontos: ", imposto1+inss)
    print("Salario liquido: ", salario_bruto-imposto1-inss)
elif salario_bruto <= 1500:
    print("Imposto de Renda: ", imposto2)
    print("INSS: ", inss)
    print("FGTS: ", fgts)
    print("Total dos descontos: ", imposto2+inss)
    print("Salario liquido: ", salario_bruto-imposto2-inss)
elif salario_bruto <= 2500:
    print("Imposto de Renda: ", imposto3)
    print("INSS: ", inss)
    print("FGTS: ", fgts)
    print("Total dos descontos: ", imposto3+inss)
    print("Salario liquido: ", salario_bruto-imposto3-inss)
elif salario_bruto > 2500:
    print("Imposto de Renda: ", imposto4)
    print("INSS: ", inss)
    print("FGTS: ", fgts)
    print("Total dos descontos: ", imposto4+inss)
    print("Salario liquido: ", salario_bruto-imposto4-inss)