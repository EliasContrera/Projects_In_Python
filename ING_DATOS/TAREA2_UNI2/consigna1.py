nombre = input("Ingresar nombre: ")
edad = input("Ingresar edad: ")
direccion = input("Ingresar direccion: ")
telefono = input("Ingresar telefono: ")

thisdict = {
  "nombre": nombre,
  "edad": edad,
  "direccion": direccion,
  "telefono": telefono,
}
print(f"{nombre} tiene {edad} años, vive en {direccion} y su número de teléfono es: {telefono}")