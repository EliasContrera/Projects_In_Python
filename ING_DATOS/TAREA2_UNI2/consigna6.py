import json

archivo_listado = "telefonos.json"

# Cargar los datos existentes o crear un diccionario vacío
try:
    with open(archivo_listado, "r") as archivo:
        listado_telefonico = json.load(archivo)
except FileNotFoundError:
    listado_telefonico = {}

while True:
    print("\nMenú:")
    print("1. Consultar teléfono de un cliente")
    print("2. Agregar nuevo cliente")
    print("3. Eliminar cliente")
    print("4. Salir")

    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == "1":
        nombre_cliente = input("Ingrese el nombre del cliente: ")
        telefono = listado_telefonico.get(nombre_cliente)
        if telefono is not None:
            print(f"Teléfono de '{nombre_cliente}': {telefono}")
        else:
            print("Cliente no encontrado")
    elif opcion == "2":
        nombre_cliente = input("Ingrese el nombre del nuevo cliente: ")
        telefono_cliente = input("Ingrese el teléfono del nuevo cliente: ")
        listado_telefonico[nombre_cliente] = telefono_cliente
        with open(archivo_listado, "w") as archivo:
            json.dump(listado_telefonico, archivo)
        print(f"Cliente '{nombre_cliente}' agregado con éxito.")
    elif opcion == "3":
        nombre_cliente = input("Ingrese el nombre del cliente a eliminar: ")
        if nombre_cliente in listado_telefonico:
            del listado_telefonico[nombre_cliente]
            with open(archivo_listado, "w") as archivo:
                json.dump(listado_telefonico, archivo)
            print(f"Cliente '{nombre_cliente}' eliminado.")
        else:
            print("Cliente no encontrado")
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida.")