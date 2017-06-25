from operator import itemgetter
from math import *


def matriz_2x2(lista):


    porcentaje_error = 0.0001
    iteraciones = 0
    norma = 10.0000

    X1 = 0.0000
    Y1 = 0.0000
    X2 = 0.0000
    Y2 = 0.0000

    print("%.4f" %porcentaje_error)
    
    a11 = lista[0]
    a12 = lista[1]
    b1  = lista[2]
    a21 = lista[3]
    a22 = lista[4]
    b2  = lista[5]

    a11 = float(a11)
    a12 = float(a12)
    b1  = float(b1)
    a21 = float(a21)
    a22 = float(a22)
    b2  = float(b2)

    condicion1 =  0

    print("Primero se comprobara la condicion [  |a11| > |a12|  y  |a22| > |a21|  ]")

    if abs(a11) > abs(a12) and abs(a22) > abs(a21):
        print("Bien! , la matriz cumple la condicion.")
        print("")
        print("")
        condicion1 = condicion1 + 1
    else:
        print("Lamentablemente la matriz del archivo no cumple con las condiciones requeridas")
        print("Porfavor intente mas tarde con una matriz valida")


    if condicion1 == 1:
        
        while porcentaje_error <= norma:
            if iteraciones == 0:
                print("[ X: 0.0000","  Y: 0.0000","  NORMA:   NULA      ESTADO:           Error      ITERACION:",iteraciones,"]")
                iteraciones = iteraciones + 1
            else:
                X2 =float((b1-(a12*Y1))/a11)
                if X2 == -0:
                    X2 = abs(X2)
                Y2 =float((b2-(a21*X2))/a22)
                
                if Y2 == -0:
                    Y2 = abs(Y2)


                norma = sqrt((X2-X1)*(X2-X1)+(Y2-Y1)*(Y2-Y1))
                
                if norma <= porcentaje_error:
                    estado = 'Terminado'
                else:
                    estado = 'Error'

                print("[ X:","%.4f" %X2,"  Y:","%.4f" %Y2,"  NORMA:","%.4f" %norma,"     ESTADO:          ",estado,"     ITERACION:",iteraciones,"]")
                
                X1 = X2
                Y1 = Y2

                iteraciones = iteraciones + 1


def matriz_3x3(lista):



    porcentaje_error = 0.0001
    iteraciones = 0
    norma = 10.0000

    X1 = 0.0000
    Y1 = 0.0000
    Z1 = 0.0000
    X2 = 0.0000
    Y2 = 0.0000
    Z2 = 0.0000

    print("%.4f" %porcentaje_error)
    
    a11 = lista[0]
    a12 = lista[1]
    a13 = lista[2]
    b1  = lista[3]
    a21 = lista[4]
    a22 = lista[5]
    a23 = lista[6]
    b2  = lista[7]
    a31 = lista[8]
    a32 = lista[9]
    a33 = lista[10]
    b3  = lista[11]

    a11 = float(a11)
    a12 = float(a12)
    a13 = float(a13)
    b1  = float(b1)
    a21 = float(a21)
    a22 = float(a22)
    a23 = float(a23)
    b2  = float(b2)
    a31 = float(a31)
    a32 = float(a32)
    a33 = float(a33)
    b3  = float(b3)


    condicion1 =  0

    print("Primero se comprobara la condicion [  |a11| > |a12| + |a13|  ,  |a22| > |a21| + |a23| ,  |a33| > |a31| + |a32| ]")

    if abs(a11) > abs(a12)+abs(a13) and abs(a22) > abs(a21)+abs(a23) and abs(a33) > abs(a31)+abs(a32):
        print("Bien! , la matriz cumple la condicion.")
        print("")
        print("")
        condicion1 = condicion1 + 1
    else:
        print("Lamentablemente la matriz del archivo no cumple con las condiciones requeridas")
        print("Porfavor intente mas tarde con una matriz valida")


    if condicion1 == 1:
        
        while porcentaje_error <= norma:
            if iteraciones == 0:
                print("[ X: 0.0000","   Y: 0.0000","   Z: 0.0000","   NORMA:   NULA       ESTADO:           Error      ITERACION:",iteraciones,"]")
                iteraciones = iteraciones + 1
            else:
                X2 = float((b1-(a12*Y1 + a13*Z1))/a11)
                if X2 == -0:
                    X2 = abs(X2)
                Y2 = float((b2-(a21*X2+a23*Z1))/a22)
                if Y2 == -0:
                    Y2 = abs(Y2)
                Z2 = float((b3-(a31*X2+a32*Y2))/a33)
                if Z2 == -0:
                    Z2 = abs(Z2)

                norma = sqrt((X2-X1)*(X2-X1)+(Y2-Y1)*(Y2-Y1)+(Z2-Z1)*(Z2-Z1))
                
                if norma <= porcentaje_error:
                    estado = 'Terminado'
                else:
                    estado = 'Error'

                print("[ X:","%.4f" %X2,"  Y:","%.4f" %Y2,"  Z:","%.4f" %Z2,"  NORMA:","%.5f" %norma,"     ESTADO:          ",estado,"     ITERACION:",iteraciones,"]")
                
                X1 = X2
                Y1 = Y2
                Z1 = Z2

                iteraciones = iteraciones + 1



