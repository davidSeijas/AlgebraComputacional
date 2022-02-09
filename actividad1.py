#DAVID SEIJAS PÉREZ
#problema 1.5

m = 0                         #m lleva la cuenta de los digitos (no nums) recorridos           
champernowne = []             #guardanmos los numeros de charnowne que querremos despues multiplicar
nums = [1, 10, 100, 1000, 10000, 100000, 1000000]    #esto son los indices de los decimales que queremosi
resultado = 1    

for cont in range(1, 200000):  #con 200000 nos vale porque segun avanzamos hay muchos mas digitos que numeros
    for aux in str(cont):      #aux es el digito recorrido en cada momento
        m += 1
        if m in nums:          #si ocupa una posicion de las que queremos lo metemos en la lista champernowne
            champernowne.append(int(aux))
        
for x in champernowne:
    resultado *= x
    
print(resultado)

#Recorremos numero a numero (con cont) y en cada numero recorremos sus digitos
#y por cada digito contabilizado sumamos uno a m. Cuando m llega a uno de los 
#digitos buscados (los que estan en nums) lo añadimos a champernowne para
#despues multiplicarlo 