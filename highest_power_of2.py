'''Corregir este programa-.'''
n = 100
p = 1
limite_inferior = 2 
limite_superior = 2
potencia_1 = 0
potencia_2 = 1

ciclo = True
while ciclo: 
    if (limite_inferior <= n < limite_superior): 
        ciclo = False
    else:        
        limite_inferior = limite_inferior << potencia_1
        limite_superior = limite_superior << potencia_2
        potencia_1 = potencia_1 + 1
        potencia_2 = potencia_2 + 1
    print("limite_inferior :", limite_inferior, \
          "limite_superior :", limite_superior, \
          "potencia_1 :", potencia_1, \
          "potencia_2 :", potencia_2)
print("Resultado ", limite_inferior, "<=", n, "<", limite_superior)