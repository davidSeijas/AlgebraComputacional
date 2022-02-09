#DAVID SEIJAS PEREZ
#problema 7.10

#importar modular de Notas
import modular as mod
import math
import random

#Funcion para ver el gcd de dos numeros 
def gcd_binario(x,y):    # (x,y) != (0,0)
    x = abs(x)
    y = abs(y)
    xespar = x%2 == 0
    yespar = y%2 == 0
    if x == 0:           # caso base: gcd(0,y)=y
        m = y
    elif y == 0:         # caso base: gcd(x,0)=x
        m = x
    elif xespar and yespar:
        m = 2 * gcd_binario(x//2, y//2)
    elif xespar:
        m = gcd_binario(x//2, y)
    elif yespar:
        m = gcd_binario(x, y//2)
    elif x > y:
        m = gcd_binario(y, x-y)
    else:
        m = gcd_binario(x, y-x)
    return m

#Funcion para ver si un numero es primo 
def isPrimo(n):
    d = 2
    while d*d <= n:
        if n % d == 0:
           return False
        d += 1
    return True

#Funcion para calcular betha
def  calculoBetha(N, B):
    x = 1
    p = 2
    #Aplicamos la formula de las notas para betha. Producto de los primos menores que B elevados al log_p(N)
    while p <= B:
        if isPrimo(p):
            x *= (p ** math.ceil(math.log(N, p)))   
        p += 1
    return x

#Funcion que devuelve los factores primos de un numero en una lista
def factorizar(a):
    factores = []
    p = 2
    aux = a
    while aux != 1:
        if isPrimo(p) and aux % p == 0:
            factores.append(p)
            aux //= p
        else:
            p += 1
    return factores

#Funcion para calcular a^betha mod N elevando cada vez a uno de sus factores y haciendo mod N
def potenciaRara(a, betha, N):
    factores = factorizar(betha)
    sol = a
    cont = 0
    #Para cada factor de betha, elevamos modulo N el resutlado acumulado a ese factor y volvemos a iterar para hacerlo con todos
    while cont < len(factores):
        sol = mod.potencia_mod(sol, factores[cont], N)
        cont += 1
    return sol      

#Funcion que dado un N y un B hace la factorizacion p-1 Pollard de N con primos <= B
def pollard(N, B):
    a = random.randint(1, N-1)
    betha = calculoBetha(N, B)
    x = gcd_binario(a, N)                                   #Si x no es 1, es p y q y ya hemos encontrado un factor. El otro viene de dividir N por este
    if x != 1:
        return (x, N//x)
    y = gcd_binario(potenciaRara(a, betha, N) - 1, N)       #Si x era 1 hay que calcular el gcd(a^B! - 1, N)
    if y != 1 and y != N:                                   #Si y no es un numero trivial ya hemos encontrado un factor
        return (y, N//y)
        
        
N = 1542201487980564464479858919567403438179217763219681634914787749213
B = 100
print(pollard(N, B))