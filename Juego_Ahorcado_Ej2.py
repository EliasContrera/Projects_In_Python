import random #Importamos la libreria random

maximo_errores = 100 #Utilizo variable global maximoerrores para utilizarla en el programa

def ahorcado(diccionario):  # Definimos nuestra funcion ahorcado, donde recibe la palabra ingresada por el jugador 1
    palabra = random.choice(diccionario).lower()
    palabra_Secreta = ['_'] * len(palabra)
    return palabra_Secreta, palabra, []


def pedir_letra(palabra_Secreta, errores):

    letra = input().lower()

    return letra


def procesar_letra(letra, palabra, palabra_Secreta, errores):
    if letra in palabra:
        actualizar_palabra_Secreta(letra, palabra, palabra_Secreta)
    else:
        errores.append(letra) # Ponemos la letra erronea a la lista de errores


def actualizar_palabra_Secreta(letra, palabra, palabra_Secreta):
    for indice, letra_palabra in enumerate(palabra): #Utilizo la funcion enumerate para recorrer y buscar la letra en la palabra.
        if letra == letra_palabra: #Comparacion de la letra ingresada con alguna letra de la palabra secreta
            palabra_Secreta[indice] = letra # Asignamos la letra ya que coincide.


def comprobar_palabra(palabra_Secreta):
    return '_' not in palabra_Secreta #Si hay espacios vacios en la palabra, entonces sigue el juego


def jugar_al_ahorcado(diccionario):

    intentos = 0
    
    palabra_Secreta, palabra, errores = ahorcado(diccionario) 
    while len(errores) < maximo_errores: # En mi caso, le doy al jugador 10 intentos para adivinar, y eso lo comparo, mientras errores sea menor al maximo, sigue el bucle
        letra = pedir_letra(palabra_Secreta, errores) #Letra toma el valor que retorna la funcion pedir_letra
        intentos+=1  # Incremento el numero de intentos
        procesar_letra(letra, palabra, palabra_Secreta, errores) #La funcion procesar letra es la que se encarga de validar el ingreso.
        if comprobar_palabra(palabra_Secreta): #La funcion comprobar_palabra realiza la comparacion
            print(intentos)
            break


if __name__ == '__main__':
    
    intentos = 0
    palabra_jugador1 = input()

    diccionario = [palabra_jugador1]
    jugar_al_ahorcado(diccionario)