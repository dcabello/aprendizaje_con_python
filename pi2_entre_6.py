pi2_entre_6 = 3.141592654**2 / 6

es_cierto = True
numero = 0
divisor = 1
print("pi2_entre_6 :", round(pi2_entre_6, 6))
print("Numero  divisor")
print("------  -------")
while es_cierto:
    numero += round(1 / divisor**2, 5) # debe ser progresion (1 / (2)2), (1 / (3)2), (1 / (4)2)...
    print("{:6.5f}".format(numero).ljust(12) \
          ,"{:2.0f}".format(divisor).ljust(8))
    divisor += 1      
    es_cierto = False if divisor >= 101 else True