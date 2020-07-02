import random
ganador = True
x = total_acumulado = 0
while (ganador):
    print("Jugada N° : ", x + 1)
    d1 = random.randrange(1, 13)
    d2 = random.randrange(1, 13)
    total_jugada = d1 + d2
    if ((total_jugada == 4 or total_jugada == 6 \
    or total_jugada == 8 or total_jugada == 10) and (d1 == d2)):
        total_acumulado = total_acumulado + total_jugada
        print("Ganador!!! ", total_jugada, "("+str(d1)+"+"+str(d2)+") ")
        ganador = False
    else:
        print("Mejor suerte para la próxima. : ", total_jugada, "("+str(d1)+"+"+str(d2)+")")  
    x = x + 1
print("Total Acumulado : ", total_acumulado)