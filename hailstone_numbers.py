'''
Hailstone Numbers. For additional information, see [Banks02].
Start with a small number, n, 1 ≤ n < 30.
There are two transformation rules that we will use:
• If n is odd, multiple by 3 and add 1 to create a new value for n.
• If n is even, divide by 2 to create a new value for n.
Perform a loop with these two transformation rules until you get to n = 1. 
You’ll note that when n = 1, you get a repeating sequence of 1, 4, 2, 1, 4, 2, ...
'''
import random
numero = new_numero = path_length = max_value = 0

print("Numero inicial : ", numero)
print("Numero  Nuevo Numero")
print("------  ------------")
for x in range(30, 1, -1):
    numero = x  
    cierto = True 
    print("*") 
    while cierto:  
        if numero%2 == 0: #Si el numero es par...
            new_numero = numero / 2.
        else:             #Si el numero es impar...
            new_numero = numero * 3. + 1
        numero -= 1 
        path_length += 1
        max_value += new_numero
        print("  {:2.0f}".format(numero).ljust(12), \
              "{:2.0f}".format(new_numero).ljust(12), \
              "{:4.0f}".format(path_length).ljust(12), \
              "{:4.0f}".format(max_value))
        cierto = False if numero == 1 else True