# -*- coding:utf-8 -*-
# Author:         yeyu
# file name:        divideandconquer.py
import sys
import time
sys.setrecursionlimit(100000) #递归深度设置为十万
n1 = 0 # 全局变量记录比较次数
n2 = 0
n3 = 0

def LCG(rdls, n): #线性同余法生成随机数
    m = 2 ** 32  # 线性同余法变量定义
    a = 1103515245
    c = 12345
    mi, ma = 1, 100  # 随机数范围1-100
    seed = time.time()
    for i in range(n):
        seed = (a * seed + c) % m
        rdls.append(int((ma - mi) * seed / float(m - 1)) + mi)

def BubbleSort(lt, n): #冒泡排序
    global n1
    numberOfPairs = n
    swappedElements = True
    while swappedElements:
        numberOfPairs = numberOfPairs - 1
        swappedElements = False
        for i in range(numberOfPairs+1):
            if lt[i] > lt[i+1]:
                lt[i], lt[i+1] = lt[i+1], lt[i]
                swappedElements = True
            n1 += 1

def MergeSort(lt, first, last): #合并排序
    global n2
    n2 += 1
    if first<last:
          middle=int((first+last)/2)
          MergeSort(lt, first, middle)
          MergeSort(lt, middle+1, last)
          MergeLists(lt, first, middle, middle+1, last)
def MergeLists(lt, start1, end1, start2, end2):
    global n2
    finalStart = start1
    finalEnd = end2
    result = []
    indexC = 0
    n2 += 1
    while (start1<=end1) and (start2<=end2):
        n2 += 1
        if lt[start1] < lt[start2]:
            result.append(lt[start1])
            start1=start1+1
        else:
            result.append(lt[start2])
            start2 +=1
        indexC=indexC+1
    n2 += 1
    if start1 <= end1:
          for i in range(start1,end1+1):
            result.append(lt[i])
            indexC=indexC+1
    else:
          for i in range(start2,end2+1):
            result.append(lt[i])
            indexC=indexC+1
    indexC=0
    for i in range(finalStart,finalEnd+1):
          lt[i]=result[indexC]
          indexC=indexC+1

def QuickSort(lt, first, last): #快速排序
    global n3
    n3 += 1
    if first<last:
      pivot=PivotList(lt, first, last)
      QuickSort(lt, first, pivot-1)
      QuickSort(lt, pivot+1, last)

def PivotList(lt, first, last):
    global n3
    PivotValue=lt[first]
    PivotPoint=first
    for index in range(first+1,last+1):
        n3 += 1
        if lt[index]<PivotValue:
            PivotPoint=PivotPoint+1
            lt[PivotPoint],lt[index]=lt[index],lt[PivotPoint]
    lt[first],lt[PivotPoint]=lt[PivotPoint],lt[first]
    return PivotPoint
def output(t):
    global n1,n2,n3
    n1,n2,n3=0,0,0
    x1 = []
    LCG(x1,t)
    n = len(x1)
    x2 = x1.copy()
    x3 = x1.copy()
    BubbleSort(x1, n - 1)
    MergeSort(x2, 0, n - 1)
    QuickSort(x3, 0, n - 1)
    print('数据规模：',t)
    print('BubbleSort : ', n1)
    print('MergeSort: ', n2)
    print('QuickSort', n3)
    print()
if __name__ == '__main__':
    x = [10,100,1000,2000,5000,10000,100000]
    for i in x:
        output(i)