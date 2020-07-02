import random
def raiz_cuadrada(n):
    g1 = 0
    g2 = n
    while ((g1 * g1 - n) / n < -0.002):
        punto_medio = (g1 + g2) / 2
        punto_comp = (punto_medio * punto_medio) - n
        if punto_comp <= 0:
            resultado = g1 = punto_medio
        elif punto_comp >= 0:
            resultado = g2 = punto_medio
        elif punto_comp == 0:
            resultado = punto_medio
    return resultado

def gcd(num1, num2):
    # Determine the smaller of num1 and num2
    min = num1 if num1 < num2 else num2
    # 1 is definitely a common factor to all ints
    largestFactor = 1
    for i in range(1, min + 1):
        if num1 % i == 0 and num2 % i == 0:
            largestFactor = i # Found larger factor
    return largestFactor    

n  = random.randrange(1, 301) #numero al que se le aplica la raiz cuadrada.
n1 = random.randrange(1, 301) 
n2 = random.randrange(1, 301) 
resultado = 0
print("Raiz cuadrada de ", n, ":", round(raiz_cuadrada(n), 2))
print("Maximo Comun Divisor de ", n1, "y", n2, gcd(n1, n2))