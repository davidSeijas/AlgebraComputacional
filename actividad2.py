#DAVID SEIJAS PEREZ
#problema 2.4

lista = [1]*100                 #lista original con la que comparar (cada posicion lleva el numero de bolas que hay en su caja)
lista2 = [1]*100                #lista con las posiciones de las bolas actuales
turno = 0                       #lleva la cuenta del turno por el que vamos
i = 0                           #i indicara la caja por la que empezamos cada turno a sacar bolas
stop = False                    #nos indicara cuando hemos terminado

while stop != True:
    turno += 1
    ind = i                     #ind sera el indice de la caja donde hay que ir poniendo las bolas sacadas
    aux = lista2[i]             #aux es el numero de bolas que habia en la caja que se vacia 
    
    while aux > 0:              
        ind = (ind + 1)%100     #actualizamos el indice de la caja en la que insaertar la siguiente bola
        lista2[i] -= 1          #movemos de la bola de caja
        lista2[ind] += 1
        aux -= 1                
        
    i = ind                     #para empezar el siguiente turno por la caja en la que se puso la ultima bola
    if lista2 == lista:         #si la configuracion de bolas al acabar el turno es igual que la original hemos acabado
        stop = True

print(turno)


#Se necesita el aux en el while y no vale lista2[i] pues hay un momento en 
#el que se mete una bola en la propia caja de la que se saca y ahí el bucle 
#no pararía pues lista2[i] seria 1, aunque ya hayamos terminado el turno