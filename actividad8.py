#DAVID SEIJAS PEREZ
#problema 10.7
    

#Funcion que implementa el algoritmo de Cooley - Tuckey para calcular DFT_n (p)
def dfft(pol, exp, p):
    n1_2, n2 = len(pol[0]), len(pol)  #n1x2 porque es 2n1
    if n2 == 1:
        return pol
    
    #Inicializamos con listas de 0
    pol_even, pol_odd = [[0]*n1_2]*(n2//2), [[0]*n1_2]*(n2//2)
    
    for i in range(n2//2):
        pol_even[i], pol_odd[i]  = pol[2*i], pol[2*i + 1]
    
    #Elevar a 2 la xi es multiplicar por 2 el exponente que se envia al algoritmo
    a_even , a_odd = dfft(pol_even, 2*exp, p), dfft(pol_odd, 2*exp, p)   
    a = [[0] * n1_2] * n2
    
    for i in range(n2//2):
        #Calculamos xi^i * a_odd[i], para lo que necesitamos una funcion extra pues 
        #estamos multiplicando un polinomio (en lista) por una potencia de u
        aux = mult_pol_pot_u(a_odd[i], i*exp)
        a[i] = [(a_even[i][j] + aux[j]) % p for j in range(n1_2)]
        a[i + n2//2] = [(a_even[i][j] - aux[j]) % p for j in range(n1_2)] 
        
    return a


#Funcion que implementa el algoritmo de Cooley - Tuckey para calcular la transformada inversa
def ifft(pol, exp, primo):
    #En p queremos guardar fft(1/xi), pero 1/xi = xi^-1 = u^(-exp) = u^(4n1 - exp) pues u^4n1 = 1
    p = dfft(pol, 2*len(pol[0]) - exp, primo) 
    n = len(pol) #n = n2
    inv_n = 0
    
    #Ahora queremos calcular 1/n2 (que no es tan trivial como 1//n2 al estar en Zp)
    i = 1
    parar = False
    #Al estar en Zp, le inverso de n2 es aquel que multiplicado por n2 (modulo p=primo) da 1
    #Vamos hasta primo pues estamos en Zp y el inverso es unico asi que una vez lo encontremos paramos
    while not(parar) and i < primo:  
        if (n * i) % primo == 1:
            inv_n = i
            parar = True
        i += 1
    aux = len(pol[0])    #aux = 2n1
    for i in range(n):
        for j in range(aux):
            p[i][j] = (p[i][j] * inv_n) % primo

    return p


#Funcion que multiplica un polinomio por u^exp en Z/<u^2n1 + 1>
def mult_pol_pot_u(pol, exp):        
    n = len(pol)    #n = 2n1
    prod = [0]*n
    signo = 1       #pues u^(2n1+j) = -u^j
    
    while exp > 2*n:    #Le restamos al exponente potencia de 4n1 pues u^4n1=1 y queda igual               
        exp -= 2*n
    if exp >= n:        #Como u^2n1 = -1 si el exponente es mayor que 2n1 pasamos el exponente a positivo y guardamos que el signo es -
        exp = exp - n
        signo = -1
        
    #n - exp + i < n -> al aplicar modulo x^n + 1 esos exponentes van a pasar a estar restando    
    for i in range(n):
        if i >= exp:   
            prod[i] = signo * pol[i - exp]
        else:
            prod[i] = -signo * pol[n - exp + i]
            
    return prod


#Función que calcula la negaconvolución básica para la mult. de pols en casos base k = 0,1,2
def mult_base (f, g, p) : #Long de f y g es, al menos, 2^k
    sol = []
    for i in range(len(f)):
        aux = 0
        for j in range(len(f)):
            if j <= i:
                aux += f[j] * g[i - j]
            else: 
                aux -= f[j] * g[i + len(f) - j]
        sol.append(aux % p)
    return sol


#Funcion que calcula el producto de los polinomios f y g en el anillo (Z/pZ)[x]/<x^2^k+1>
def mult_ss_mod(f, g, k, p) : 
    #Extendemos los pols f y g con 0s a long 2^k
    f += [0]*(2**k - len(f))
    g += [0]*(2**k - len(g))
    
    if 0 <= k <= 2 : #Casos base k = 0,1,2
        return mult_base(f, g, p)
    
    #Definimos k1 y k2 para que k1=k2 (si k par) o 1+k1=k2 (si k impar)
    k1 = k // 2
    k2 = k - k1
    n1, n2 = 2**k1, 2**k2
    
    #EMPEZAMOS LA NEGACONVOLUCIÓN
    #Necesitamos que f y g tengan elems de long 2n1
    f_t = [[f[x] for x in range(n1*i, n1*(i+1))] + [0]*n1 for i in range(n2)]
    g_t = [[g[x] for x in range(n1*i, n1*(i+1))] + [0]*n1 for i in range(n2)]
    
    n1_2, n2 = len(f_t[0]), len(f_t)    #n1_d = 2n1
    exp = n1_2//n2                      #u^exp es raiz 2n2-ésima
    
    v = [mult_pol_pot_u(f_t[k], exp*k) for k in range(n2)] #Estas serian realmente las a·v
    w = [mult_pol_pot_u(g_t[k], exp*k) for k in range(n2)] #a·w
    v_d = dfft(v, 2*exp, p) #DFT_n(a·v)
    w_d = dfft(w, 2*exp, p) #DFT_n(a·w)    
    
    #Usamos la recursion para calcular DFT_n(a·v)·DFT_n(a·w)
    #Llamamos con k1+1 pues los elems ahora son de longitud 2n1
    r = [mult_ss_mod(v_d[i], w_d[i], k1 + 1, p) for i in range(n2)]
    #Calculamos ahora IDFT_n de lo anterior 
    r_i = ifft(r, 2*exp, p)
    
    #Calculamos h multiplicando por a^-1 y aplicando el módulo
    h_t = [mult_pol_pot_u(r_i[i], (2*n2 - i) * exp) for i in range(n2)]
    
    #Para acabar tenemos que poner la solucion h_t bien con elementosde long n1
    #Creo un vector donde iré guardando los elementos. Lo que hago es sumar los elementos
    #del elemento n1*i + j de h_t (que esta distribuida como matriz) en los elementos n1*i+j 
    #de sol (que es una unica lista). Hay que tener en cuenta que cuando sobrepasamos n1*n2 
    #(los ultimos n1 elems de h_t[n2-1] (pues la long de h_t es de n1*n2 + n1) los restamos a los
    #primeros n1 elems de la solucion por la aplicación del módulo
    sol = h_t[0]
    for i in range(1, len(h_t)):
        for j in range(len(h_t[i])):
            if j >= n1:
                if i == n2 - 1: #Restar los n1 ultimos elementos por el modulo x^n2 + 1
                    sol[j - n1] = (sol[j - n1] - h_t[i][j]) % p
                else:
                    sol.append(h_t[i][j])
            else:
                sol[n1*i + j] = (sol[n1*i + j] + h_t[i][j]) % p
                
    return sol
        
    

#Funcion que calcula el producto de f*g en el anillo (Z/pZ)[x]
def mult_pol_mod(f, g, p) :
    if len(f) == 0 or len(g) == 0:
        return []
    
    #Grado de f*g es grado de f + grado de g, pero la lista de coefs es de longitud grado + 1
    d = len(f) + len(g) - 2 
    k = 0
    x = 1
    #Buscamos el k tal que 2^k > d = deg(f) + deg(g)
    while(d >= x):           
        x *= 2
        k += 1
    prod = mult_ss_mod(f, g, k, p)
    
    
    #Eliminamos los 0s de la derecha del producto f*g
    #Empezando por la derecha paramos en el indice que tenga el primer elemento no nulo
    #Si todos los elementos eran 0 llegamos a i = -1 y entonces devolvemos la lista vacia y si no devolvemos hasta el indice que hemos llegado
    i = len(prod) - 1
    while prod[i] == 0 and i >= 0: 
        i -= 1
    if i < 0: 
        return []
    else:
        return prod[:i+1]