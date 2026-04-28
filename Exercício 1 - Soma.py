soma = 0

while True:
    numero = int(input("Digite um número para iniciar uma conta, e finalize a conta colocando o número 0: "))
    
    if numero == 0:
       break

    soma += numero

print(f"A SOMA DE TODOS OS NÚMEROS INSERIDOS É:{soma}")