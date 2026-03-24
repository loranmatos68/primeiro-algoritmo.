salario = float(input("Digite o valor do salário: "))
reajuste = float(input("Digite o percentual de reajuste(%): "))

# Calcular o reajuste
reajuste = reajuste/100
vlr_reajuste = salario * reajuste

# somar o reajuste ao salario
nvSalario = salario = vlr_reajuste

# Imprimir tudo
print("Novo Salario: ",nvSalario)