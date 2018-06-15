# -*- coding: utf-8 -*-
__author__ = 'Victor'
import numpy as np

#动态规划法求解 0/1 背包问题

def KnapSack(w, v, n, c):
    i = 0
    V = np.zeros((n+1, c+1))
    for j in range(c+1):
        V[0][j] = 0
    for i in range(1, n+1):
        for j in range(1, c+1):
            V[i][j] = V[i-1][j]
            if j>= w[i-1] and V[i][j] < V[i-1][j-w[i-1]] + v[i-1]:
                V[i][j] = V[i-1][j-w[i-1]] + v[i-1]

    return V

if __name__ == '__main__':
    w = [2, 2, 6, 5, 4]
    v = [6, 3, 5, 4, 6]
    n = 5
    C = 10

    result = KnapSack(w, v, n, C)
    print result
