inicial = int(input("DIGITE O NÚMERO INICIAL DA LISTA: "))
final = int(input("DIGITE O MÚMERO FINAL DA LISTA: "))
divisivel = int(input("DIGITE UM DIVISÍVEL PARA A LISTA: "))
if inicial <= final:
    for i in range(inicial, final, +1):
      if i%divisivel == 0:
        print(i, end=" ")
else:
    print("LISTA INVÁLIDA!")