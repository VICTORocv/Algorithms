# -*- coding: utf-8 -*-
__author__ = 'Victor'
import numpy as np
from itertools import combinations

#动态规划法求解TSP问题

def Tsp(arc, n, v):
    d = [[0 for col in range(2**(n-1))] for row in range(n)]
    #d[0] = v
    for i in range(1, n):
        d[i][0] = arc[i][0]
    for j in range(1, 2**(n-1)):
        for i in range(1, n):
            if i not in v[j]:
                lst = []
                for k in v[j]:
                    vj = list(v[j])
                    vj.remove(k)
                    num = v.index(vj)
                    sum = arc[i][k] + d[k][num]
                    lst.append(sum)
                if len(lst) != 0:
                    d[i][j] = min(lst)
                else:
                    d[i][j] = 0
    lst = []
    for k in v[2**(n-1)-1]:
        vj = list(v[2**(n-1)-1])
        vj.remove(k)
        num = v.index(vj)
        sum = arc[0][k] + d[k][num]
        lst.append(sum)
    d[0][2**(n-1)-1] = min(lst)
    print d

if __name__ == '__main__':
    #n = int(raw_input("请输入矩阵的n值:"))
    n = 4
    #arc = np.zeros((n,n))

    '''
    print("请输入矩阵每行的元素，以空格间隔，每行结束以回车间隔")
    i = 0
    while i < n:
        raw = raw_input().split(" ")
        raw_int = [int(j) for j in raw]
        arc[i] = raw_int
        i += 1
    '''

    arc = [[0, 3, 6, 7], [5, 0, 2, 3], [6, 4, 0, 2], [3, 7, 5, 0]]
    v = []
    v.append([])
    for i in range(1, n):
        vi = [c for c in combinations(range(1, n), i)]
        for j in vi:
            v.append(list(j))
        #v.append([c for c in  combinations(range(1, n), i)])

    Tsp(arc, n, v)
