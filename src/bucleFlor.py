"""
Generar números enteros entre el 1 y el 1000 e imprimir el número dado, 
pero si el número es múltiplo de 3 imprimirá la palabra “Fizz”, en el 
caso que sea múltiplo de 5 deberá imprimir “Buzz”, y en caso de ser 
múltiplo de ambos (3 y 5) imprimirá “FizzBuzz”
"""

for i in range(1,1001):
   if(i%3==0):
       print("Fzzz")
   elif(i%5==0):
       print("Buzz")
   else:
       print(i)        
                 
    
   