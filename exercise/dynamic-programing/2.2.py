# -*- coding:utf-8 -*-
# Author:         yeyu
# file name:        dynamic-programing.py
n1,n2 = 0,0

def DAC_f(n):
    global n1
    if n==1 or n==2:
       return 1
    else:
        n1 += 1
        return DAC_f(n-1)+DAC_f(n-2)
def DP_f(n):
    global n2
    f = []
    for i in range(n):
        if i==0 or i==1:
             f.append(1)
        else:
            f.append(f[i-1]+f[i-2])
        n2 += 1
    return f[n-1]
def output(n):
    DAC_f(n)
    DP_f(n)
    print('n = ',n)
    print('DAC_f : ',n1)
    print('DP_f : ',n2)
    print()

if __name__ == '__main__':
    n = [5,10,15,20,25,30]
    for i in n:
        output(i)