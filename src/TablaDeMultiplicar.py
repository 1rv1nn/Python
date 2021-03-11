print("Vamos haremos una tabla de multiplicar con números positivos(-1 para salir)")

número=int(input("Dame un número positivo: "))

while número!=-1: #Evalua la condición,sí es verdadera se sigue ejecutando hasta que deje de cumplirse   
    for i in range(1,11):
        resultado=i*número
        print(("%s x %s =%s")%(número,i,resultado))
    número=int(input("Dame un número positivo: "))    

print("Gracias por colaborar")   

  
