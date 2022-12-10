#Topicos-especiais.py

#Revisão de conteudo basico especial

#Isto é um comentario de uma linha
"""
Este é um comentario
de
multiplas
linhas
"""

#Tipos de variáveis
a=30#int
print(type(a))

nome="Luiz"#float
print(type(nome))

valor='123' #str
print(type(valor))

complexo=3+5j #complex
print(type(complexo))

nenhum=None #NoneType
print(type(nenhum))

#Testando tipos
import numbers

#é um numero?
print('a:',isinstance(a,int))
print('nome:',isinstance(nome,float))

#False
print(isinstance('nome:',numbers.Number))  #'Luiz'
print(isinstance('valor:',numbers.Number))      #'123'

print('nome:',nome.isnumeric())  #False
print('valor:',valor.isnumeric()) #True

print(isinstance(complexo, complex))    #True
print(isinstance(complexo, numbers.Number))  #False

print(isinstance(nenhum, numbers.Number))    #False

#Conversões
print('\nConversões')
a=int(3.94)    #trunca
print(a)

b=float(5)
print(b)

c='abc'
if c.isnumeric():
     r=int(c)
else:
     r='Não é número'
     print(r)

d=float('3.14')
print('d:',d)
e=complex(3,5) #3+5j
print('e:',e)
f=e.real #3.0
print('f:',f)
