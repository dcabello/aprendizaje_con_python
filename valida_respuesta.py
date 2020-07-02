def valida_respuesta(respuesta):
    if respuesta == "Y" or respuesta == "y" or respuesta == "Yes" \
    or respuesta == "YES":
        print "You chose Yes"
    else:
        print "You chose No"
valida_respuesta("Y")
valida_respuesta("Yes")
valida_respuesta("yES")
valida_respuesta("yEs")
valida_respuesta("No")        
