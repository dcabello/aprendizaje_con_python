def al_cuadrado(valor = 1):
    return valor * valor
def al_cubo(valor = 1):
    return valor * valor * valor
def numero_x_valor(valor = 1., valor2 = 1.):
    return valor * valor2
def fahrenheit_to_celsius(value):        
    return ( (5./9.) * (value * 32) )    

print "Numero".ljust(15),
print "Al Cuadrado".ljust(15),
print "Al Cubo".ljust(15),
#print "Numero x 23".ljust(15),
print "F to C"
for x in range(1,10):
    print str(x).ljust(15),
    print str(al_cuadrado(x)).ljust(15),
    print str(al_cubo(x)).ljust(15),
    #print numero_x_valor(x, 23).ljust(15),
    print ("%f" % round(fahrenheit_to_celsius(x),4))
    #print("variable2 = %s, variable4 = %d" % (variable2, variable4))
