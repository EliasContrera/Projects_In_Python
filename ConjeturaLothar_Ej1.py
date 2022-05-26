def lothar(x):
    aux = 0
    if x > 0:
        while x != 1:   # El bucle se ejecuta hasta que llegue a 1.
            if x % 2:  # Chequeo para verificar numero impar
                x = x * 3 + 1 # Si es impar, se multiplica por 3 y se suma 1
            else:
                x //= 2 # Si es par, se divide por 2
            aux+=1
    else:
        return False # Se retorna 0 si el ingreso fue igual o menor a 0. (invalido)
    print(aux)
    
n = int(input())
lothar(n)
        