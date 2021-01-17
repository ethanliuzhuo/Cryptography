# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 23:38:06 2020

@author: ethan
"""

#希尔密码

import numpy as np

Plaintext = 'COKE'#字母需要大写

A  = np.mat([[22,13],[11,5]])

Ciphertext = ''

if len(Plaintext)%2 == 0:
    pass
else:
    Plaintext += 'K' #填充K

for i in range(len(Plaintext)):
    if i%2 == 0:
        M = Plaintext[i:i+2]
        
        X = np.mat([[ord(M[0]) -65],[ord(M[1]) -65]]) 
        Y = A*X%26
        
        Ciphertext += chr(int(Y[0]) + 65)
        Ciphertext += chr(int(Y[1]) + 65)
print(Ciphertext)    
    