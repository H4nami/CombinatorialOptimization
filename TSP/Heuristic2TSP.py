from sys import argv
from operator import itemgetter

def Lectura(numFiles,size):
	restantes=numFiles

	#Ciclo para abrir archivos de instancia
	for x in xrange(1,numFiles+1):

		#Mantener el archivo abierto
		nombre='instancia'+str(x)+'_'+str(size)+'.txt'
		with open(nombre, 'r') as archivo:

			#Leer los datos
			lineas=[str.split(line) for line in archivo if line[0].isdigit()]
			peso=int(lineas[size][0])
			print peso
			print lineas
			print '\n'
			for i in lineas:
				del i[0]
			del lineas[size]
			Heuristica(lineas, peso, nombre)

		archivo.close()

def Heuristica(lineas, pesomax, nombre):

	lineas=[[int(j) for j in i] for i in lineas] 
	lineas.sort(key=itemgetter(1), reverse=True)
	print lineas
	pesos=[i[0] for i in lineas]
	valores=[i[1] for i in lineas]
	sumap=0
	cont=0
	for i in pesos:
		if i<=(pesomax-sumap):
			sumap+=i
			cont+=1
	print sumap
	sumav=0
	for i in xrange(0,cont+1):
		sumav+=valores[i]
	print sumav

	escritura(sumap,sumav,nombre)



def escritura(sumap,sumav,nombre):
	archivo=open('Resultados_Heuristica2.txt','a')
	archivo.write(nombre+' Peso:'+str(sumap)+' Valor:'+str(sumav)+'\n')
	archivo.close()



Lectura(int(argv[1]), int(argv[2]))