# Set de problema Torres de Hanoi
# Problema: Porcentaje de segunda nota de semestre.
# Lenguaje y Tecnicas de Programacion
# Profesor: Igor Caracci
# Profesor(Ayudante): Andres Caro
# Alumnos: Ana Karina Alvarez Ojeda, Nicolás Fernando Pérez Poblete.
# Universidad de Santiago de Chile
# 15 de Agosto del 2013
#
# Descripcion: Tenemos el codigo de las torres de hanoi, y con nuestros conocimientos debemos
# traspasar la recursividad de este a iterativo y posteriormente el codigo final adaptarlo
# a Python.
# 
#
#------------------------------------------------------------------------------------------------------------------------------------------------------ 
#
#
#
#                               PROGRAMA ADAPTADO A LENGUAJE PYTHON.



def Torres_Hanoi(n, origen, destino, auxiliar): # Funcion Torres 
    
    a = [] # Lista en donde se guardaran todos los datos de los movimientos que realizara el programa.
    cantidad_movimientos = 0
    n_aux = n # variable auxiliar que guarda la cantidad de discos inicial.

    while n > 1: # Primer ciclo while que reemplaza a la primera llamada recursiva del codigo de las torres de hanoi, mientras la cantidad de discos sea mayor a 1.
        
        a.append([n, origen, destino, auxiliar]) # El append() se encarga de guardar en el ultimo espacio de la lista datos que se requieran, en este caso guardamos una lista dentro de otra lista.

        n = n-1;                # Operaciones simples que solo van modificando los valores predeterminados mediante el ciclo,
        aux2 = destino          # aunque vallan siendo modificados el registro queda al inicio del ciclo while, por lo tanto
        destino = auxiliar      # los datos quedan registrados y no se pierden.
        auxiliar = aux2         #
        origen = origen         #
     
    if n > 0:  # esto es para que si la cantidad de discos en 0 el contador no sume de a 1 y la cantidad de movimientos final sea 0.
        print(" Mover disco de la Torre", origen," a la Torre", destino) # Primer imprimir de movimiento, indicara en pantalla cual es el movimiento inicial.
        cantidad_movimientos = cantidad_movimientos + 1
    else:
        print("No se encontro ningun disco en las torres.")
    

    aux = len(a)  # El comando len() es para saber el largo de la lista, como son puras listas dentro de la principal, contará cuantas listas hay dentro de nuestra lista a.
    
    while aux > 0: # Segundo ciclo que depende de la cantidad de listas dentro de nuestra lista principal, el valor sera modificado mediante el ciclo y se saldra cuando ya todos los movimientos sean realizados. 
        
        n,origen,destino,auxiliar = a.pop() # El comando pop() nos sirve para darle el ultimo valor de la lista a las variables que ocupemos, al momento de hacerlo asigna valores y elmimina los ultimos datos de la lista ya que no los ocuparemos.
        
        print(" Mover disco de la Torre", origen," a la Torre", destino) # Segundo imprimir  de movimientos que mostrara movimientos en mayor cantidad que el primero.
        cantidad_movimientos = cantidad_movimientos + 1

        n = n-1             # Operaciones simples que solo van modificando los valores predeterminados mediante el ciclo.
        aux2 = origen       # Estos valores son los que sacamos de nuestra lista principal y ahora los modificamos cambiando
        origen = auxiliar   # las pociciones de algunos.
        auxiliar = aux2     #
        destino = destino     #
        
   
        while n > 1: # Tercer y ultimo ciclo while que hace modificaciones de valores y registra estos en nuestra lista principal.
            
            a.append([n, origen, destino, auxiliar])  # El append() se encarga de guardar en el ultimo espacio de la lista datos que se requieran, en este caso guardamos una lista dentro de otra lista.

            n = n - 1            # Operaciones simples que solo van modificando los valores predeterminados mediante el ciclo,
            aux2 = destino       # aunque vallan siendo modificados el registro queda al inicio del ciclo while, por lo tanto
            destino = auxiliar   # los datos quedan registrados y no se pierden.
            auxiliar = aux2      #
            origen = origen      #

        aux = len(a)  # aux en este momento toma el valor de un largo de lista modificado por este ultimo ciclo while.

        print(" Mover disco de la Torre", origen," a la Torre", destino)  # Ultimo imprimir movimientos que hace la misma cantidad de ellos que el segundo.
        cantidad_movimientos = cantidad_movimientos + 1
    print(" ")
    print("La cantidad de movimientos finales con ",n_aux , " disco(s) es:  ",cantidad_movimientos)  # La cantidad de movimientos sera : (2^(cantidad de discos)) - 1


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
# La funcion main() es para darle mas interaccion al algoritmo. La funcion Torres_Hanoi() por separada tambien funciona perfectamente.
#
#


def main(): # Funcion secundaria que muestra todas las opciones de uso del programa.

    print("*********************************************")   #
    print("Bienvenido al programa de Las Torres de Hanoi")   #
    print("*********************************************")   #     Inicio del programa.
    print("")                                                #
    print("")                                                #

    cont = 0   # ambas variables utilizadas como restriccion para que las opciones ingresadas sean correctas.
    cont2 = 0  # al momento de que estos valores sean modificados sera por que las opciones ingresadas son aceptadas.

    while cont != 1:         # Ciclo que se encarga de mantener el programa en funcionamiento hasta que el usuario lo desee.
        print("ADVERTENCIA: Ingresar solo numeros enteros cuando se pida la cantidad de discos, el ingreso de letras u otro caracter significara el final del programa.")
        print("")
        print("")
        Variable = int(input("Ingrese la cantidad de DISCOS que desee que el programa utilice.")) # Variable sera la cantidad de discos ingresada por el usuario, si es una letra o un numero negativo el programa no funcionara.
        cont2 = 0  # Esta variable esta encargada de hacer que vuelva a funcionar el programa si el usuario ingresa las opciones correspondientes.
        if ( Variable > 0 ):
            Torres_Hanoi(Variable,1,3,2) # Llamada a la funcion principal con la cantidad de discos que ingreso el usuario.
            print("") # Se salta un espacio.

            while cont2 != 1:
                palabra = str(input("¿ Desea volver a ocupar el programa ?     s / n")) # Opcion que da la posibilidad de volver a ocupar el programa.

                if palabra == 'n' or palabra =='s':  # si la opcion ingresada pertenece a lo requerido.
                    if palabra == 'n':
                        cont = 1
                        cont2 = 1
                    else:
                        cont = 0
                        cont2 = 1
                else:
                    print("Ingrese las opciones correspondientes")
        else:
            if Variable == 0: # Si la cantidad de discos ingresada es 0, la cantidad de movimientos es 0 tambien.
                print ("Las torres no contienen ningun disco, por lo tanto la cantidad de movimientos es 0. ")
                while cont2 != 1:
                    palabra = str(input("¿ Desea volver a ocupar el programa ?     s / n")) # Opcion que da la posibilidad de volver a ocupar el programa.

                    if palabra == 'n' or palabra =='s':
                        if palabra == 'n':
                            cont = 1
                            cont2 = 1
                        else:
                            cont = 0
                            cont2 = 1
                    else:
                        print("Ingrese las opciones correspondientes")
            else:
                print("Ingrese un numero adecuado a las opciones porfavor.")
                print("")

    print("")
    print("Ejecución finalizada.")
    print("")
    print("*****************************************")
    print("Gracias por utilizar el programa, Goodbye")
    print("*****************************************")
    
 
#
#
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#

main()
# Final del programa.
