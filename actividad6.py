#DAVID SEIJAS PEREZ
#problema 7.10

#importar modular de Notas
import modular as mod
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

#Funcion para calcular a^B!
def potenciaRara(a, B, N):      
    i = 1
    pot = a
    while i <= B:  
        pot = mod.potencia_mod(pot, i, N)  
        i += 1     
    return pot
#En este bucle lo que vamos haciendo es a, a^2, (a^2)^3(, (a^2)^3)^4,... hasta B!
#En cada iteracion elevamos lo que tenemos calculado de la anterio al siguiente numero
#Calculamos con potencia modular para cuando elevemos lo que llevamos calculado a un numero muy grande

#Funcion que dado un N y un B hace la factorizacion p-1 Pollard de N con primos <= B
def pollard(N, B):
    a = random.randint(1, N-1)
    x = gcd_binario(a, N)                            #Si x no es 1, es p y q y ya hemos encontrado un factor. El otro viene de dividir N por este
    if x != 1:
        return (x, N//x)
    y = gcd_binario(potenciaRara(a, B, N) - 1, N)    #Si x era 1 hay que calcular el gcd(a^B! - 1, N)
    if y != 1 and y != N:                            #Si y no es un numero trivial ya hemos encontrado un factor
        return (y, N//y)
        
        
N = 1542201487980564464479858919567403438179217763219681634914787749213
B = 100
print(pollard(N, B))