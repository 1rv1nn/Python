#Cruz González Irvin Javier.


#TAREA 1#


### Utiliza UNICAMENTE los datos dentro del siguiente diccionario: 

dic={'k1':('+','-','*','/',':',['1234567890'],'//','%','*=','+=','='),
	 'k2':[('murcielago','zacatecas','normandia','ejercicio','jupiter','mayonesa'),
	 		(True,[0,1],False),('circunferencia','rectangulo','lado',
	 		 'area','perimetro','etc')]
	 ,'k3':[(3.1415926,2.71828182,1.6180339887,1.41421356237),('e',
	 	   'raiz de dos','phi','pi')],
	 'k4':' '
	}

dic

#1.- Escribe la palabra "ingenieria y ciencias" 
print("ejercicio 1: "+ dic['k2'][0][0][4]+dic['k2'][0][2][0]+dic['k2'][0][0][8]+dic['k2'][0][0][5]+dic['k2'][0][2][0]+dic['k2'][0][0][5]
      +dic['k2'][0][0][2]+dic['k2'][0][0][4]+dic['k2'][0][0][7]+" "+dic['k2'][0][5][2]+" "+dic['k2'][0][0][3]
			   +dic['k2'][0][0][4]+dic['k2'][0][0][5]+dic['k2'][0][3][4]+dic['k2'][0][0][4]+dic['k2'][0][1][1]+dic['k2'][0][1][8])

#print(dic ['k2']['murcielago'][4])

#2 Calcula el area de una circunferencia con radio igual a 18
print("ejercicio 2: "+ str (((dic['k3'][0][0]*18)**2)))

#3 Calcula el perimetro de un rectangulo sabiendo que b = 207 y h = 839
print("ejercicio 3: "+ str ((2*(839+207))))

#4 Calcula la hipotenusa de un triangulo con ambos catetos igual a 1 (Teorema de Pitagoras)
import math
print("ejercicio 4: "+ str (math.sqrt(1**2+1**2)))

#5 Enlista los numeros irracionales en 'k3' con su respectivo nombre.
print("ejercicio 5: \n"+ str ((dic['k3'][0][0]))+":"+ str ((dic['k3'][1][3]))+"\n"+str ((dic['k3'][0][1]))+":"+ str ((dic['k3'][1][0]))+
      "\n"+str ((dic['k3'][0][3]))+":"+ str ((dic['k3'][1][1]))+"\n"+str ((dic['k3'][0][2]))+":"+str ((dic['k3'][1][2])))

