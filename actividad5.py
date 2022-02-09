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


#Funcion que me dice si un numero es Carmichael o no
def isCarmichaelNumber(n):   
    b = 2
    while b < n:
        if (gcd(b, n) == 1): #Si son coprimos
            if (mod.potencia_mod(b, n-1, n) != 1):  #Si alguno de los coprimos no cumple la propiedad no es Carmichael
                return False
        b = b + 1
    return True   #Si llegamos aqui es que todos los coprimos han cumplido la propiedad y es Carmichael
 
#Recorro todos los numeros COMPUESTOS y cada vez que encuentro uno de carmichael 
#aumento cont y lo imprimo. Parare cuando haya encontrado los 10 que queriamos
cont = 0
x = 2
while cont < 10:
    if not(isPrimo(x)) and isCarmichaelNumber(x):
        print(x)
        cont += 1
    x += 1
    
#TERMINA EN SEGUNDOS!!