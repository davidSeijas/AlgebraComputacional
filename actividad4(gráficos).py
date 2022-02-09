import actividad4_DavidSeijas_4_4 as multStrassen
import random as rnd
import matplotlib.pyplot as plt
import time
import math

mindigs = 1
maxdigs = 400
digstep   = 1

numdigs = []
tiempos = []
tnormal = []
nlog = []
tlog = []

n = mindigs
while n <= maxdigs:
   A = []
   B = []
   for i in range(n):
       A.append([0]*n)
       B.append([0]*n)
       for j in range(n):
           A[i][j] = rnd.randint(0, 9)
           B[i][j] = rnd.randint(0, 9)
   
   ini = time.time()
   c = multStrassen.mult_strassen(A, B)
   fin = time.time()
   numdigs += [n]
   t = fin-ini
   t_norm = t / (n**(math.log(3)/math.log(2)))
   tiempos += [t]
   tnormal += [t_norm]
   nlog += [math.log(n)]
   print ("n =", n, "tiempo =", t, "[seg]")
   n += digstep

plt.plot(numdigs, tiempos, "b-")
plt.grid(b=True, which='major',axis='both', color='r', linestyle='--', linewidth=0.5)
plt.xlabel('número de dígitos')
plt.ylabel('tiempo [seg]')
plt.savefig("strassen-tiempos.png")
#plt.show()
plt.clf()
