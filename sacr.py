s = 3000    #Presion inicial del tanque (en psi)
f = 500     #Presion final del tanque (en psi)
t = 60      #Tiempo (en minutos) categoria media
d = 60      #profundidad (en pies) categoria media
c = (33 * (s - f)) / (t * (d + 33))
print("% de consumo de aire de superficie (Medio) : {}".format(c))
t = 100     #Tiempo (en minutos) categoria profunda
d = 15      #profundidad (en pies) categoria profunda
c = (33 * (s - f)) / (t * (d + 33))
print("% de consumo de aire de superficie (Profundo) : {}".format(c))
t = 30      #Tiempo (en minutos) categoria superficie
d = 60      #profundidad (en pies) categoria superficie
f = 1500    #Presion final del tanque (en psi) categoria superficie
c = (33 * (s - f)) / (t * (d + 33))
print("% de consumo de aire de superficie (superficie) : {}".format(c))
s = 2500    #Presion inicial del tanque (en psi)
f = 500     #Presion final del tanque (en psi)
d = 60      #profundidad (en pies) categoria media
c = 15.2    #consumo de aire de superficie
t = (33 * (s - f)) / c / (d + 33) 
print("Tiempo con % SACR = 15.2 : {}".format(t))