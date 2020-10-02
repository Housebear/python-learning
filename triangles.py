#!/usr/bin/python3
# -*- coding:utf-8 -*-

# File Name: triangles.py
# Author: Lipsum
# Mail: niuleipeng@gmail.com
# Created Time: 2020-10-02 15:42:17


def triangles():
    L = [1]

    while True:
        yield L
        L = [0] + L + [0]
        L = [L[i] + L[i+1] for i in range(len(L) - 1)]

n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')