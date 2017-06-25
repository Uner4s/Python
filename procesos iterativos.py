import math
import os
def diagonal_pesada(matriz, rango,):
    respaldo=[]

    #Comprobar si cumple con las condiciones de la matriz pesada
    for i in range(int(rango)):
       respaldo=matriz[i][:] #Respaldo de columna de matri
       respaldo.pop(i)
       suma=0
       for elemento in respaldo:
           if abs(elemento) >= abs(matriz[i][i]):
               return False
           suma = suma + abs(elemento)

       if suma >= abs(matriz[i][i]):
           return False
    return True


def jacobi(matriz,resultados,rango,error):
    iteracion_anterior=[]
    iteracion_siguiente=[]

    respaldo_matriz=[]
    respaldo_diagonal=[]
    
    columna=[]

    #Matriz con la diagonal nula 
    for i in range(int(rango)):
        columna=matriz[i][:]
        respaldo_diagonal.append(columna[i])
        columna[i]=0
        respaldo_matriz.append(columna)

    
    

    #Iteracion 1:
    for i in range(int(rango)):
        iteracion_anterior.append(resultados[i]/matriz[i][i])

    #error=input("Ingrese el rango de error que desea para la solucion: ")
    parar=False
    numero_iteracion=2
    while not parar:
       
        for i in range(int(rango)):
            suma=0
            for j in range(int(rango)):
                suma=suma+(respaldo_matriz[i][j]*iteracion_anterior[j])
            resultado=(resultados[i]-suma)/respaldo_diagonal[i]
            iteracion_siguiente.append(resultado)

        #Calcular distancia entre iteraciones
        aux = 0
        for i in range(int(rango)):
            aux = aux + (iteracion_siguiente[i]-iteracion_anterior[i])**2

        distancia = math.sqrt(aux)
        print("Iteracion:",numero_iteracion,"Distancia:",distancia)

        #Si la distancia es menor o igual al rango de error aceptado
        if distancia <= float(error):
            parar = True #Se detiene el proceso
        #Caso contrario, se continua con el proceso
        else:
            iteracion_anterior=iteracion_siguiente[:]
            iteracion_siguiente[:]=[]
            numero_iteracion=numero_iteracion+1


def seidel(matriz,resultados,rango,error):
    iteracion_anterior=[]
    iteracion_siguiente=[]

    respaldo_matriz=[]
    respaldo_diagonal=[]
    
    columna=[]

    #Matriz con la diagonal nula 
    for i in range(int(rango)):
        columna=matriz[i][:]
        respaldo_diagonal.append(columna[i])
        columna[i]=0
        respaldo_matriz.append(columna)

    
    

    #Iteracion 1:
    for i in range(int(rango)):
        iteracion_anterior.append(resultados[i]/matriz[i][i])

    #error=input("Ingrese el rango de error que desea para la solucion: ")
    parar=False
    numero_iteracion=2
    while not parar:
       
        for i in range(int(rango)):
            suma=0
            for j in range(int(rango)):
                if j<len(iteracion_siguiente):
                    suma=suma+(respaldo_matriz[i][j]*iteracion_siguiente[j])
                else:
                    suma=suma+(respaldo_matriz[i][j]*iteracion_anterior[j])
            resultado=(resultados[i]-suma)/respaldo_diagonal[i]
            iteracion_siguiente.append(resultado)

        #Calcular distancia entre iteraciones
        aux = 0
        for i in range(int(rango)):
            aux = aux + (iteracion_siguiente[i]-iteracion_anterior[i])**2

        distancia = math.sqrt(aux)
        print("Iteracion:",numero_iteracion,"Distancia:",distancia)

        #Si la distancia es menor o igual al rango de error aceptado
        if distancia <= float(error):
            parar = True #Se detiene el proceso
        #Caso contrario, se continua con el proceso
        else:
            iteracion_anterior=iteracion_siguiente[:]
            iteracion_siguiente[:]=[]
            numero_iteracion=numero_iteracion+1    


