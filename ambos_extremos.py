def ambos_extremos (n):
str(n)
largo = len(n)
    if largo >= 2 :
        resultado = n[0:2]+n[largo-2:largo]
        return resultado
    if largo < 2 :	
        return ""
