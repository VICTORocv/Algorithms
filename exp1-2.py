# -*- coding: utf-8 -*-
__author__ = 'Victor'
import numpy as np
import time, random, math
import pylab as pl

#最近点对问题，分治法和蛮力法两种方法求解

#计算两点的距离
def calDis(seq):
    dis=math.sqrt((seq[0][0]-seq[1][0])**2+(seq[0][1]-seq[1][1])**2)
    return dis

#生成器：生成横跨跨两个点集的候选点
def candidateDot(u,right,dis,med_x):
    cnt=0
    #遍历right（已按横坐标升序排序）。若横坐标小于med_x-dis则进入下一次循环；若横坐标大于med_x+dis则跳出循环；若点的纵坐标好是否落在在[u[1]-dis,u[1]+dis]，则返回这个点
    for v in right:
        if v[0]<med_x-dis:
            continue
        if v[0]>med_x+dis:
            break
        if v[1]>=u[1]-dis and v[1]<=u[1]+dis:
            yield v

#求出横跨两个部分的点的最小距离
def combine(left,right,resMin,med_x):
    dis=resMin[1]
    minDis=resMin[1]
    pair=resMin[0]
    for u in left:
        if u[0]<med_x-dis:
            continue
        for v in candidateDot(u,right,dis,med_x):
            dis=calDis([u,v])
            if dis<minDis:
                minDis=dis
                pair=[u,v]
    return [pair,minDis]


#分治求解
def divide(seq):
    #求序列元素数量
    n=len(seq)
    #按点的纵坐标升序排序
    seq=sorted(seq)
    #递归开始进行
    if n<=1:
        return None,float('inf')
    elif n==2:
        return [seq,calDis(seq)]
    else:
        half=int(len(seq)/2)
        med_x=(seq[half][0]+seq[-half-1][0])/2
        left=seq[:half]
        resLeft=divide(left)
        right=seq[half:]
        resRight=divide(right)
        #获取两集合中距离最短的点对
        if resLeft[1]<resRight[1]:
            resMin=combine(left,right,resLeft,med_x)
        else:
            resMin=combine(left,right,resRight,med_x)
        pair=resMin[0]
        minDis=resMin[1]
    return [pair,minDis]


#蛮力法
def calDirect(seq):
    minDis=float('inf')
    pair=[]
    for i in range(len(seq)):
        for j in range(i+1,len(seq)):
            dis=calDis([seq[i],seq[j]])
            if dis <minDis:
                minDis=dis
                pair=[seq[i],seq[j]]
    return [pair,minDis]


if __name__ == '__main__':
    seq=[(random.uniform(0,10),random.uniform(0,10)) for x in range(30)]
    for e in seq:
        pl.plot(e[0], e[1], 'bo')
    list = []
    time_start = time.time()
    list = divide(seq)
    time_end = time.time()
    print "距离最近的点对为：%s和%s，它们之间的距离是%f" % (list[0][0], list[0][1], list[1])
    print "分治法求解时间：%fs" % (time_end - time_start)
    time_start = time.time()
    list2 = calDirect(seq)
    time_end = time.time()
    print "蛮力法求解的时间：%fs" % (time_end - time_start)
    pl.plot(list[0][0][0], list[0][0][1], 'ro')
    pl.plot(list[0][1][0], list[0][1][1], 'ro')
    x1 = [list[0][0][0], list[0][1][0]]
    x2 = [list[0][0][1], list[0][1][1]]
    pl.plot(x1, x2, 'r')
    pl.show()
