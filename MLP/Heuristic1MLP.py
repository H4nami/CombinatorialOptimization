#Nearest neighbor heuristic to solve the Minimum Latency Problem (MLP) 
#This script reads a file that contains a symetrical weights/time matrix
#it outputs a report file at the end of the analysis
#You can pass arguments to activate a II-opt algorithm and to randomize the initial city (node)
#You can run the script with the following syntax
#Heuristic1.py <Number of files to read> <Matrix Size> <Best city (0 or 1)> <Local search (0 or 1)>


from sys import argv
import random
from operator import itemgetter


def Lectura(numFiles,size,mejorC, busqueda):
	#Ciclo para abrir archivos de instancia
	for x in xrange(1,numFiles+1):

		#Mantener el archivo abierto
		nombre='instancia'+str(x)+'_'+str(size)+'.txt'
		with open(nombre, 'r') as archivo:

			#Leer los datos
			matrix=[str.split(line) for line in archivo if line[0].isalnum()]
			matrix=[[int(i) if i.isdigit() else "X" for i in line] for line in matrix]
			Heuristica(matrix,size,mejorC,busqueda)

		archivo.close()

def Heuristica(matrix,size,mejorC,busqueda):
	tiempos=[0 for i in range(size)]
	ciudades=[i for i in range(size)]
	ciudadesVisitadas=[999 for i in range(size)]
	for x in range(size):
		suma=0
		for y in range(size):
			if (str(matrix[x][y]).isdigit()):
				suma+=matrix[x][y]
		tiempos[x]=suma

	indice=[ciudades,tiempos]

	ciudadInicial=0
	if(mejorC==1):
		indicezip=zip(*indice)
		indicezip.sort(key=lambda x: x[1])
		indicezip=zip(*indicezip)
		ciudadInicial=indicezip[0][0]
	else:
		ciudadInicial=random.randint(0,size-1)
	
	ciudadesVisitadas[0]=ciudadInicial
	tiempo=0
	for x in range(size-1):
		sigNodo=0
		aux=100
		for y in range(size):
			if (y != ciudadesVisitadas[x]):
				sigNodo=matrix[ciudadesVisitadas[x]][y]
				if(sigNodo<aux and not y in ciudadesVisitadas):
					aux=sigNodo
					auxIndex=y
		tiempo+=aux
		ciudadesVisitadas[x+1]=auxIndex
	
	ciudadesVisitadas.append(ciudadInicial)

	if (busqueda==1):
		print str(ciudadesVisitadas)+' '+' Tiempo:'+str(tiempo)+'\n'
		busquedaLocal(matrix,ciudadesVisitadas,tiempo,size,busqueda,mejorC)
	else:
		print str(ciudadesVisitadas)+' '+str(ciudadInicial)+' Tiempo:'+str(tiempo)+'\n'
		escritura(ciudadesVisitadas,tiempo,mejorC,busqueda,0)




def busquedaLocal(matrix,ciudadesVisitadas,tiempo,size,busqueda,mejorC):
	ciudadesCopia=ciudadesVisitadas
	tiempoN=tiempo
	par1=[0,0]
	par2=[0,0]
	aux1=0
	aux2=0
	cont=0
	
	for index in xrange(size-2):
		for j in xrange(index,size-4):
			par1[0]=ciudadesVisitadas[(index)%size]
			par1[1]=ciudadesVisitadas[(index+1)%size]
			par2[0]=ciudadesVisitadas[(j+2)%size]
			par2[1]=ciudadesVisitadas[(j+3)%size]
			aux1=matrix[par1[0]][par1[1]]+matrix[par2[0]][par2[1]]
			aux2=matrix[par1[0]][par2[1]]+matrix[par2[0]][par1[1]]
			cont+=1
		

			if aux2<aux1:
				ciudadesVisitadas[(index)%size]=par1[0]
				ciudadesVisitadas[(index+1)%size]=par2[1]
				ciudadesVisitadas[(j+2)%size]=par2[0]
				ciudadesVisitadas[(j+3)%size]=par1[1]
				tiempoN=(tiempo-aux1)+aux2
			
	
	print str(ciudadesVisitadas)+' Tiempo'+str(tiempoN) #' Cont:'+str(cont)
	escritura(ciudadesVisitadas,tiempo,mejorC,busqueda,tiempoN)
	




def escritura(ciudadesVisitadas,tiempo,mejorC,busqueda,tiempoN):
	archivo=open('Resultados_Heuristica1.txt','a')

	if (busqueda==1):
		if (mejorC==1):
			archivo.write(str(ciudadesVisitadas)+' Tiempo:'+str(tiempo)+' Mejor ciudad'+' busqueda:'+str(tiempoN)+'\n')
		else:
			archivo.write(str(ciudadesVisitadas)+' Tiempo:'+str(tiempo)+' busqueda:'+str(tiempoN)+'\n')		
	else:
		if(mejorC==1):
			archivo.write(str(ciudadesVisitadas)+' Tiempo:'+str(tiempo)+' Mejor ciudad'+'\n')
		else:
			archivo.write(str(ciudadesVisitadas)+' Tiempo:'+str(tiempo)+'\n')

	archivo.close()



Lectura(int(argv[1]), int(argv[2]), int(argv[3]), int(argv[4]))