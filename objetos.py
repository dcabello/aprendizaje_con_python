"""Programa Ejemplo de Objetos - Clases y Metodos"""
class FirstClass: 
    def setdata (self, value):
        self.data = value    
    def display(self):
        print self.data
class SecondClass(FirstClass):
    def display(self):
        print "Current Value = '%s'" % self.data    
class Trabajador:
    def __init__(self, name = ""):
        self.name = name        
    def setName(self, value):
        self.name = value        
    def getName(self):
        print self.name        
class Empleado(Trabajador):  
    def setSueldo(self, value):
        self.sueldo = value        
    def getSueldo(self):
        print "Sueldo : %s" % self.sueldo
try:
    print "Ejemplo De Trabajador, clase Original con 'Nombre' como atributo unico "
    emp1 = Trabajador()
    emp1.setName("Daniel Cabello")
    emp1.getName()

    emp4 = Trabajador("Benito Calo")
    emp4.getName()
    if issubclass(Empleado, Trabajador): 
        es_subclase = "Si"
    else:
        es_subclase = "No"
    print "Ejemplo De Empleado, clase derivada de Trabajador con nuevo atributo Sueldo"
    print "La clase Empleado es subclase de Trabajador : %s" % es_subclase
    print ""
    emp2 = Empleado()
    emp2.setName("Pedro Perez")
    emp2.getName()
    emp2.setSueldo(2500)
    emp2.getSueldo()
    emp5 = Empleado("Benito Bodoque")
    emp5.setSueldo(1200)
    emp5.getName()
    emp5.getSueldo()
        
    # print ""
    # print ""
    # x = FirstClass()
    # y = SecondClass()
    # x.setdata("The boy called Brian.")
    # y.setdata(42)
    # x.display()
    # y.display()
except TypeError:
    print "***Error de sintaxis y/o en llamada de argumentos"
#except NameError: 
#    print "*** Error en definicion de Clases"

#print "Nombre del Trabajador : " + emp1.getName())