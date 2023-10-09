print("Se convierte nota (0 a 100) a letra")

nota = int(input("Ingrese la nota: "))

if nota > 90 and nota <= 100:
    print("A")

elif nota > 80 and nota < 89:
    print("B")
elif nota > 70 and nota < 79:
    print("C")
elif nota > 50 and nota < 69:
    print("D")
elif nota > 0 and nota < 59:
    print("F")