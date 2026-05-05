somadepares = 0
somadeimpares = 0

for i in range(1, 101, 1):
    if i%2 == 0:
        somadepares = somadeimpares + i
    else:
        somadeimpares = somadepares + i
print("Soma dos pares entre 1 a 100: ", somadepares)
print("Soma dos impares entre 1 a 100: ", somadeimpares)