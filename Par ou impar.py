Nmax = int(input("Coloque um valor máximo: "))
Nmin = int(input("Coloque um valor mínimo: "))
for i in range(Nmin, Nmax+1):
    resto = i%2
    if resto == 0:
       print(i," - Par")
    else:
       print(i," - Impar")
print("Obrigado por usar o nosso sistema")       