#Topicos-especiais2.py

#Operadores relacionais
x=5
y=7
x==y      #False
x!=y      #True
x>y       #False
x>=y      #False
x<y       #True
x<=y      #True
3<x<7
#if 3>x and x<7:
#    print('True')

#Valores não numéricos
import math
import numbers
x=float('nan') #Not a Number
print(x)  #nan
print(type(x)) #float
print(x+1) #nan

#Não é numérico, porém é instancia de Number
print(isinstance(x,numbers.Number)) #True

y=math.nan
print(math.isnan(y))     #True

a=float('-inf')
print(math.isinf(a)) #é infinito
print(isinstance(a,numbers.Number))     #é numérico

b=float('inf')
print(math.isinf(b)) #é infinito
print(isinstance(b,numbers.Number))     #é numérico

print(a+b)#nan
print(a<-1)#-inf <-1=True
print(b>1)#inf >1 =True
print(a==b)#-inf==inf=False
print(a!=b)#-inf!=inf=True

c=10
print(math.isfinite(c))  #c é finito=True






