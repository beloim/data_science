#Conjuntos.py

#Um conjunto de uma coleçao desordenada de elementos, sem repetiçao

frutas= {'uva','banana','laranja','uva','banana'}
frutas.add('kiwi')
frutas.remove('banana')
print(frutas)
print('Tamanho:',len(frutas))

#tem uva np conjunto?
print('uva'in frutas)
#nao tem banana?
print('banana'not in frutas)

print('\nImprimindo o conjunto:')
for f in frutas: print(f)

#conjunto para lista
print(list(frutas))

#conjuto para tupla
print(tuple(frutas))

#criando um conjunto com a funçao set
a= set('abaracadabra')
print(a)

b=set ('alacazam')
print(b)
