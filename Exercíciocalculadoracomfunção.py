def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
       return "ERRO: DIVISÃO POR ZERO"
    return a / b

def exibirmenu():
    print("--- CALCULADORA DE PYTHON ---")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Sair")
    return input("ESCOLHA UMA OPÇÃO: ")

def calculadora():
    while True:
        opcao = exibirmenu()
        
        if opcao == '5':
            print("Saindo...")
            break
        if opcao in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                
                if opcao == '1':
                    print(f"Resultado: {somar(num1, num2)}")
                elif opcao == '2':
                    print(f"Resultado: {subtrair(num1, num2)}")
                elif opcao == '3':
                    print(f"Resultado: {multiplicar(num1, num2)}")
                elif opcao == '4':
                    print(f"Resultado: {dividir(num1, num2)}")
            except ValueError:
                print("ERRO: POR FAVOR, DIGITE NÚMEROS VÁLIDOS.")
        else:
            print("OPÇÃO INVÁLIDA! TENTE NOVAMENTE.")
            
# Iniciar o programa
calculadora()                               