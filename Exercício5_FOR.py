import random
while True:
    n1 = random.randint(0,10)
    n2 = random.randint(0,10)
    resultado = n1 * n2
    print(f'QUANTO É {n1} VEZES {n2}?')
    resposta = int(input())
    if resultado == resposta:
        print('ACERTOU!')
    else:
        print('ERROU!')
    continuar = str(input('CONTINUAR (S/N)\n'))
    if continuar != 'S' or continuar != 's':
        break        