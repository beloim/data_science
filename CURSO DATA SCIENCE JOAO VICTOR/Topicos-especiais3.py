#Topicos-especiais3.py

import math

#Listas com valores nao numericos
lista=[-10,None,math.nan,3.14,float('-inf'),2,float('inf')]

print(lista)

for x in lista:
     if x is not None and math.isfinite(x):
          print(x)
     else:
          print('não é numerico')
#operador ternario
for x in lista:
     print(x if x is not None and math.isfinite(x) else'não é numerico')
      
#Laço de repetiçao while
print('Exemplo while')
x=1
while x<6:
     print(x,end=' ')
     x +=1

#Blocos de identação
x=0
while x<6:
     if x % 2 == 0:
          print(x,'=par')
     else:
          print(x,'=impar')
     x+=1
     
print('fim do programa')
