# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 15:28:40 2021

@author: ethan
"""

#二进制数

a = 2641

a_bin = bin(2641)[2:]

cov_a_bin = bin(2641)[2:][::-1]

sum_a = ''

for i in range(len(cov_a_bin)):
    if cov_a_bin[i] == '1':
        print(i)
        
        if sum_a == '':
            sum_a += str(2**(i))
        else:
            sum_a += ' + ' + str(2**(i))
            

print(sum_a)