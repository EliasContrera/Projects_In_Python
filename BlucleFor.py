""" Ejemplo de uso de bucle 'for' """

# Bucle 'for' con estructura 'lista'
from dataclasses import replace
from timeit import repeat


print("\nBucle 'for' con estructura 'lista'")
print("==================================\n")

print("Ejemplo: Itera una lista de animales\n")

# Definir lista
animales = ['gato', 'perrito', 'serpiente']
for animal in animales:
    print("El animal es: {0}, tamaño de palabra es: {1}".format(
        animal, len(animal)))
print("Tamaño de la lista: ", len(animales))

# Si se necesita iterar sobre una secuencia de números. 
# Generar una lista conteniendo progresiones aritméticos
print("\nFunción range()")
print("===============\n")
a =  range(15)
print("Rango de 15 números:", a)
print(type(range))


