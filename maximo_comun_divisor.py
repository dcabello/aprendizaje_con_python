import random
numero_1 = random.randrange(1, 100)
numero_2 = random.randrange(1, 100)
print("Inicio. Numero 1 :", numero_1, "Numero 2 : ", numero_2)
numero_inicial_1 = numero_1
numero_inicial_2 = numero_2
while numero_1 != numero_2:
    if numero_1 < numero_2:
        numero_1, numero_2 = numero_2, numero_1
    else:
        numero_1 = numero_1 - numero_2
print("Maximo comun divisor de", numero_inicial_1, "y", numero_inicial_2, ":", numero_1)    