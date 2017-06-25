# AUTOR: Nicolas Fernando Perez Poblete
# FECHA: 04 de Enero de 2014
# VERSIÓN: 2.0


############################################################################
# 																		   #
#   FUNCIONES															   #
#																		   #
############################################################################

############################################################################
#                                                                          #
#   IMPORTACIÓN DE FUNCIONES                                               #
#                                                                          #
############################################################################


import math
import os

def metodo_Jacobi(Matriz_A,Matriz_B,Matriz_C,Matriz_Resultados,orden):
	
	contador = 0
	print("Iteracion --> ",contador)
	orden = int(orden)
	for i in range(orden):
		print("X",i+1," ---> ",Matriz_Resultados[i])

	espacio = orden
	suma = 0


	error = 1

	while error > 0.0001:

		for e in range(orden):
			for u in range(orden):
				suma = float(suma + Matriz_B[e][u]*Matriz_Resultados[u])
			Matriz_Resultados[espacio] = float(((Matriz_C[e]-(suma))/Matriz_A[e][e]))
			espacio = espacio + 1
			suma = 0

        #Calcular distancia entre iteraciones
		aux = 0
		h = orden
		for i in range(orden):
			aux = aux + (Matriz_Resultados[h]-Matriz_Resultados[h-orden])**2
			h = h + 1
			error = math.sqrt(aux)
		contador = contador + 1
		espacio = orden
		print("Iteracion --> ",contador)
		orden = int(orden)
		for i in range(orden):
			print("X",i+1," ---> ",Matriz_Resultados[espacio])
			espacio = espacio + 1

		espacio = orden
		for o in range(orden):
			Matriz_Resultados[o] = Matriz_Resultados[o+orden]




def metodo_Seidel(Matriz_A,Matriz_B,Matriz_C,Matriz_Resultados,orden):
	
	contador = 0
	print("Iteracion --> ",contador)
	orden = int(orden)
	for i in range(orden):
		print("X",i+1," ---> ",Matriz_Resultados[i])

	espacio = orden
	suma = 0

	matriz_respaldo = [0 for col in range(1) for row in range(orden*2)]


	error = 1

	while error > 0.0001:

		for e in range(orden):
			for u in range(orden):
				suma = float(suma + Matriz_B[e][u]*matriz_respaldo[u])
			Matriz_Resultados[espacio] = float(((Matriz_C[e]-(suma))/Matriz_A[e][e]))
			matriz_respaldo[e] = float(((Matriz_C[e]-(suma))/Matriz_A[e][e]))
			espacio = espacio + 1
			suma = 0

        #Calcular distancia entre iteraciones
		aux = 0
		h = orden
		for i in range(orden):
			aux = aux + (Matriz_Resultados[h]-Matriz_Resultados[h-orden])**2
			h = h + 1
			error = math.sqrt(aux)
		contador = contador + 1
		espacio = orden
		print("Iteracion --> ",contador)
		orden = int(orden)
		for i in range(orden):
			print("X",i+1," ---> ",Matriz_Resultados[espacio])
			espacio = espacio + 1

		espacio = orden
		for o in range(orden):
			Matriz_Resultados[o] = Matriz_Resultados[o+orden]

#                                       Funcion Principal
#----------------------------------------------------------------------------------------------------------#

def funcion_principal(orden, lista):

	orden = int(orden)
	orden_total = orden*orden
	orden_total = int(orden_total)
	Matriz_A = [] # Matriz de la diagonal y ceros el resto
	matriz_aux = []
	Matriz_B = [] # Matriz de la diagonal llena de ceros y el resto los valores correspondientes
	Matriz_C = [] # Matriz que contiene los resultados.
	Matriz_Resultados = []

	# buckets = [[0 for col in range(orden)] for row in range(orden)]
	# print(buckets)

	Matriz_A = [[0 for col in range(orden)] for row in range(orden)]
	Matriz_B = [[0 for col in range(orden)] for row in range(orden)]
	Matriz_Resultados = [0 for col in range(1) for row in range(orden*2)]
	print(Matriz_Resultados)
	for i in range(orden*2):
		Matriz_Resultados[i] = float(Matriz_Resultados[i])

	i = 0
	h = 0
	e = 0
    
    # Llenamos la matriz A con la diagonal.
#--------------------------------------------
	while e != orden :
		Matriz_A[e][i] = int(lista[h])
		i = i + 1
		h = orden + 2 + h
		e = e + 1
	print(Matriz_A)
#--------------------------------------------


	# Llenamos la matriz con los resultados de la matriz principal.
#---------------------------------------------------------------------
	e = orden
	for i in range(orden):
		Matriz_C.append(lista[e])
		e = e + orden + 1 
	for i in range(orden):
		Matriz_C[i] = int(Matriz_C[i])

	print(Matriz_C)		
#---------------------------------------------------------------------


	# Llenamos la matriz restante con los componentes dejando la diagonal en 0
#-------------------------------------------------------------------------------
	h = 0
	for e in range(orden):
		for i in range(orden):
			Matriz_B[e][i] = int(lista[h])
			h = h + 1
		h = h + 1

	e = 0
	i = 0
	h = 0

	while e != orden:
		Matriz_B[e][i] = 0
		i = i + 1
		h = orden + 2 + h
		e = e + 1

	print(Matriz_B)
#-------------------------------------------------------------------------------
	

	resultado = 0
	condicion = 0
	for i in range(orden):
		for e in range(orden):
			resultado = resultado + abs(Matriz_B[i][e])
		if abs(Matriz_A[i][i]) > resultado:
			condicion = condicion + 1
			resultado = 0

	if condicion == orden:
		print("La matriz cumple con las condiciones necesarias")
		print("Ingrese una de las siguientes opciones")

		print("Metodo Gauss Jacobi  ---> [1]")
		print("Metodo Gauss Seidel  ---> [2]")

		metodo = int(input("Ingrese que metodo desea ocupar"))


		if metodo == 1:
			metodo_Jacobi(Matriz_A,Matriz_B,Matriz_C,Matriz_Resultados,orden)
		elif metodo == 2:
			metodo_Seidel(Matriz_A,Matriz_B,Matriz_C,Matriz_Resultados,orden)
		else:
			print("Ingrese una opcion valida")
	else:
		print("La matriz no cumple con las condiciones necesarias")
		print("Porfavor, cambie manualmente los valores de la matriz para que cumpla con los requisitos  |aii| > |aij| ")


#----------------------------------------------------------------------------------------------------------#


def programa():

	orden = input("Ingrese el orden de la matriz")
	f= open("prueba.txt", "r",encoding = 'utf-8')
	lines = f.read()
	lista = lines.split()
	f.close()
	print("Se enviaran los datos a la funcion correspondiente")
	funcion_principal(orden, lista)
    
programa()
