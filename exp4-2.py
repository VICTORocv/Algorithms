# -*- coding: utf-8 -*-
__author__ = 'Victor'
import numpy as np

#回溯法求解八皇后问题

def place(x, k): #判断是否冲突
    for i in range(1, k):
        if x[i] == x[k] or abs(x[i] - x[k]) == abs(i - k):
            return False
    return True

def queens(n):
    k = 1    #设置初始皇后为第一个
    x = [0 for row in range(n + 1)]# 设置x列表初始值为0
    while k > 0:
        x[k] = x[k] + 1 # 在当前列的下一列开始
        while (x[k] <= n) and (not place(x, k)): # 不满足条件，继续搜索下一列位置
            x[k] = x[k] + 1
        if x[k] <= n:# 判断是否为最后一个，不是就执行下一行
            if k == n:# 是最后一个皇后，退出
                break
            else: # 不是，则处理下一行皇后
                k = k + 1   #执行下一行
                x[k] = 0    #初始化，从第一列开始
        else:#n列均不满足，回溯到上一行
            x[k] = 0    #初始化列到第一列
            k = k - 1   #回溯到上一行
    return x[1:]    #返回1-8个皇后的位置
print("八个皇后的位置分别为:")
print(queens(8))
