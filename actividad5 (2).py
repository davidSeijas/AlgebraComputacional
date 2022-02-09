#DAVID SEIJAS PEREZ
#problema 6.6

#importar modular de Notas
import modular as mod

#Funcion para ver el gcd de dos numeros y poder ver si son coprimos o no
def gcd(a, b) :
    if (a < b) :
        a, b = b, a
    if (a % b == 0) :
        return b
    return gcd(b, a % b)

#Funcion para ver si un numero es primo o compuesto
def isPrimo(n):
    d = 2
    while d*d <= n:
        if n % d == 0:
           return False
        d += 1
    return True

#Funcion que me saca la lista de los coprimos de un numero
def coprimos(n):
    coprimos = []
    for i in range(2, n):
        if gcd(i, n) == 1:
            coprimos.append(i)
    return coprimos

#Funcion que me saca los n primeros numeros de Carmichael
def carmichael(n):      
    cont = 0            #cont lleva la cuenta del nº de numeros que ya he encontrado
    N = 2
    carmichael = []     #guardamos los numeros en una lista para lueo mostrarla
    
    while cont < n:     #en el bucle recorremos todos los números (que sean compuestos) y avanzamos cont cuando encontramos uno de carmichael
        esCarmichael = True
        if isPrimo(N) is False:
            cop = coprimos(N)    #me devuelve una lisa con los coprimos de N
            
            for i in range(0, len(cop)):
                if (mod.potencia_mod(cop[i], N-1, N) != 1):
                    esCarmichael = False           #tenemos que ver que para todos sus coprimos se cumple que a^N-1 = a 1 mod N
            
            if esCarmichael is True:                #si para todos se ha cumplido, la variable sera true pues si no la hubiesemos hecho False y añadimos ese numero de Carmichael a la lista
                carmichael.append(N)
                cont += 1
        
        N += 1
        
    return carmichael

print(carmichael(10))

#NO TERMINA O TARDA DEMASIADO!!