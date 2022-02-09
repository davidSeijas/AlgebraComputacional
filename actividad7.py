#DAVID SEIJAS PEREZ
#problema 8.5

import random
import matplotlib.pyplot as plt

#Funcion para ver el gcd de dos numeros 
def gcd(a, b) :
    if (a < b) :
        a, b = b, a
    if (a % b == 0) :
        return b
    return gcd(b, a % b)


################################ NO LO USO ###################################

#Funcion que calcula el simbolo de Jacobin (a/N) (no funciona por profundida de la recursion)
def jacobi_clase(a, n):
    if a == 0:
        return 0
    elif a == 1:
        return 1
    elif a == -1:
        return (-1)**(((n-1)//2)%2)             #%2 es por eficiencia
    elif a == 2:
        return (-1)**(((n*n-1)//8)%2)
    elif a%2 == 0:
        return jacobi_clase(2, n)*jacobi_clase(a//2, n)     #uso propiedad multiplicativa
    elif a > n:
        return jacobi_clase(a%n,n)
    else:
        return jacobi_clase(n, a)*(-1)**((((n-1)*(a-1))//4)%2)

###############################################################################
    

#Funcion para calcular el simbolo de Jacobi de forma iterativa:
#Basado en la ley de reprocidad cuadratica
def jacobi(a, n):
    if gcd(a,n) != 1:
       return 0
    #Primero reducimos modulo n para reducir el numero pues el simb jacobi es igual
    a = a % n 
    #Si l num es 1 ya sabemos que jacobi es 1
    if a == 1: 
        return 1
    #Si a es -1 ya sabemos que jacobi es 1 o -1 segun N mod 4
    if a  == -1:
        if n % 4 == 1:
            return 1
        else:
            return -1
    #Si el numero es par, separamos el 2 y calculamos el jacobi de 2 (1, o -1 segun modulos) y el otro por separado
    if a % 2 == 0: 
        if n % 8 == 1 or n % 8 == 7:
            return jacobi(a//2, n)
        else:
            return -jacobi(a//2, n)
    #En otro caso utilizamos la formula dada
    else:
        if n % 4 == 3 and a % 4 == 3:
            return -jacobi(n, a)
        else:
            return jacobi(n, a)


#Funcion que aplica k veces el test de Solovay-Strassen al entero N impar
def solovay_strassen(N, k):
    for i in range(k):
        #Elegimos numero al azar entre 1 y N-1 (siempre par).
        #Si a es factor de N, N es compuesto
        a = random.randint(1, N-1)            
        if gcd(a, N) > 1:       
            return "compuesto"
        
        #Calculamos simb. Jacobi mod N y vemos si a^(N-1)/2 es igual a este 
        #para ver si es compuesto. Si no, es problabemente primo
        jac = jacobi(a,N) % N
        ex = pow(a, (N-1)//2, N) 
        if jac != ex:
            return "compuesto"
    return "probablemente primo"


#Funcion que genera un numero de n digitos e itera k veces el test de 
#Solovay-Strassen hasta que encontramos un numero que lo pasa 
def generar_primo(n, k):
    cnt = 0
    parar = False
    p = 0
    while not(parar):
        cnt += 1
        #Generamos el numero p, generando n digitos entre 0 y 9 y multiplicandolo por 1, 10, 100,... y sumandolos 
        #Fuerzo a que el numero generado sea par (primer digito)
        ok = False
        while not(ok):
            p = random.randint(1, 9)
            if (p % 2 != 0):
                ok = True
        #Genero el resto de digitos
        for i in range(1, n):
            a = random.randint(0, 9)
            p += a * (10 ** i)
            
        #Pasamos k veces el test con p y vemos si hemos acertado o hay que probar con otro numero
        if(p != 1 and solovay_strassen(p, k) == "probablemente primo"):
            parar = True
    return (p, cnt)
        
    
#Funcion que genera el histograma de invocar numerosas veces generar_primo(300,20)
def generar_histograma(): 
    n = 120     
    histograma = []
    for i in range(n):
        x, y = generar_primo(300, 20)
        histograma.append(y)
            
    plt.title('Histograma generar_primo(300, 20)')
    plt.xlabel('cnt')
    plt.ylabel('frecuecia')
    plt.hist(histograma, rwidth=0.5, bins = 50) #bins es el numero de intervales que hace
    plt.savefig('histograma.png')
    plt.show()


################################ NO LOS USO ###################################
    
def generar_barras(): 
    n = 120     
    barras = {}
    for i in range(n):
        x, y = generar_primo(300, 20)
        if y in barras:
            barras[y] += 1
        else:
            barras[y] = 1
    
    print(barras)            
    plt.title('Diagrama Barras generar_primo(300, 20)')
    plt.xlabel('cnt')
    plt.ylabel('frecuecia')
    plt.bar(barras.keys(), barras.values())
    plt.savefig('diagBarras.png')
    plt.show()
    
def generar_sectores():            
    n = 120
    results = []
    for i in range(n):
        x, y = generar_primo(300, 20)
        results.append(y)
            
    plt.title('Diagrama Sectores generar_primo(300, 20)')
    plt.pie(results)
    plt.savefig('diagSectores.png')
    plt.show()
    
###############################################################################
    
    
    
    