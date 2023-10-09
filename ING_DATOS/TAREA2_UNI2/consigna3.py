persona = {}

while True:
    nombre = input("Nombre: ")
    persona["Nombre"] = nombre

    edad = input("Edad: ")
    persona["Edad"] = edad

    sexo = input("Sexo: ")
    persona["Sexo"] = sexo

    telefono = input("Teléfono: ")
    persona["Teléfono"] = telefono

    email = input("Correo electrónico: ")
    persona["Correo electrónico"] = email

    print("\nInformación completa de la persona:")
    for campo, valor in persona.items():
        print(f"{campo}: {valor}")

    continuar = input("¿Deseas ingresar información de otra persona? (Escribe 'BASTA' para terminar o cualquier otra cosa para continuar): ")
    
    if continuar == 'BASTA':
        break