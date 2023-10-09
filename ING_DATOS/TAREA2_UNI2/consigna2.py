verduleria = {
    "manzana": 7.0,
    "banana": 5.5,
    "naranja": 10.5,
}

print(f"Stock disponible: {verduleria}")
fruta = input("Ingresé una fruta de las existentes: ") 

if fruta in verduleria:
    try:
        kg = float(input("Ingrese la cantidad de KG que desea de su fruta: "))
        total = kg * verduleria[fruta]
        print(f"El precio de {kg} kilos de {fruta} es ${total:.2f}")
    except ValueError:
        print("La valor ingresado es invalido.")
else:
    print("La fruta ingresada no está disponible.")