def seidel2(matriz,resultados,rango,iteraciones,error):
    iteracion_anterior=[]
    iteracion_siguiente=[]

    respaldo_matriz=[]
    respaldo_diagonal=[]
    
    columna=[]

    #Matriz con la diagonal nula 
    for i in range(int(rango)):
        columna=matriz[i][:]
        respaldo_diagonal.append(columna[i])
        columna[i]=0
        respaldo_matriz.append(columna)

    
    

    #Iteracion 1:
    for i in range(int(rango)):
        iteracion_anterior.append(resultados[i]/matriz[i][i])

    #error=input("Ingrese el rango de error que desea para la solucion: ")
    parar=False
    max_iter = False
    numero_iteracion=2
    iteraciones = iteraciones - 2
    while not parar and not max_iter:
       
        for i in range(int(rango)):
            suma=0
            for j in range(int(rango)):
                if j<len(iteracion_siguiente):
                    suma=suma+(respaldo_matriz[i][j]*iteracion_siguiente[j])
                else:
                    suma=suma+(respaldo_matriz[i][j]*iteracion_anterior[j])
            resultado=(resultados[i]-suma)/respaldo_diagonal[i]
            iteracion_siguiente.append(resultado)

        #Calcular distancia entre iteraciones
        aux = 0
        for i in range(int(rango)):
            aux = aux + (iteracion_siguiente[i]-iteracion_anterior[i])**2

        distancia = math.sqrt(aux)
        print("Iteracion:",numero_iteracion,"Distancia:",distancia)

        #Si la distancia es menor o igual al rango de error aceptado
        if distancia <= float(error):
            parar = True #Se detiene el proceso
        #Caso contrario, se continua con el proceso
        elif iteraciones == 0:
            max_iter = True
        else:
            iteracion_anterior=iteracion_siguiente[:]
            iteracion_siguiente[:]=[]
            numero_iteracion=numero_iteracion+1    

        iteraciones = iteraciones-1
    if parar == False:
        print("No se pudo encontrar aproximacion con el numero de iteraciones dadas")

def jacobi2(matriz,resultados,rango,iteraciones,error):
    iteracion_anterior=[]
    iteracion_siguiente=[]

    respaldo_matriz=[]
    respaldo_diagonal=[]
    
    columna=[]

    #Matriz con la diagonal nula 
    for i in range(int(rango)):
        columna=matriz[i][:]
        respaldo_diagonal.append(columna[i])
        columna[i]=0
        respaldo_matriz.append(columna)

    
    

    #Iteracion 1:
    for i in range(int(rango)):
        iteracion_anterior.append(resultados[i]/matriz[i][i])

    #error=input("Ingrese el rango de error que desea para la solucion: ")
    parar=False
    max_iter = False
    numero_iteracion=2
    iteraciones = iteraciones - 2
    while not parar and not max_iter:
       
        for i in range(int(rango)):
            suma=0
            for j in range(int(rango)):
                suma=suma+(respaldo_matriz[i][j]*iteracion_anterior[j])
            resultado=(resultados[i]-suma)/respaldo_diagonal[i]
            iteracion_siguiente.append(resultado)

        #Calcular distancia entre iteraciones
        aux = 0
        for i in range(int(rango)):
            aux = aux + (iteracion_siguiente[i]-iteracion_anterior[i])**2

        distancia = math.sqrt(aux)
        print("Iteracion:",numero_iteracion,"Distancia:",distancia)

        #Si la distancia es menor o igual al rango de error aceptado
        if distancia <= float(error):
            parar = True #Se detiene el proceso
        elif iteraciones == 0:
            max_iter = True
        #Caso contrario, se continua con el proceso
        else:
            iteracion_anterior=iteracion_siguiente[:]
            iteracion_siguiente[:]=[]
            numero_iteracion=numero_iteracion+1

        iteraciones=iteraciones-1
    if parar == False:
        print("No se pudo encontrar aproximacion con el numero de iteraciones dadas")
 



nombre = input("Ingrese el nombre del archivo: ")
archivo = open(nombre,'r')
rango = archivo.readline(); #Recibe el rango de la matriz
matriz = [[0 for i in range(int(rango))]for j in range(int(rango))] #Crea matriz nula del rango dado

#Llenado de Marriz
i=0
resultados=[]
for linea in archivo: #Se recibe una fila de valores completa desde el archivo de texto
    linea=linea.split() #Los elementos se separan en un vector
    for j in range(int(rango)+1): #Se recorre la matriz para colocar los valores correspondientes
        if j == int(rango): 
            resultados.append(int(linea[j])) #Los resultados se guardan en un vector aparte
        else:
            matriz[i][j]=int(linea[j])
    i=i+1

validez = diagonal_pesada(matriz,rango)
if validez == False:
    print("La matriz no cumple con los requerimientos de la diagonal pesada.")
    while True:
        opcion=input("¿Desea ejecutar los procesos de todos modos? S/N ")
        if opcion == 'S' or opcion == 'N' or opcion =='s' or opcion == 'n':
          break;
        else:
          print("Opcion invalida, ingrese la opcion nuevamente ")
    if opcion == 'S' or opcion == 's':
        iteraciones = input("Ingrese el numero de iteraciones que desea realizar ")
        iteraciones = int(iteraciones)
        error = input("Ingrese el rango de error ")
        error = float(error)
        print("Jacobi")
        jacobi2(matriz,resultados,rango,iteraciones,error)
        print("\nSeidel")
        seidel2(matriz,resultados,rango,iteraciones,error)

else:
    error = input("Ingrese el rango de error ")
    error = float(error)
    print("Jacobi")
    jacobi(matriz,resultados,rango,error)
    print("\nSeidel")
    seidel(matriz,resultados,rango,error)

pause = input("\nPresione ENTER para finalizar")
