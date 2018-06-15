# -*- coding: utf-8 -*-
__author__ = 'Victor'
import numpy as np
import sys

#贪心法求解多机调度问题

def MultiMachine(work_time, n, d, m):
    s = []#存储m台机器处理的作业
    timeList = sorted(work_time.items(), key = lambda item:item[1], reverse = True)
    print "按作业处理时间排序后的结果:", timeList
    for w in range(0, m):
        s.append([timeList[w][0]])
        d.append(timeList[w][1])
    for w in range(m, n):
        j = d.index(min(d))
        s[j].append(timeList[w][0])
        d[j] += timeList[w][1]
    print "每个机器处理的作业序号:", s
    print "每个机器处理所有作业的总时长:",d

if __name__ == '__main__':
    n = 7
    work = [1, 2, 3, 4, 5, 6, 7]
    t = [2, 14, 4, 16, 6, 5, 3]
    wt = zip(work, t)
    work_time = dict((w, t) for w, t in wt)
    print "作业序号和处理时间的对应关系:", work_time
    m = 3
    d = []#存储m台机器空闲时间
    MultiMachine(work_time, n, d, m)
