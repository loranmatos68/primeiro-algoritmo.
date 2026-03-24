# Obtenção de dados
Dias = int(input("Quantidade de dias: "))
Horas = int(input("Quantidade de horas: "))
Minutos = int(input("Quantidade de Minutos: "))
Segundos = int(input("Quantidade de segundos: "))

# Convertendo em segundos
Dias = Dias * 24 * 60 * 60 # dia em segundos
Horas = Horas * 60 * 60 # hora em segundos
Minutos = Minutos * 60 # minuto em segundos

# Somando tudo
Total = Dias + Horas + Minutos + Segundos

print("Total em Segundos:", Total)