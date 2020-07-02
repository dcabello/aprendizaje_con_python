'''El objetivo de este programa es
generar 6 valores aleatorios que 
no se repitan, esto servirá como
base para generar direcciones IP
que no se repitan, y utilizarlo
en el programa para envío por 
e-mail de la carta del esquema 
de US$6. '''

import random, time
t_inicio = time.time()
i = 7
for x in range(1, 11):     
    if x == 1: 
        v1 = random.randrange(i)
        v2 = random.randrange(i)
        v3 = random.randrange(i)
        v4 = random.randrange(i)
        v5 = random.randrange(i)
        v6 = 0    
        print("{} {} {} {} {} {} (ciclo {})".format(v1, v2, v3, v4, v5, v6, x))
        
    else:
        print("{} {} {} {} {} {} (ciclo {} antes swap)".format(v1, v2, v3, v4, v5, v6, x))
        v1, v2, v3, v4, v5 = v2, v3, v4, v5, v6 
        v6 = random.randrange(i)        
        print("{} {} {} {} {} {} (ciclo {} luego swap)".format(v1, v2, v3, v4, v5, v6, x))
            
    while (v1 == v2):
        print("Entro al ciclo While (v2) ")
        v2 = random.randrange(i)
        print("{} {} {} {} {} {} ".format(v1, v2, v3, v4, v5, v6))    
    
    while (v1 == v3 or v2 == v3):
        print("Entro al ciclo While (v3)")
        v3 = random.randrange(i)
        print("{} {} {} {} {} {} ".format(v1, v2, v3, v4, v5, v6))
        
    while (v1 == v4 or v2 == v4 or v3 == v4):
        print("Entro al ciclo While (v4)")
        v4 = random.randrange(i)
        print("{} {} {} {} {} {} ".format(v1, v2, v3, v4, v5, v6))    
        
    while (v1 == v5 or v2 == v5 
        or v3 == v5 or v4 == v5):
        print("Entro al ciclo While (v5)")
        v5 = random.randrange(i)
        print("{} {} {} {} {} {} ".format(v1, v2, v3, v4, v5, v6))

    while (v1 == v6 or v2 == v6 
        or v3 == v6 or v4 == v6 or v5 == v6):
        print("Entro al ciclo While (v6)")
        v6 = random.randrange(i)
        print("{} {} {} {} {} {} ".format(v1, v2, v3, v4, v5, v6))   
        
    print("{} {} {} {} {} {} Fuera del ciclo****".format(v1, v2, v3, v4, v5, v6))
t_final = time.time()
print("Tiempo total : ", t_final - t_inicio)
    