# -*- coding: utf-8 -*-
__author__ = 'Victor'
import numpy as np
from itertools import product

#回溯法求解0/1背包问题

def KnapSack(w, v, n, c):
    resultList = []
    result = []
    for i in product(range(2), repeat=n):
        resultList.append(i)
    resultList.reverse()
    for i in resultList:
        flag = True
        for j in range(len(i)):
            if i[j] == 1:
                c -= w[j]
                if c < 0:
                    flag = False
        if flag == True:
            result.append(i)
        c = C

    return result

if __name__ == '__main__':
    w = [20, 15, 10]
    v = [20, 30, 25]
    n = 3
    global C
    C = 25

    result = KnapSack(w, v, n, C)
    print "解空间为:", result
    value = []
    for i in result:
        va = 0
        for j in range(len(i)):
            if i[j] == 1:
                va += v[j]
        value.append(va)
    print "解空间中每个背包的价值分别为:", value
