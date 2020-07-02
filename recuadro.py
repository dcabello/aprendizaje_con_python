import random

numero = random.randrange(1, 41)

for x in range(1, numero + 1):    
    for y in range(1, numero):
        print("*", end = "")
    print("*")    
print()        
print("numero : ", numero)