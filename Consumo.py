watts = float(input("Digite o consumo em watts por hora: "))
horas = float(input("Digite quantas horas por dia o aparelho fica ligado: "))
dias = int(input("Digite a quantidade de dias: "))

consumo = watts * horas * dias 

print("o consumo no mês será de", consumo, "watts")