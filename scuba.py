profundidad = 60                    # medida en pies
presion_inicial_tanque = 3000       # medida en PSI
presion_final_tanque = 500          # medida en PSI
tiempo = 30                         # medido en Minutos
consumo_de_aire = 33*(presion_inicial_tanque - presion_final_tanque) / tiempo * (profundidad + 33)
print "Consumo de Aire: "+str(consumo_de_aire)+" Libras"
precio, comision = 23, 3
print precio, comision, precio*comision
