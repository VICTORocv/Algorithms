# -*- coding: utf-8 -*-
__author__ = 'Victor'
import numpy as np
import time

#分治法解决循环赛日程表安排问题

def match(k):
    time_start = time.time()
    for i in range(1,k):
        half=2**i
        #左下角的子表中项为左上角子表对应项加2**i
        for row in range(half):
            for col in range(half):
                a[row+half][col]=a[row][col]+half

        # 右上角的子表等于左下角子表
        for row in range(half):
            for col in range(half):
                a[row][col+half]=a[row+half][col]

        # 右下角的子表等于左上角的子表
        for row in range(half):
            for col in range(half):
                a[row+half][col+half]=a[row][col]
    time_end = time.time()

    print "当k = %d、n = %d 时，矩阵如下，运行时间为：%fs" % (k, 2**k, time_end - time_start)
    np.set_printoptions(threshold='nan')
    print a

if __name__ == '__main__':
    for k in range(3,6):
        n = 2**k
        a = np.zeros((n,n))
        a[0][0] = 1
        a[1][1] = 1
        a[1][0] = 2
        a[0][1] = 2
        match(k)
