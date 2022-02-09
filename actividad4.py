#DAVID SEIJAS PEREZ

def suma_matrices(A,B): 
    C = []
    for i in range(len(A)):
        C.append([0]*len(A[i]))
        for j in range(len(A[0])):
            C[i][j] = A[i][j] + B[i][j]
    return C

def resta_matrices(A,B): 
    C = []
    for i in range(len(A)):
        C.append([0]*len(A[i]))
        for j in range(len(A[0])):
            C[i][j] = A[i][j] - B[i][j]
    return C

def mult_escuela(A,B):
    C = []
    for i in range(len(A)):
        C.append([0]*len(A[i]))
        for j in range(len(A[0])):
            for k in range(len(A)):
                C[i][j] += A[i][k] * B[k][j]
    return C


def mult_strassen(A,B):
    n = len(A)
    p = (n%2 == 0)
    
    if n == 0:
        return []
    elif n == 1:
        return [[A[0][0]*B[0][0]]]
    elif n <= 50:
        return mult_escuela(A,B)
    elif not(p):                        #Si n es impar reajustamos             
        A.append([0]*(n+1))             #Añadimos una fila de 0s a cada matriz
        B.append([0]*(n+1))
        for i in range(n):
            A[i] += [0]                 #Añadimos un 0 al final de cada fila en cada matriz
            B[i] += [0]                 #que es basicamente añadirle una col de 0s
        n += 1
        
    #Troceamos las matrices
    A11 = [[A[i][j] for j in range (n//2)] for i in range(n//2)]
    A12 = [[A[i][j] for j in range (n//2, n)] for i in range(n//2)]
    A21 = [[A[i][j] for j in range (n//2)] for i in range(n//2, n)]
    A22 = [[A[i][j] for j in range (n//2, n)] for i in range(n//2, n)]
    B11 = [[B[i][j] for j in range (n//2)] for i in range(n//2)]
    B12 = [[B[i][j] for j in range (n//2, n)] for i in range(n//2)]
    B21 = [[B[i][j] for j in range (n//2)] for i in range(n//2, n)]
    B22 = [[B[i][j] for j in range (n//2, n)] for i in range(n//2, n)]
    
    #Calculamos Ms y Cs
    s1 = suma_matrices(A11, A22)
    s2 = suma_matrices(B11, B22)
    s3 = suma_matrices(A21, A22)
    s4 = resta_matrices(B12, B22)
    s5 = resta_matrices(B21, B11)
    s6 = suma_matrices(A11, A12)
    s7 = resta_matrices(A21, A11)
    s8 = suma_matrices(B11, B12)
    s9 = resta_matrices(A12, A22)
    s10 = suma_matrices(B21, B22)
    
    M1 = mult_strassen(s1, s2)
    M2 = mult_strassen(s3, B11)
    M3 = mult_strassen(A11, s4)
    M4 = mult_strassen(A22, s5)
    M5 = mult_strassen(s6, B22)
    M6 = mult_strassen(s7, s8)
    M7 = mult_strassen(s9, s10)
                       
    C11 = suma_matrices(resta_matrices(suma_matrices(M1, M4), M5), M7)
    C12 = suma_matrices(M3, M5)
    C21 = suma_matrices(M2, M4)
    C22 = suma_matrices(suma_matrices(resta_matrices(M1, M2), M3), M6)                
    
    #Recomponenos la matriz:
    C = []
    
    for i in range(n//2):
        C.append([0]*n)
        for j in range(n//2):
            C[i][j] = C11[i][j]
        for j in range(n//2, n):
            C[i][j] = C12[i][j - n//2]
            
    for i in range(n//2, n):
        C.append([0]*n)
        for j in range(n//2):
            C[i][j] = C21[i - n//2][j]
        for j in range(n//2, n):
            C[i][j] = C22[i - n//2][j - n//2]
    
    #Si n es impar (era antes) borramos ultima fila y columna
    if not(p):
        C.pop(n-1)                      #Borramos la últ. fila
        for i in range(len(C)):
            C[i].pop(n-1)               #Borramos el últ. elem. de cada fila (borramos la últ. col.)
    return C