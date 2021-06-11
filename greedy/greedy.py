# -*- coding:utf-8 -*-
# Author:         yeyu
# file name:        greedy.py
import random
import time

w = []
v = []
x = []
temp = []
# def LCG(rdls, mi, ma, n): #线性同余法生成随机数
#     m = 2 ** 32  # 线性同余法变量定义
#     a = 1103515245
#     c = 12345
#     seed = time.time()
#     for i in range(n):
#         seed = (a * seed + c) % m
#         rdls.append(int((ma - mi) * seed / float(m - 1)) + mi)

def KnapsackGreedy(v, w, m, x, n): # 这里的v,w是合并排序后的价值、重量列表
    value = 0  #value记录对应解的总价值
    for i in range(n):
        x.append(0)
    cu=m    #cu是背包剩余容量
    for i in range(n):
        if w[i]>cu:
            break
        x[i]=1
        value += v[i]
        cu=cu-w[i]
    if i<=n:
        x[i]=cu/w[i]
        value += x[i]*v[i]
    # print('value = ',value)

def MergeSort(lt, first, last): #升序合并排序，只对v、w进行排序
    if first<last:
          middle=int((first+last)/2)
          MergeSort(lt, first, middle)
          MergeSort(lt, middle+1, last)
          MergeLists(lt, first, middle, middle+1, last)
def MergeLists(lt, start1, end1, start2, end2):
    global v,w
    finalStart = start1
    finalEnd = end2
    result1 = []
    result2 = []
    indexC = 0
    while (start1<=end1) and (start2<=end2):
        if lt[start1] > lt[start2]:
            result1.append(v[start1])
            result2.append(w[start1])
            start1 +=1
        else:
            result1.append(v[start2])
            result2.append(w[start2])
            start2 +=1
        indexC +=1
    if start1 <= end1:
          for i in range(start1,end1+1):
            result1.append(v[i])
            result2.append(w[i])
            indexC +=1
    else:
          for i in range(start2,end2+1):
            result1.append(v[i])
            result2.append(w[i])
            indexC +=1
    indexC=0
    for i in range(finalStart,finalEnd+1):
        v[i] = result1[indexC]
        w[i] = result2[indexC]
        indexC +=1
def output(n):
    global w,v,x,temp
    m = 200 #背包容量限定为200
    w = []
    v = []
    x = []
    temp = []

    for i in range(n): #随机生成n件物品的价值、重量，计算出（价值/重量）
        w.append(random.randint(1, 30))
        v.append(random.randint(1, 100))
        temp.append(v[i] / w[i])
    start = time.time() #此处时间记录的是对v/w合并排序和贪婪算法求解背包问题的总时间
    MergeSort(temp, 0, n - 1)  #temp为排序依据
    KnapsackGreedy(v, w, m, x, n)
    end = time.time()
    print('n = ',n,' Time is ',(end-start)*1000,'ms')

if __name__ == '__main__':
    n = [10, 20, 40, 100, 200, 400, 800, 2000]
    for i in n:
        output(i)