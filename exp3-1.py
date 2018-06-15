# -*- coding: utf-8 -*-
__author__ = 'Victor'
import numpy as np
import sys

#贪心法求解Tsp问题最近临点策略

def Tsp(start, arc):
    #start为开始和结束的节点；节点数字从1-5
    way = []
    way.append(start)
    for e in range(len(arc)):
        m = arc[start][:]
        for n in way:
            m[n] = sys.maxint
        next = m.index(min(m))
        way.append(next)
        start = next

    return way

if __name__ == '__main__':
    arc = [[sys.maxint, 3, 3, 2, 6],
    [3, sys.maxint, 7, 3, 2],
    [3, 7, sys.maxint, 2, 5],
    [2, 3, 2, sys.maxint, 3],
    [6, 2, 5, 3, sys.maxint]]
    way = Tsp(0, arc)
    #计算路径长度
    length = 0
    for i in range(0, 5):
        length += arc[way[i]][way[i+1]]
    #way中的节点数字是从0-4的，对way列表中每个元素加一，对应节点1-5
    way = [i+1 for i in way]
    print "路径为:", way
    print "路径长度为:", length
