preco_litro = float(input("Preço do litro do combustível (R$): "))
desempenho = float(input("Desempenho do veículo (km/l): "))
distancia = float(input("Distância da viagem (km): "))

litros_gastos = distancia / desempenho
custo_total = litros_gastos * preco_litro

print(f"\nResultados:")
print(f"Combustível gasto: {litros_gastos:.2f} litros")
print(f"Custo total da viagem: R$ {custo_total:.2f}")