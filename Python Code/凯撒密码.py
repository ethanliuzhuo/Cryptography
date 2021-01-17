# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 23:41:18 2020

@author: ethan
"""

cipher = 'exxegoexsrgi'


for j in range(26):
    Plaintext = ''
    for i in cipher:
        if (ord(i) - j) < 97:
            alpha =  chr((ord(i) - j)  + 26)
        else:
            alpha = chr(ord(i) - j)
        Plaintext += alpha
    print(Plaintext)


#%%
Plaintext = 'iamaperson'
ciphertext = ''

key = 4

for i in Plaintext:
    if (ord(i) + key) > 122:
            alpha =  chr((ord(i)  + key)  - 26)
    else:
        alpha = chr(ord(i) + key)
    ciphertext += alpha
print(ciphertext)