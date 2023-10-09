import json

def main():
    carrito = {}
    total = 0

    while True:
        articulo = input("Ingrese el nombre del articulo (o 'basta' para finalizar): ")
        if articulo == 'basta':
            break

        try:
            precio = float(input("Ingrese el precio del articulo: "))
            carrito[articulo] = precio
            total += precio
        except ValueError:
            print("Error: Por favor, ingrese un precio valido.")

    print("\nLista de Compra:")
    for articulo, precio in carrito.items():
        print(f"{articulo}: ${precio:.2f}")

    print(f"Coste Total: ${total:.2f}")

    with open("carrito.json", "w") as archivo:
        json.dump(carrito, archivo)

if __name__ == "__main__":
    main()