import json

# Cadena de texto con la información del directorio
directorio_texto = """cuit;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"""

# Dividir la cadena en líneas
lineas = directorio_texto.strip().split('\n')

# Obtener los nombres de los campos desde la primera línea
nombres_campos = lineas[0].split(';')

# Inicializar el diccionario de clientes
clientes = {}

# Procesar las líneas de datos de clientes
for linea in lineas[1:]:
    datos_cliente = linea.split(';')
    cuit_cliente = datos_cliente[0]
    info_cliente = {}
    
    # Crear un diccionario para el cliente con los nombres de los campos como claves
    for i in range(1, len(nombres_campos)):
        info_cliente[nombres_campos[i]] = datos_cliente[i]
    
    # Agregar el diccionario del cliente al diccionario principal usando el CUIT como clave
    clientes[cuit_cliente] = info_cliente

# Guardar el diccionario en un archivo JSON
with open('directorio_clientes.json', 'w') as archivo_json:
    json.dump(clientes, archivo_json, indent=4)

print("Diccionario de clientes guardado en 'directorio_clientes.json'")