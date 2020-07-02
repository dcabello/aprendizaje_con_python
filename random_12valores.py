'''El objetivo de este programa es
generar 12 valores aleatorios que 
no se repitan, esto servirá como
base para generar direcciones IP
que no se repitan, y utilizarlo
en el programa para envío por 
e-mail de la carta del esquema 
de US$6. '''
import random, time
t_inicio = time.time()
i = 251
nlista = 0
lista = []
for x in range(1, 35):
    v1 = random.randrange(2, i)
    if v1 in lista:
        pass
    else:
        if nlista < 12: #Solo se aceptan 12 elementos en la lista        
            lista.append(v1)
            nlista = nlista + 1        
        else:
            lista.pop(0)
            lista.append(v1)
        print(lista)
t_final = time.time()
print("Tiempo total : ", t_final - t_inicio)