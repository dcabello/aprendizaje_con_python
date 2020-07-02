def miles(numero):
    letra = "Mil"    
    if str(numero)[0] == 1:
        pass    
    elif str(numero)[0] == "2":
        letra = "Dos " + letra 
    elif str(numero)[0] == "3":
        letra = "Tres" + letra     
    elif str(numero)[0] == "4":
        letra = "Cuatro" + letra 
    elif str(numero)[0] == "5":
        letra = "Cinco" + letra 
    elif str(numero)[0] == "6":
        letra = "Seis" + letra 
    elif str(numero)[0] == "7":
        letra = "Siete" + letra 
    elif str(numero)[0] == "8":
        letra = "Ocho" + letra 
    elif str(numero)[0] == "9":
        letra = "Nueve" + letra 
    return letra
    
numero = 2500
largo = len(str(numero))
if largo == 4:
    print(miles(numero))