def es_primo(x):
    cuenta_es_primo = 0
    for y in range(1, x+1):
        if x%y != 0:
            # cuenta_es_primo ejecuta la suma cuando cumple con 
            # la condicion de que el numero no es divisible sin 
            # residuo, pero ademas de la condicion anterior,
            # el numero es primo al cumplir 2 condiciones: 
            # - cuando el numero se divide sin residuo entre 1 y...
            # - cuando el numero se divide sin residuo entre si mismo
            # por eso se hace el "if cuenta_es_primo + 2 == x"
            # en el return.
            cuenta_es_primo += 1    
    return True if cuenta_es_primo + 2 == x or x == 1 else False
    
print("Numeros Primos del 1 al 100 :")
for x in range(1, 101):
    if es_primo(x):
        print("{:3.0f}".format(x))