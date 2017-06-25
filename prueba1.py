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


def Matriz_DiagonalCero(Matriz_B,orden, lista):


	# Llenamos la matriz restante con los componentes dejando la diagonal en 0
	#-------------------------------------------------------------------------------
	contador_1 = 0
	for contador_2 in range(orden):
		for contador_3 in range(orden):
			Matriz_B[contador_2][contador_3] = int(lista[contador_1])
			contador_1 = contador_1 + 1
		contador_1 = contador_1 + 1

	(contador_4, contador_5,contador_6) = (0,0,0)

	while contador_4 != orden:
		Matriz_B[contador_4][contador_5] = 0
		contador_5 = contador_5 + 1
		contador_6 = orden + 2 + contador_6
		contador_4 = contador_4 + 1
	print("- Matriz de los componentes  | R | -")
	print("-----------------------------------------------")
	for contador_minimo in range(orden):
		print("| ",Matriz_B[contador_minimo])
	print("-----------------------------------------------")
	#-------------------------------------------------------------------------------
	return Matriz_B
	


def Matriz_resultadosMatriz(Matriz_C,orden, lista):

	# Llenamos la matriz con los resultados de la matriz principal.
	#---------------------------------------------------------------------
	contador_1 = orden
	for contador_2 in range(orden):
		Matriz_C.append(lista[contador_1])
		contador_1 = contador_1 + orden + 1 
	for contador_3 in range(orden):
		Matriz_C[contador_3] = int(Matriz_C[contador_3])

	print("- Matriz de los resultados  | B | -")
	print("-----------------------------------------------")
	for contador_minimo in range(orden):
		print("|",Matriz_C[contador_minimo],"|")
	print("-----------------------------------------------")	
	print(" ")
	print(" ")
	#---------------------------------------------------------------------
	return Matriz_C


def Matriz_Diagonal(Matriz_A,orden, lista):

	(contador_1,contador_2,contador_3)=(0,0,0)
    # Llenamos la matriz A con la diagonal.
	#-------------------------------------------------------------
	while contador_3 != orden :
		Matriz_A[contador_3][contador_1] = int(lista[contador_2])
		contador_1 = contador_1 + 1
		contador_2 = orden + 2 + contador_2
		contador_3 = contador_3 + 1
	print("- Matriz de la Diagonal  | D | -")
	print("-----------------------------------------------")
	for contador_minimo in range(orden):
		print("| ",Matriz_A[contador_minimo])
	print("-----------------------------------------------")
	#-------------------------------------------------------------
	return Matriz_A




def metodo_Jacobi(Matriz_A,Matriz_B,Matriz_C,Matriz_Resultados,orden):
	

	Contador_Externo = orden
	(suma_de_valores,iteracion_principal) = (0,0)
	print("*----------------------------------------------------------*")
	print("|  Numero de la Iteracion = ",iteracion_principal, "  |")
	orden = int(orden)	
	for contador_resultados in range(orden):
		print("X",contador_resultados+1,"  = ","%.4f" %Matriz_Resultados[contador_resultados])
	print("|  Grado de error = ","  Nulo")
	print("*----------------------------------------------------------*")

	Norma_Resultados_Matrices = 1
	while Norma_Resultados_Matrices > 0.0001:

		for contador_resultados2 in range(orden):
			for contador_resultados3 in range(orden):
				suma_de_valores = float(suma_de_valores + Matriz_B[contador_resultados2][contador_resultados3]*Matriz_Resultados[contador_resultados3])
			Matriz_Resultados[Contador_Externo] = float(((Matriz_C[contador_resultados2]-(suma_de_valores))/Matriz_A[contador_resultados2][contador_resultados2]))
			Contador_Externo = Contador_Externo + 1
			suma_de_valores = 0


		valor_auxiliar = 0
		contador_norma = orden
		for contador_resultados in range(orden):
			valor_auxiliar = valor_auxiliar + (Matriz_Resultados[contador_norma]-Matriz_Resultados[contador_norma-orden])**2
			contador_norma = contador_norma + 1
			Norma_Resultados_Matrices = math.sqrt(valor_auxiliar)
		iteracion_principal = iteracion_principal + 1
		Contador_Externo = orden

		print("*----------------------------------------------------------*")
		print("|  Numero de la Iteracion = ",iteracion_principal, "  |")
		orden = int(orden)
		for contador_resultados in range(orden):
			print("X",contador_resultados+1,"  = ","%.4f" %Matriz_Resultados[Contador_Externo])
			Contador_Externo = Contador_Externo + 1
		print("|  Grado de error = ","%.4f" %Norma_Resultados_Matrices)
		print("*----------------------------------------------------------*")
		Contador_Externo = orden
		for cambio_posicion in range(orden):
			Matriz_Resultados[cambio_posicion] = Matriz_Resultados[cambio_posicion+orden]



