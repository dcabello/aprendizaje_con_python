from __future__ import print_function
import sys, string
print( "This is an error message", file=sys.stderr )
print( "This is stdout" )
print( "This is also stdout", file=sys.stdout )
print( "335/113=",)
print( 335.0/113.0)
print( "Hi, Mom", "Isn't it lovely?",)
print('I said, "Hi".', 42, 91056) 
print("Mensaje de error del sistema!!!", file=sys.stderr)  
print("Mensaje de salida normal del sistema!!!", file=sys.stdout) 
print("Todo Ok!!!") 
variable1 = "Fino compa!!!"
print(variable1)
variable2 = "Ta rudo compa!!!"
print(variable2)
variable3 = variable1 * 3 + " " + variable2
print(variable3)
print(variable3[10], len(variable3), len(variable2), len(variable1))
variable4 = 2505
variable5 = 3273
print (variable4 + variable5, variable4 * 5)
for i in variable1: print(i, "x" in variable1)
print(variable1[3:9],"/", variable1[-7: -3])
print("variable2 = %s, variable4 = %d" % (variable2, variable4))
print("variable2 en mayusculas = %s, el signo ! esta en la posicion %d" % (string.upper(variable2), string.find(variable2,"!")))
string = "The Life of Brian & me"
print("El largo de la cadena '"+string+"' es : "+str(len(string)))