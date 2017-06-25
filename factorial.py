def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n > 1:
        resultado = 1
        while n > 0 :
            resultado = resultado * n
            n = n-1      
        return resultado 