def matriz_4x4(lista):



    porcentaje_error = 0.0001
    iteraciones = 0
    norma = 10.0000

    X1 = 0.0000
    Y1 = 0.0000
    W1 = 0.0000
    Z1 = 0.0000
    X2 = 0.0000
    Y2 = 0.0000
    W2 = 0.0000
    Z2 = 0.0000

    print("%.4f" %porcentaje_error)
    
    a11 = lista[0]
    a12 = lista[1]
    a13 = lista[2]
    a14 = lista[3]
    b1  = lista[4]
    a21 = lista[5]
    a22 = lista[6]
    a23 = lista[7]
    a24 = lista[8]
    b2  = lista[9]
    a31 = lista[10]
    a32 = lista[11]
    a33 = lista[12]
    a34 = lista[13]
    b3  = lista[14]
    a41 = lista[15]
    a42 = lista[16]
    a43 = lista[17]
    a44 = lista[18]
    b4  = lista[19]

    a11 = float(a11)
    a12 = float(a12)
    a13 = float(a13)
    a14 = float(a14)
    b1  = float(b1)
    a21 = float(a21)
    a22 = float(a22)
    a23 = float(a23)
    a24 = float(a24)
    b2  = float(b2)
    a31 = float(a31)
    a32 = float(a32)
    a33 = float(a33)
    a34 = float(a34)
    b3  = float(b3)
    a41 = float(a41)
    a42 = float(a42)
    a43 = float(a43)
    a44 = float(a44)
    b4  = float(b4)


    condicion1 =  0

    print("Primero se comprobara la condicion [  |a11| > |a12| + |a13|  ,  |a22| > |a21| + |a23| ,  |a33| > |a31| + |a32| ]")

    if abs(a11) >= abs(a12)+abs(a13)+abs(a14) and abs(a22) >= abs(a21)+abs(a23)+abs(a24) and abs(a33) >= abs(a31)+abs(a32)+abs(a34) and abs(a44) >= abs(a41)+abs(a42)+abs(a43):
        print("Bien! , la matriz cumple la condicion.")
        print("")
        print("")
        condicion1 = condicion1 + 1
    else:
        print("Lamentablemente la matriz del archivo no cumple con las condiciones requeridas")
        print("Porfavor intente mas tarde con una matriz valida")


    if condicion1 == 1:
        
        while porcentaje_error <= norma:
            if iteraciones == 0:
                print("[ X: 0.0000","   Y: 0.0000"," W: 0.0000","   Z: 0.0000","   NORMA:   NULA        ESTADO:           Error      ITERACION:",iteraciones,"]")
                iteraciones = iteraciones + 1
            else:
                X2 = float((b1-(a12*Y1 + a13*W1 + a14*Z1))/a11)
                if X2 == -0:
                    X2 = abs(X2)
                Y2 = float((b2-(a21*X2 + a23*W1 + a24*Z1))/a22)
                if Y2 == -0:
                    Y2 = abs(Y2)
                W2 = float((b3-(a31*X2 + a32*Y2 + a34*Z1))/a33)
                if W2 == -0:
                    W2 = abs(W2)
                Z2 = float((b4-(a41*X2 + a42*Y2 + a43*W2))/a44)
                if Z2 == -0:
                    Z2 = abs(Z2)


                norma = sqrt((X2-X1)*(X2-X1)+(Y2-Y1)*(Y2-Y1)+(W2-W1)*(W2-W1)+(Z2-Z1)*(Z2-Z1))
                
                if norma <= porcentaje_error:
                    estado = 'Terminado'
                else:
                    estado = 'Error'

                print("[ X:","%.4f" %X2,"  Y:","%.4f" %Y2,"  W:","%.4f" %W2,"  Z:","%.4f" %Z2,"  NORMA:","%.5f" %norma,"     ESTADO:          ",estado,"     ITERACION:",iteraciones,"]")
                
                X1 = X2
                Y1 = Y2
                W1 = W2
                Z1 = Z2

                iteraciones = iteraciones + 1

def Metodo_Seidel():

    f= open("prueba.txt", "r",encoding = 'utf-8')
    lines = f.read()
    lista = lines.split()

    H = 0
    while H == 0:

        # Aca debe ir un limpiador de pantalla.
        print("********* PROGRAMA DE GAUSS JACOBI *********")
        print("*****************************************")
        print("Ingrese una de la siguientes opciones:")
        print("Matriz de 2x2  -->  [2]")
        print("Matriz de 3x3  -->  [3]")
        print("Matriz de 4x4  -->  [4]")
        opcion = int(input("OPCION:  "))
        if opcion < 2 or opcion > 4:
            print("No se ha ingresado una opcion correcta, porfavor vuelva a intentarlo")
        else:
            print("OPCION INGRESADA CON EXITO")
            H = H + 1

    f.close()
    
    for a in lista:
        print(a)

    if opcion == 2:
        matriz_2x2(lista)
    if opcion == 3:
        matriz_3x3(lista)
    if opcion == 4:
        matriz_4x4(lista)



Metodo_Seidel()