def metodo_Seidel(Matriz_A,Matriz_B,Matriz_C,Matriz_Resultados,orden):
	
	suma_de_valores = 0 # Suma los valores que se convierten en las iteraciones especificas.
	iteracion_principal = 0 # Va contando la cantidad de iteraciones realizadas.


	print("*----------------------------------------------------------*")
	print("|  Numero de la Iteracion = ",iteracion_principal, "  |")
	orden = int(orden)
	for contador_resultados in range(orden):
		print("X",contador_resultados+1,"  = ","%.4f" %Matriz_Resultados[contador_resultados])
	Contador_Externo = orden
	print("|  Grado de error = ","  Nulo")
	print("*----------------------------------------------------------*")	

	matriz_respaldo = [0 for col in range(1) for row in range(orden*2)]

	Norma_Resultados_Matrices = 1
	while Norma_Resultados_Matrices > 0.0001:

		for contador_resultados2 in range(orden):
			for contador_resultados3 in range(orden):
				suma_de_valores = float(suma_de_valores + Matriz_B[contador_resultados2][contador_resultados3]*matriz_respaldo[contador_resultados3])
			Matriz_Resultados[Contador_Externo] = float(((Matriz_C[contador_resultados2]-(suma_de_valores))/Matriz_A[contador_resultados2][contador_resultados2]))
			matriz_respaldo[contador_resultados2] = float(((Matriz_C[contador_resultados2]-(suma_de_valores))/Matriz_A[contador_resultados2][contador_resultados2]))
			Contador_Externo = Contador_Externo + 1
			suma_de_valores = 0

    
		valor_auxiliar = 0
		contador_norma = orden
		for contador_resultados in range(orden):
			valor_auxiliar = valor_auxiliar + (Matriz_Resultados[contador_norma]-Matriz_Resultados[contador_norma-orden])**2
			contador_norma = contador_norma + 1
			Norma_Resultados_Matrices = math.sqrt(valor_auxiliar)
		iteracion_principal = iteracion_principal + 1
		Contador_Externo = orden
		print("*----------------------------------------------------------*")
		print("|  Numero de la Iteracion = ",iteracion_principal, "  |")
		orden = int(orden)
		for contador_resultados in range(orden):
			print("X",contador_resultados+1,"  = ","%.4f" %Matriz_Resultados[Contador_Externo])
			Contador_Externo = Contador_Externo + 1
		print("|  Grado de error = ","%.4f" %Norma_Resultados_Matrices)
		print("*----------------------------------------------------------*")
		Contador_Externo = orden
		for cambio_posicion in range(orden):
			Matriz_Resultados[cambio_posicion] = Matriz_Resultados[cambio_posicion+orden]


#                                       Funcion Principal
#----------------------------------------------------------------------------------------------------------#

