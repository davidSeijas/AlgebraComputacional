#DAVID SEIJAS PEREZ
#problema 3.4

def es_posible_ganar_con_n_piedras(n): 
    if n == 0:
        return True
    elif n == 1:
        return False
    elif 2 <= n < 6:
        if not(es_posible_ganar_con_n_piedras(n-1) and es_posible_ganar_con_n_piedras(n-2)):
            return True
        else:
            return False
    else :
        if not(es_posible_ganar_con_n_piedras(n-1) and es_posible_ganar_con_n_piedras(n-2) and es_posible_ganar_con_n_piedras(n-6)):
            return True
        else:
            return False
        
#Alg recursivo: simplemente tengo que mirar que si quitando 1, 2 o 6 piedras
#(esto lo hacemos llamando a la misma funcion, pero con n-1 n-2 o n-6) 
#llevo al rival a una situación en la que No tiene estrategia ganadora y, por 
#tanto, puedo ganar yo siempre

#Algoritmo iterativo con programacion dinamica

def es_posible_ganar_con_n_piedras_PD(n):
    l = [True] * (n+1)                      #creamos la lista al elemento que queremos saber con True
    l[1] = False                            #caso base de 1 es False
    i = 2
    while i <= n:                           #hasta llegar al elem que nos interesa vamos dando valor a los anteriores pues se necesitaran para luego determinar el del que queremos
        if i < 6:
            l[i] = not(l[i-1] and l[i-2])   
        else:
            l[i] = not(l[i-1] and l[i-2] and l[i-6])  #si uno de esos elementos anteriores es False es que hemos llevado al rival a una situación de perder y, por tanto, nosotros tenemos estrategia ganadora (valor de True) quitando el numero de palos correspondiente al elem que sea False
        i += 1
    return l[n]

#Es la misma idea, pero con programación dinámica. De esta manera, creamos 
#una lista en la que los casos base (0 y 1, podría ser solo 0) los sabemos
#y los elementos siguiente se irán creando en función de los elementos i-1,
#i-2 e i-6 de esa lista. Finalmente, cuando hayamos determinado el valor de
# la posicion que queríamos saber simplemente paramos y devolvemos ese valor.
#Estaríamos formando una especie de gafo orientado en el que cada elemento
#es apuntado por su anterior, el anterior del anterior y el de la 6a posición
#detras de el.

#Para que el caso base sea solo 0, podemos añadir condiciones de if i < 2
#y hacer solo comparacion con l[i-1] (en la recursiva tambien) pero el
#resultado es esencialmente el mismo

print(es_posible_ganar_con_n_piedras_PD(10**6))