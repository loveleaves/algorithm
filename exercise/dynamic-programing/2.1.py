# -*- coding:utf-8 -*-
# Author:         yeyu
# file name:        dybamic-programing.py
import sys
import time
sys.setrecursionlimit(100000) #递归深度设置为十万

def LCG(rdls, mi, ma, n): #线性同余法生成随机数
    m = 2 ** 32  # 线性同余法变量定义
    a = 1103515245
    c = 12345
    seed = time.time()
    for i in range(n):
        seed = (a * seed + c) % m
        rdls.append(int((ma - mi) * seed / float(m - 1)) + mi)
def KnapsackDP(w, v, C,n):
    m = [[0] * (C) for _ in range(n)]
    for i in range(n):
      for j in range(C):
        m[i][j]=m[i-1][j]
      if w[i]<=j:
        m[i][j]=max(m[i][j],m[i-1][j-w[i]]+v[i])
    return m[n-1][C-1]
def output(C,n):
    start = time.time()
    w = []
    v = []
    LCG(v,1,100,n)
    LCG(w,1,30,n)
    m = KnapsackDP(w,v,C,n)
    end = time.time()
    print('n = ',n,' Time is ',(end-start)*1000,'ms')

if __name__ == '__main__':
    n = [10, 20, 40, 100, 200, 400, 800, 2000]
    C = [200,400,800,2000]
    for i in C:
        print('C = ',i)
        for j in n:
            output(i,j)
        print()