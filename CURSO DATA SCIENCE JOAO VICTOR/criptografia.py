#Criptografia.py

#rolagem
#inteiro para binario
inteiro= ord ('A') #65
binario= bin(inteiro)    #'0b10000001'
print(binario)

#OU
binario= format(inteiro,'b') #'10000001'

#binario para interio
intyerio= int(binario,2) #base 2
print(inteiro)

#rolagem de bits para a esquerda
#'10000001' -> '00000011'
bit1= binario[0]
novo= binario[1:8] +bit1
print(novo)
print(binario, '=',int(binario,2))
print(novo,'=',int(novo,2))

#-------------------------------

#Criptografia com algoritmo simetrico de Fernet
#usa a mesma chave para criptografar e descriptografar

#pip install cryptography
from cryptography.fernet import Fernet

#gera chave de Fernet que deve ser mantida em segurança para
#descriptografar o texto
key =Fernet.generate_key()
#objeto fernet contendo a chave
f = Fernet(key)

#texto para criptografar em bytes
texto='os rios correm para o mar'

#codifica texto para utf-8(encode) e criptografa
criptografado=f.encrypt(texto.encode())
print('\n---- Fernet -----')
print(criptografado)

#descriptografa texto e decodifica de utf-8
descriptografado=f.decrypt(criptografado).decode()
print(descriptografado)

#-------------CONTINUA...
