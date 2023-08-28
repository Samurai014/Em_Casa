operacao = float(input("Seu salário no mês ?"))

if operacao <= 280:
    print("Salário antes do reajuste: ", operacao)
    print("Porcentagem do aumento é 20%")
    print("Valor do aumento: ", operacao*20/100)
    print("Seu novo salário sera: ", operacao+operacao*20/100)
elif operacao <= 700 :
    print("Salário antes do reajuste: ", operacao)
    print("Porcentagem do aumento é 15%")
    print("Valor do aumento: ", operacao*15/100)
    print("Seu novo salário sera: ", operacao+operacao*15/100)
elif operacao <= 1500:
    print("Salário antes do reajuste: ", operacao)
    print("Porcentagem do aumento é 10%")
    print("Valor do aumento: ", operacao*10/100)
    print("Seu novo salário sera: ", operacao+operacao*10/100)
elif operacao > 1500:
    print("Salário antes do reajuste: ", operacao)
    print("Porcentagem do aumento é 5%")
    print("Valor do aumento: ", operacao*5/100)
    print("Seu novo salário sera: ", operacao+operacao*5/100)