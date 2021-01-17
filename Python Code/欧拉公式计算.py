# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 15:27:59 2021

@author: ethan
"""

# 计算欧拉公式值
def gcd(p,q):
    while q != 0:
        p, q = q, p%q
    return p

def is_coprime(x, y):
    return gcd(x, y) == 1

def phi(x):
    if x == 1:
        return 1
    else:
        n = [y for y in range(1,x) if is_coprime(x,y)]
        return len(n)
print(phi(360))