from itertools import count


votos = int(input())
postulante = [] # Creo la lista vacia

if votos >= 1 and votos <= 100:
    for i in range(votos):
        nuevo_postulante = input()  # Cada elemento es ingresado por teclado
        postulante.append(nuevo_postulante) # Se agrega el elemento a la lista
            
else:
    print("Numero invalido") # Si se ingreso un numero invalido, se muestra este mensaje por pantalla

aux = 1 # variable auxiliar inicializada en 1 para su uso en el recorrido
flag = postulante[aux] # variable flag es el elemento que corresponda con aux

for y in range(len(postulante)):
    if postulante[y] == flag: #Si el elemento 0 es igual al elemento 1
        aux += 1   # Incremento la variable aux para comparar el elemento 1 con el elemento 2

    else:
        aux += 1 #Incremento el valor de aux para comparar con el siguiente elemento


print(max(set(postulante), key = postulante.count)) #Imprimo por pantalla el elemento que se repitio mas veces
