def calcular_Edad():
    madre = int(input("Ingrese la edad de la madre: "))
    hijo = int(input("Ingrese la edad del hijo: "))
    
    if hijo > madre :
        print("Las edades ingresadas son invalidas, un hijo no puede ser mayor a una madre. \n")

    else:
        edad_Actual = madre - hijo
    
    print(f"La edad de la madre al momento de dar a luz a su hijo es de {edad_Actual}")
    
calcular_Edad()