import random
numero = suma_num = average = 0
for x in range(0, 10):
    numero = random.randrange(1, 12)
    print("Numero: ", numero)
    suma_num = suma_num + numero
    count_num = x + 1
average = round(float(suma_num)/count_num, 2) if count_num != 0 else None
print("Promedio : ", average, "Numero de elementos : ", count_num, "Total de Elementos : ", suma_num)    