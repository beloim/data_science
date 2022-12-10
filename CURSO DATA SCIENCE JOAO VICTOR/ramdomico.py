#ramdomico.py
import random
frutas= ['banana','laranja','uva','abacaxi','kiwi']
#embaralha
random.shuffle(frutas)
print(frutas)

#numero aleatorio entre 0 e 1
print(random.random())

#retorna randomicamente 2 itens da lista
print(random.sample(frutas,k=2))

#retorna randomicamente 3 itens da lista
print(random.sample(frutas,k=3))

#inicio,fim (exclusivo), passo
print(random.randrange(3,12)) #passo 1

#start,end, step
print(random.randrange(3,12,3)) #passo 3:3,6,9

#idem randeranre,porem é inclusivo!
print('randint', random.randint(3,12)) #sem step

print(ord('A'),ord('B'),ord('C'))
print(chr(65),chr(66),chr(67))

frase='o rato roeu a roupa'
for letra in frase:
     print(ord(letra), end=' ')

#list comorehension(compreensao de lista)
lista=[ord(letra) for letra in frase]
print (lista)

print('Soma(hash):',sum(lista))
print('Min:',min(lista))
print('Max:',max(lista))

#criptografando texto
palavra= input('Digite uma palavra:')#'hoje'
codigo=[ord(c)+1 for c in palavra]
print(''.join([chr(c) for c in codigo]))

#gerador de senhas                                  #a   z
print('Senha randomica:',''.join([chr(random.randint(97,122))for x in range(7)]),end='')
