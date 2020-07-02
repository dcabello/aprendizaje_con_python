pi = 3.141592654

es_cierto = True
n = 0
numero_dividendo = numero_divisor = 1.0
dividendo = 1.0
divisor = 3.0
pi_cercano = 1
print("pi :", round(pi, 6))
print("pi_cercano  Dividendo   Divisor ")
print("----------  ---------   --------")
while es_cierto:
    n = n + 1    
    if divisor%2 > 0 or n != 1:
        numero_divisor *= round(divisor, 6) 
    numero_dividendo *= round(dividendo, 6)
    
    pi_cercano += numero_dividendo / numero_divisor
        
    print("{:2.6f}".format(pi_cercano).ljust(12) \
         ,"{:6.0f}".format(numero_dividendo).ljust(9) \
         ,"{:8.0f}".format(numero_divisor).ljust(12) \
         ,"{:2.6f}".format(numero_dividendo/numero_divisor))
    dividendo += 1
    divisor   += 2
    es_cierto = False if n >= 10 else True