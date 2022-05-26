def ConvertirAFarenheit(tempC): #Funcion que convierte los grados a Celcius
    return tempC * 9 / 5 + 32 #Retorna el valor de la variable TempC que guarda la operacion de conversion

def ConvertirAKelvin(tempC): #Funcion que convierte los grados a Kelvin
    return tempC + 273.15 #Retorna el valor de la variable TempC que guarda la operacion de conversion

temp = float(input("Ingrese temperatura (en celcius): "))

if temp < -273.15: #Si la temperatura ingresada es mayor menor a -273.15, se indica por pantalla un mensaje de advertencia
  print("Error: La temperatura ingresada inferior al cero absoluto.") 
else:  #Si la temeratura es mayor a la indicada ..
  print("Temperatura Farenheit: ", ConvertirAFarenheit(temp)) #..Le paso por parametro el valor ingresado por el usuario a ambas funciones
  print("Temperatura Kelvin: ", ConvertirAKelvin(temp))