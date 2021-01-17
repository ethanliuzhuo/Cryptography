# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 23:38:46 2020

@author: ethan
"""

Plaintext = 'ICANPLAY'#字母需要大写
a = 7
b = 25

Ciphertext = ''
for i in Plaintext:
    x = ord(i) -65 
    y = (a*x + b)%26
    Ciphertext += chr(y+ 65) 
    