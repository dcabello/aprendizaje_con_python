import random
ganador = True
x = total_acumulado = 0
while (ganador):
    print("Jugada N° : ", x + 1)
    d1 = random.randrange(1, 13)
    d2 = random.randrange(1, 13)
    total_jugada = d1 + d2
    if ((total_jugada == 2 or total_jugada == 12) and (total_jugada%2 > 0)) \
    or (total_jugada == 3 or total_jugada == 4 or total_jugada == 9 \
    or total_jugada == 10 or total_jugada == 11 and (total_jugada%2 == 0)):
        total_acumulado = total_acumulado + total_jugada
        print("Ganador!!! ", total_jugada, "("+str(d1)+"+"+str(d2)+") "+str(total_jugada%2) )        
    else:
        print("Mejor suerte para la próxima. : ", total_jugada, "("+str(d1)+"+"+str(d2)+") "+str(total_jugada%2) )  
        ganador = False
    x = x + 1
print("Total Acumulado : ", total_acumulado)