def funcion_principal_Metodos(orden, lista):

	orden = int(orden)
	orden_total = orden*orden
	orden_total = int(orden_total)
	matriz_aux = []
	Matriz_C = [] # Matriz que contiene los resultados.
	resultado = 0
	# buckets = [[0 for col in range(orden)] for row in range(orden)]
	# print(buckets)
	condicion = 0
	Matriz_A = [[0 for col in range(orden)] for row in range(orden)] # Matriz de la diagonal y ceros el resto
	Matriz_B = [[0 for col in range(orden)] for row in range(orden)] # Matriz de la diagonal llena de ceros y el resto los valores correspondientes
	Matriz_Resultados = [0 for col in range(1) for row in range(orden*2)]
	for Contador_Principal in range(orden*2):
		Matriz_Resultados[Contador_Principal] = float(Matriz_Resultados[Contador_Principal])

	Matriz_A = Matriz_Diagonal(Matriz_A, orden, lista)
	Matriz_B = Matriz_DiagonalCero(Matriz_B, orden, lista)
	Matriz_C = Matriz_resultadosMatriz(Matriz_C, orden, lista)

	for Contador_Principal in range(orden):
		for Contador_Secundario in range(orden):
			resultado = resultado + abs(Matriz_B[Contador_Principal][Contador_Secundario])
		if abs(Matriz_A[Contador_Principal][Contador_Principal]) > resultado:
			condicion = condicion + 1
			resultado = 0

	if condicion == orden:
		print("|  La matriz cumple con las condiciones necesarias  |")

		print(" ")
		print("****************************************************")
		print("*      Ingrese una de las siguientes opciones:     *")
		print("****************************************************")
		print("* Metodo Gauss Jacobi  ---> [1]                    *")
		print("* Metodo Gauss Seidel  ---> [2]                    *")
		print("****************************************************")
		print(" ")

		salir = 0
		while salir != 1:
			metodo = int(input("| Opcion | = "))


			if metodo == 1:
				metodo_Jacobi(Matriz_A,Matriz_B,Matriz_C,Matriz_Resultados,orden)
				salir = 1
			elif metodo == 2:
				metodo_Seidel(Matriz_A,Matriz_B,Matriz_C,Matriz_Resultados,orden)
				salir = 1
			else:
				print(" ")
				print("****************************************************")
				print("*   Ingrese una opcion valida     |ERROR|          *")                    
				print("****************************************************")
				print(" ")
	else:
		print(" ")
		print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
		print("x  La matriz no cumple con las condiciones necesarias                                                       x")
		print("x  Porfavor, cambie manualmente los valores de la matriz para que cumpla con los requisitos  |aii| > |aij|  x ")
		print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
		print(" ")
	print(" ")
	print(" ")
	print("              ***********************************************************")
	print("              *                   PROGRAMA FINALIZADO                   *")                
	print("              *                   PROCESOS ITERATIVOS                   *")
	print("              ***********************************************************")


#----------------------------------------------------------------------------------------------------------------------------------------#


def Programa_Matrices_Algebra():

	print("              ***********************************************************")
	print("              *                   PROGRAMA DE ALGEBRA                   *")                
	print("              *                   PROCESOS ITERATIVOS                   *")
	print("              ***********************************************************")
	print(" ")
	print("| Version 2.0 |")
	print(" ")
	orden = int(input("| Ingrese el orden de la matriz | = "))
	Archivo= open("Matrices.txt", "r",encoding = 'utf-8')
	lines = Archivo.read()
	lista = lines.split()
	Archivo.close()

	if (orden)*(orden)+orden == len(lista):
		print("|----------------------------------------------------|")
		print("| Se enviaran los datos a la funcion correspondiente |")
		print("|----------------------------------------------------|")

		print(" ")
		continuar = input("\n | Presione ENTER para continuar con el prograama |")
		print(" ")
		print(" ")
		funcion_principal_Metodos(orden, lista)
	else:
		print("|-------------------------------------------------------------------------------------|")
		print("| El orden de la matriz que acaba de ingresar, no coincide con los datos del archivo. |")
		print("| Porfavor vuelva a intentarlo con un ingreso que corresponda o bien que los datos    |")
		print("| del archivo esten bien definidos.                                                   |")
		print("|-------------------------------------------------------------------------------------|")
		print(" ")
		print(" ")
		print("              ***********************************************************")
		print("              *                   PROGRAMA FINALIZADO                   *")                
		print("              *                   PROCESOS ITERATIVOS                   *")
		print("              ***********************************************************")

    
Programa_Matrices_Algebra()
