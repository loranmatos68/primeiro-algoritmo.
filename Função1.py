# Funções
def imprimeNome(nome):
    print("Nome:", nome)
    
def soma(valor1, valor2):
    res = valor1 + valor2
    #print("Resultado:", res)
    return res 
    
# Programa Principal
nome = input("Digite um nome: ")
imprimeNome(nome)    
soma(10,5)
result = soma(20,30)
print (result)