pi = 3.141592654

es_cierto   = True
numero      = 0
dividendo   = 1
divisor     = 3
print("pi :", round(pi, 6))
print("Progresion PI  dividendo  divisor")
print("-------------  ---------  -------")
while es_cierto:    
    numero += round(dividendo / divisor, 5)
    print("   {:6.5f}".format(numero).ljust(18) \
         ,"{:2.0f}".format(dividendo).ljust(9) \
         ,"{:2.0f}".format(divisor))
    
    valor_puente = dividendo
    dividendo += 1
    dividendo *= valor_puente
    
    valor_puente = divisor
    divisor   += 2
    divisor   *= valor_puente
    
    es_cierto = False if dividendo >= 2551 else True