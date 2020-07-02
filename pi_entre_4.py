pi_entre_4 = 3.141592654 / 4

es_cierto = True
n = 0
numero = 1
divisor = 3
print("pi_entre_4 :", round(pi_entre_4, 6))
while es_cierto:
    n = n + 1    
    if n%2 > 0 or n == 1:   # es impar, la formula es negativa
        numero += - round((1 / (divisor)), 6) # debe ser progresion (1 / (3)), (1 / (5)), (1 / (7))...
    else:                   # es par, la formula es positiva
        numero += + round((1 / (divisor)), 6) # debe ser progresion (1 / (3)), (1 / (5)), (1 / (7))...    
    print("numero :{:6.5f}".format(numero).ljust(10) \
          ,"n : {:2.0f}".format(n).ljust(6) \
          ,"divisor : {:2.0f}".format(divisor))
    divisor += 2      
    es_cierto = False if n >= 100 else True