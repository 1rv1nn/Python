print("Hola Mundo!")

print("Bienvenid@ haremos una suma ")
try:
    w=int(input("Dame un número "))
    e=int(input("Dame un segundo número "))
    print("La suma de "+str(w)+"+"+str(e)+"="+str(w+e))
except ValueError:
    print("Ingresa un dato invalida.Intenta de nuevo") 