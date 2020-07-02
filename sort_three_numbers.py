import random
d1 = random.randrange(1, 13)
d2 = random.randrange(1, 13)
d3 = random.randrange(1, 13)
print("d1 : ", d1, "d2 : ", d2, "d3 : ", d3)
if (d1 <= d2 and d2 <= d3):
    print("Ok")
elif (d1 <= d2 and d2 >= d3 and d1 >= d3):
    print("Paso 1")
    d1, d2, d3 = d3, d1, d2  
elif (d1 <= d2 and d2 >= d3 and d3 >= d1):
    print("Paso 2")
    d1, d2, d3 = d1, d3, d2
elif (d1 >= d2 and d2 >= d3 and d1 >= d3):
    print("Paso 3")
    d1, d2, d3 = d3, d2, d1
elif (d1 >= d2 and d2 <= d3 and d1 <= d3):
    print("Paso 4")
    d1, d2, d3 = d2, d1, d3
elif (d1 >= d2 and d2 <= d3 and d1 >= d3):
    print("Paso 5")
    d1, d2, d3 = d2, d3, d1    
print("Nuevo orden: ")    
print("d1 : ", d1, "d2 : ", d2, "d3 : ", d3)