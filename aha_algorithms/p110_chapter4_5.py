#!/usr/bin/env python
# -*- coding:utf-8 -*-


land_map = """
1 2 1 0 0 0 0 0 2 3
3 0 2 0 1 2 1 0 1 2
4 0 1 0 1 2 3 2 0 1
3 2 0 0 0 1 2 4 0 0
0 0 0 0 0 0 1 5 3 0
0 1 2 1 0 1 5 4 3 0
0 1 2 3 1 3 6 2 1 0
0 0 3 4 8 9 7 5 0 0
0 0 0 3 7 8 6 0 1 2
0 0 0 0 0 0 0 0 1 0
"""
land_map = [[int(j) for j in i.split(' ')]for i in land_map.split('\n') if i]
book = [[0 for i in range(10)] for j in range(10)]
_sum = 1

def dfs(x, y):
    global _sum
    _next = [
        [0, 1],
        [1, 0],
        [0, -1],
        [-1, 0],
    ]
    for i in range(4):
        tx = x + _next[i][0]
        ty = y + _next[i][1]
        if tx<0 or tx>edge-1 or ty<0 or ty>edge-1:
            continue
        if land_map[tx][ty] > 0 and book[tx][ty] == 0:
            _sum += 1
            book[tx][ty] = 1
            dfs(tx, ty)

edge, startx, starty= (10, 5, 7)
book[startx][starty] = 1
dfs(startx, starty)
print "land size: %d" % _sum

