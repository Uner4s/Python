# AUTOR: 
# FECHA: 
# VERSIÓN: 1.0


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


def funcion_principal ():

	#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
	os.system('clear')
	print("")
	print("     |--------------------------------------------------------------|")
	print("     |                      Programa Iniciado                       |")
	print("     |--------------------------------------------------------------|")
	print(" ")


	# En este caso, el programa estara definido para resolver el siguiente problema:
	# Se quiere saber si existe relacion entre el genero y la tasa de infidelidad de
	# las personas, comparando respuestas de que si han sido infieles alguna vez.
	#
	# Infieles:     Si      No
	# Hombres :      5      40 
	# Mujeres :     50      10 
	#
	#

	print(" ")
	print(" ")
	variable1 = int(input(" | Ingrese el primer valor numerico  | --->  ")) # Pide el primer valor numerico.
	variable2 = int(input(" | Ingrese el segundo valor numerico | --->  ")) # Pide el segundo valor numerico.
	variable3 = int(input(" | Ingrese el tercer valor numerico  | --->  ")) # Pide el tercer valor numerico.
	variable4 = int(input(" | Ingrese el cuarto valor numerico  | --->  ")) # Pide el cuarto valor numerico. 

	total1 = variable1 + variable2 # En estas operaciones se sacan 4 valores de las sumas de las variablesingresadas  y el valor del total.
	total2 = variable3 + variable4
	total3 = variable1 + variable3
	total4 = variable2 + variable4
	
	comprobar1 = total1 + total2
	comprobar2 = total3 + total4 

	if ( comprobar1 == comprobar2 ):

		total_final = comprobar1

	var = input("Presione ENTER para continuar...")  
	os.system('clear')
	#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
	print("")
	print("     |--------------------------------------------------------------|")
	print("     |                        Tabla principal.                      |") # Aca se muestra la tabla principal, las variables que se estan comparando y los valores.
	print("     |--------------------------------------------------------------|")
	print(" ")

	# G = Genero ( Masculino, Femenino), en este caso Hombre y Mujer
	# I = Infidelidad.

	print("     |--------------------------------------------------------------|") 
	print("     |   G / I   |        SI         NO             TOTAL  ")
	print("     |--------------------------------------------------------------|")
	print("     |     H     |       ", variable1,"       ", variable2,"            ",total1)
	print("     |--------------------------------------------------------------|")
	print("     |     M     |       ", variable3,"       ", variable4,"            ",total2)
	print("     |--------------------------------------------------------------|")
	print("     |   TOTAL   |       ", total3,"       ",total4,"            ",total_final)
	print("     |--------------------------------------------------------------|")
	print(" ")
	print(" ")
	var = input("Presione ENTER para continuar...")# Este es para pausar el programa y para que se vea mas ordenado la secuencia de solucion.
	#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
	print("")
	os.system('clear')
	print("      |--------------------------------------------------------------|")
	print("      |                         Tabla esperada.                      |") # Aca se muestra la tabla esperada con las operaciones correspondientes.
	print("      |--------------------------------------------------------------|")
	print(" ")
	resultado1 = (total1*total3)/total_final
	resultado2 = (total1*total4)/total_final # Aca se realizan las operaciones.
	resultado3 = (total2*total3)/total_final
	resultado4 = (total2*total4)/total_final

	print("|---------------------------------------------------------------------------|") # Aca se muestran las operaciones y la tabla.
	print("|                                                                           |")
	print("|  (",total1,"*",total3,")/",total_final," = ","%.4f" %resultado1,"           ","(",total1,"*",total4,")/",total_final," = ","%.4f" %resultado2)
	print("|                                                                           |")	
	print("|---------------------------------------------------------------------------|")
	print("|                                                                           |")	
	print("|  (",total2,"*",total3,")/",total_final," = ","%.4f" %resultado3,"           ","(",total2,"*",total4,")/",total_final," = ","%.4f" %resultado4)
	print("|                                                                           |")	
	print("|---------------------------------------------------------------------------|")
	print(" ")
	print(" ")
	var = input("Presione  ENTER continuar...") # Este es para pausar el programa y para que se vea mas ordenado la secuencia de solucion.
	#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
	print(" ")
	os.system('clear') # Este comando limpia la pantalla para que se vea mas ordenado.
	print(" ")

	# Aca se muestra el X sub c al cuadrado, toda la operacion correspondiente.
	Xc2 = (((variable1 - resultado1)**2)/(resultado1) + ((variable2 - resultado2)**2)/(resultado2) + ((variable3 - resultado3)**2)/(resultado3) + ((variable4 - resultado4)**2)/(resultado4))
	print("(Xc)^2 :  ((",variable1," - ","%.4f" %resultado1,")^2)/","%.4f" %resultado1," + ","((",variable2," - ","%.4f" %resultado2,")^2)/","%.4f" %resultado2," + ","((",variable3," - ","%.4f" %resultado3,")^2)/","%.4f" %resultado3," + ","((",variable4," - ","%.4f" %resultado4,")^2)/","%.4f" %resultado4, "  =  ","%.4f" %Xc2)
	print(" ")
	print("|-------------------------------|")
	print("|       (Xc)^2 : ","%.4f" %Xc2)		# Muestra por pantalla el resultado correspondiente.
	print("|-------------------------------|")
	print(" ")
	var = input("Presione ENTER continuar...") # Este es para pausar el programa y para que se vea mas ordenado la secuencia de solucion.
	#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
	print("")
	os.system('clear')
	print("              ***********************************************************")
	print("              *                         Coeficiente                     *") # Aca se muestra el coeficiente de contingencia.
	print("              *                       de contingencia                   *")
	print("              ***********************************************************")

	print(" ")
	C = (Xc2/(Xc2 + total_final))**0.5 # Se hace la operacion para sacar el coeficiente correspondiente
	print("( (","%.4f" %Xc2,") / (","%.4f" %Xc2," + ",total_final,") ) ^ 0.5   =  ","%.4f" %C) # Muestra por pantalla las operaciones correspondientes para el coeficiente de contingencia.
	print(" ")
	print("|-----------------------------------------|")
	print("|   Coeficiente de Contingencia: ", "%.4f" %C)
	print("|-----------------------------------------|")
	print("")
	var = input("Presione ENTER para continuar...") # Este es para pausar el programa y para que se vea mas ordenado la secuencia de solucion.
	#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
	print("")
	os.system('clear')
	print("              ***********************************************************")
	print("              *                        Porcentaje de                    *") # Muestra el porcentaje de asociacion. 
	print("              *                         Asociacion                      *")
	print("              ***********************************************************")
	print("")
	Porcentaje_Asociacion = C * 100
	print("PA  =  ", "%.4f" %C," * 100") # muestra por pantalla la operacion.
	print("|----------------------------------------|")
	print("|             PA : ", "%.4f" %Porcentaje_Asociacion,"%") # Muestra por pantalla el resultado.
	print("|----------------------------------------|")
	print(" ")
	print("Hay un ","%.4f" %Porcentaje_Asociacion,"%  de asociacion")
	var = input("Presione ENTER para continuar...") # Este es para pausar el programa y para que se vea mas ordenado la secuencia de solucion.
	os.system('clear')
	print("")
	print("     |--------------------------------------------------------------|")
	print("     |                      Programa Finalizado                     |") # Menu de adios, cuando el programa ha terminado su trabajo.
	print("     |--------------------------------------------------------------|")
	print(" ")


	# os.system('clear')

funcion_principal ()
