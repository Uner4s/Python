import math
import os

def main():


	g= open("Orden_Matriz.txt", "r",encoding = 'utf-8')
	lines = g.read()
	Orden_Matriz = lines.split()
	f= open("Matriz.txt", "r",encoding = 'utf-8')
	lines = f.read()
	lista = lines.split()
	f.close()
	g.close()
    
	Orden_Matriz[0] = int(Orden_Matriz[0])
	matriz_diagonal = [] 
	matriz_valores = [] 
	matriz_componentes = [] 
	matriz_soluciones = []
	matriz_diagonal = [[0 for col in range(Orden_Matriz[0])] for row in range(Orden_Matriz[0])]
	matriz_valores = [[0 for col in range(Orden_Matriz[0])] for row in range(Orden_Matriz[0])]


	x = 0 #i
	y = 0 #h
	z = 0 #e
	while z != Orden_Matriz[0] :
		matriz_diagonal[z][x] = int(lista[y])
		x = x + 1
		y = Orden_Matriz[0] + 2 + y
		z = z + 1

	z = Orden_Matriz[0]
	for x in range(Orden_Matriz[0]):
		matriz_componentes.append(lista[z])
		z = z + Orden_Matriz[0] + 1 
	for x in range(Orden_Matriz[0]):
		matriz_componentes[x] = int(matriz_componentes[x])	

	y = 0
	for z in range(Orden_Matriz[0]):
		for x in range(Orden_Matriz[0]):
			matriz_valores[z][x] = int(lista[y])
			y = y + 1
		y = y + 1

	x = 0
	y = 0
	z = 0

	while z != Orden_Matriz[0]:
		matriz_valores[z][x] = 0
		x = x + 1
		y = Orden_Matriz[0] + 2 + y
		z = z + 1

	R= 0 #Resultado
	C = 0 #Condicion


	for x in range(Orden_Matriz[0]):
		for z in range(Orden_Matriz[0]):
			R = R + abs(matriz_valores[x][z])
		if abs(matriz_diagonal[x][x]) > R:
			C = C + 1
			R = 0

	resultados_Seidel = [0 for col in range(1) for row in range(Orden_Matriz[0]*2)]
	if C == Orden_Matriz[0]:

		margen_error = float(input("Ingrese el margen de error que desea ( Ejemplo: 0.0001 ) / Debe ingresarse con un punto (.)  = "))

		matriz_soluciones = [0 for col in range(1) for row in range(Orden_Matriz[0]*2)]
		for x in range(Orden_Matriz[0]*2):
			matriz_soluciones[x] = float(matriz_soluciones[x])
		
		
		print(" ")
		print("     **********************************")
		print("     ******     Metodo Seidel     *****")
		print("     **********************************")
		print(" ")

		cont = 0 #contador
		print("     Iteracion / ",cont)
		Orden_Matriz[0] = int(Orden_Matriz[0])
		for x in range(Orden_Matriz[0]):
			print("       X",x+1,"=",matriz_soluciones[x])

		espacio = Orden_Matriz[0]
		suma = 0

		norma_componentes = 1000000

		while norma_componentes > margen_error:

			for z in range(Orden_Matriz[0]):
				for i2 in range(Orden_Matriz[0]):
					suma = float(suma + matriz_valores[z][i2]*resultados_Seidel[i2])
				matriz_soluciones[espacio] = float(((matriz_componentes[z]-(suma))/matriz_diagonal[z][z]))
				resultados_Seidel[z] = float(((matriz_componentes[z]-(suma))/matriz_diagonal[z][z]))
				espacio = espacio + 1
				suma = 0

			aux = 0
			y = Orden_Matriz[0]
			for x in range(Orden_Matriz[0]):
				aux = aux + (matriz_soluciones[y]-matriz_soluciones[y-Orden_Matriz[0]])**2
				y = y + 1
				norma_componentes = math.sqrt(aux)
			cont = cont + 1
			espacio = Orden_Matriz[0]
			print("     Iteracion / ",cont)
			Orden_Matriz[0] = int(Orden_Matriz[0])
			for x in range(Orden_Matriz[0]):
				print("       X",x+1,"=",matriz_soluciones[espacio])
				espacio = espacio + 1

			espacio = Orden_Matriz[0]
			for i in range(Orden_Matriz[0]):
				matriz_soluciones[i] = matriz_soluciones[i+Orden_Matriz[0]]

		print(" ")
		print("     **********************************")
		print("     ******     Metodo Jacobi     *****")
		print("     **********************************")
		print(" ")
		
		matriz_soluciones = [0 for col in range(1) for row in range(Orden_Matriz[0]*2)]
		for x in range(Orden_Matriz[0]*2):
			matriz_soluciones[x] = float(matriz_soluciones[x])
		
		cont = 0
		print("     Iteracion / ",cont)
		Orden_Matriz[0] = int(Orden_Matriz[0])
		for x in range(Orden_Matriz[0]):
			print("       X",x+1,"=",matriz_soluciones[x])				

		espacio = Orden_Matriz[0]
		suma = 0
		norma_componentes = 1000


		matriz_soluciones =[]
		matriz_soluciones = [0 for col in range(1) for row in range(Orden_Matriz[0]*2)]

		while norma_componentes > margen_error:

			for z in range(Orden_Matriz[0]):
				for i2 in range(Orden_Matriz[0]):
					suma = float(suma + matriz_valores[z][i2]*matriz_soluciones[i2])
				matriz_soluciones[espacio] = float(((matriz_componentes[z]-(suma))/matriz_diagonal[z][z]))
				espacio = espacio + 1
				suma = 0

			aux = 0
			y = Orden_Matriz[0]
			for x in range(Orden_Matriz[0]):
				aux = aux + (matriz_soluciones[y]-matriz_soluciones[y-Orden_Matriz[0]])**2
				y = y + 1
				norma_componentes = math.sqrt(aux)
			cont = cont + 1
			espacio = Orden_Matriz[0]
			print("     Iteracion / ",cont)
			Orden_Matriz[0] = int(Orden_Matriz[0])
			for x in range(Orden_Matriz[0]):
				print("       X",x+1,"=",matriz_soluciones[espacio])
				espacio = espacio + 1

			espacio = Orden_Matriz[0]
			for i in range(Orden_Matriz[0]):
				matriz_soluciones[i] = matriz_soluciones[i+Orden_Matriz[0]]

	else:
		print("La matriz no cumple las condiciones de la diagonal pesada,debe cambiar los valores manualmente para que cumpla las siguientes condiciones")
		print("1._ CONDICION NECESARIA : |a.ii| < |a.ij| / Donde a distinto de j")
		print("2._ CONDICION SUFICIENTE : |a.ii| < ∑|a.ij|")

main()
