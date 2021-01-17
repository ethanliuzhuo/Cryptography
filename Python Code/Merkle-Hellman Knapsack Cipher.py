# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 23:36:53 2020

@author: ethan
"""

Plaintext = 'AGREE' #明文

a = [2,5,9,22,47,99,203,409] #Bob设置超级递增数列
p = 997  #Bob设置质数
A = 60 #Bob设置加密因子

b  = [i*A%p for i in a] #求b数列，发送给Alice

A_inv = pow(A,-1,p) #Bob求A的逆

def subset_sum(t,s,x,n,M,a,X):
    """
    子集和问题求解，返回空集合或者序列X

    Parameters
    ----------
    t : int
        递归深度.
    s : int
        子集和.
    x : dict
        判断列表，状态为1或0.
    n : int
        序列长度.
    M : int
        序列长度.
    a : list
        集合b，使得x_1b_1+x_2b_2+...+x_nb_n=M.
    X : list:
        空list，储存结果

    Returns
    -------
    X: list
    0 或 1.
    """
    if t == n:
        if s == M: 
            for i in range(0,n):
                if x[i] != 0: 
                    X += [1] #取b_i
                else:
                    X += [0] #不取b_i
            
    else:
        s = s+a[t]
        x[t] = a[t]
        subset_sum(t+1,s,x,n,M,a,X)
        s = s-a[t]         #回溯之前还原
        x[t] = 0
        subset_sum(t+1,s,x,n,M,a,X)
        
    return X

        
for i in Plaintext:
    """Alice 加密过程"""
    c_int = ord(i)
    c_bin = bin(c_int) #将字符转化为二进制
    c = 0
    
    if len(c_bin[2:]) != 8:
        c_bin = '0'*(8-len(c_bin[2:])) + c_bin[2:] #二进制转为8位二进制，与a长度相同
    else:
        c_bin = c_bin[2:]
        
    for j in range(8):
        try:
            # print(c_bin[j],b[j],j)
            c += int(c_bin[j])*b[j] #计算c，然后发送给Bob
        except:
            pass
    # print(c)
     """Bob 解密过程"""
    M = A_inv * c%p
    # print(M)
    
    t = 0            #递归深度
    s = 0            #子集和
    x = {}           #判断列表，状态为1或0
    n = len(a)
    X = []
    
    X = subset_sum(t,s,x,n,M,a,X) #解决子集和问题
    # print(X)
    
    bin_X = ''
    for k in X:
        bin_X += str(k)
    print(chr(int(bin_X,2))) #二进制转化ASCII字符
