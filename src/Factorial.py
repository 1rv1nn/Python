print("Haremos un factorial")
x=input=int(input("Dame un número cualquiera "))
if x>0:
  factorial=1
  for i in range(1,x+1):
       factorial=factorial*i

    
       print(factorial)
else:
   print("No podimos realizar la operacion tu número es menor a cero")


   #2   
#print("Veremos si tu número es par o impar 0: ")
#numero=int(input("Proporciona tu número "))
#if numero % 2==0:
#   print("Tu número es par")
#else:
#   print("Es impar")