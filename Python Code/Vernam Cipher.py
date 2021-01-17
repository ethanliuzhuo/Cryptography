# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 23:39:36 2020

@author: ethan
"""

"""加密"""
Plaintext = 'MYNAMEISBOB'#字母需要大写
U = [3,1,2,5,5,7,7,5,7]
V = [5,4,2,3,5,6,4,23,99,12]

def lcm(x, y):
   #  最小公倍数
   if x > y:
       greater = x
   else:
       greater = y
 
   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1
 
   return lcm

K_len = lcm(len(U),len(V))
K = [0 for i in range(K_len)]

for i in range(K_len):
    K[i] = (U[i%len(U)] +  V[i%len(V)])%26

print(K)#密钥

Ciphertext = ''
for i in range(len(Plaintext)):
    M_i = ord(Plaintext[i]) -65 #大写字母 -65
    K_i = K[i%len(K)]
    C_i = (M_i+K_i)%26
    Ciphertext += chr(C_i+ 65) 
    
print(Ciphertext)


"""破译"""
Ciphertext = 'UDRIWRTUDDH'
U = [3,1,2,5,5,7,7,5,7]
V = [5,4,2,3,5,6,4,23,99,12]
K = [0 for i in range(K_len)]

for i in range(K_len):
    K[i] = (U[i%len(U)] +  V[i%len(V)])%26

print(K)#密钥

Plaintext = ''
for i in range(len(Ciphertext)):
    C_i = ord(Ciphertext[i]) -65 #大写字母 -65
    K_i = K[i%len(K)]
    M_i = (C_i - K_i)%26

    Plaintext += chr(M_i+ 65) 
print(Plaintext)
