def powers(numero):
    print "Las primeros 5 valores de potencia de "+str(numero)+" son : "\
          +str(numero**0)+" "\
          +str(numero**1)+" "\
          +str(numero**2)+" "\
          +str(numero**3)+" "\
          +str(numero**4)
def score_summary(nombre, numero_1, numero_2, numero_3):
    avg = (numero_1+numero_2+numero_3)/3
    print nombre+": Max "+str(max(numero_1, numero_2, numero_3))+" "+ \
          "Min "+str(min(numero_1, numero_2, numero_3))+" "+ \
          "Average "+str( avg )
def reject(nombre):
    print "Dear "+nombre
    print "I am sorry to inform you do not have the job"
    print "Yours sincerely"
    print "Humprey Hopalong"
def accept(nombre):
    print "Dear "+nombre
    print "I am pleased to inform you that you have the job"
    print "Yours sincerely"
    print "Humprey Hopalong"
    
reject("Bill")
print ""
accept("Vicki")
#score_summary("Fred", 9, 8, 7)
#powers(10)
    
