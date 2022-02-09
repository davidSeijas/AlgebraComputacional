#DAVID SEIJAS PÉREZ
#problema 1.5

def digitos(n):             #esta funcion me devuleve una lista con los digitos de un numero, pero al reves. Es decir si n=236, me devuelve [6,3,2]
    lista = []
    m = n
    
    while m > 0:                #si tiene mas de un digito, añado el ultimo y divido entre 10 y si no añado el unico digito que tiene y divido entre 10 para acabar
        if (m // 10) != 0:
            lista.append(m%10)
        else:
            lista.append(m)
        m //= 10
        
    return lista



digs = [0]                 #digs guardara toda la secuencia de los decimales del numero de champernowne y calculara la multiplicacion de los indicados
cont = 1

while cont <= 200000:     #aqui para cada numero hasta el 200000 (no hacen falta hasta el 1000000 pues hay muchos numeros con mas de 1 digito), devuelvo sus digitos en una lista y los añado a digs en el orden correcto (pues esa lista estaba al reves)
    aux = digitos(cont)
    for i in range(1, len(aux) + 1):
        digs.append(aux[len(aux) - i])
    cont += 1
        
print(digs[1] * digs[10] * digs[100] * digs[1000] * digs[10000] * digs[100000] * digs[1000000])