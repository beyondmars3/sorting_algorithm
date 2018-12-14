#! /usr/bin/env python
# -*- coding: utf-8 -*-


import random
import time


"""
本文演示快速排序的python实现
这是一种分治思想
复杂度 O(nlogn)
参考文章 https://www.cnblogs.com/onepixel/p/7674659.html
"""


def run(arr):
    """

    :param arr:
    :return:
    """
    less = []
    pivotList = []
    more = []
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    for i in arr:
        if i < pivot:
            less.append(i)
        elif i > pivot:
            more.append(i)
        else:
            pivotList.append(i)

    # less = run(less)  # 得到第一轮分组之后，继续将分组进行下去。
    # more = run(more)
    return run(less) + pivotList + run(more)


if __name__ == '__main__':
    """ main """

    data = [random.randint(1, 1000) for _ in xrange(100)]
    # data = [36, 22, 86, 99, 32, 9, 26, 93, 48, 27]
    result = run(data)

    print result
