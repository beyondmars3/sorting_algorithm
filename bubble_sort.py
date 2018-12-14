#! /usr/bin/python
# -*- coding: utf-8 -*-

import random
import time

"""
本文演示冒泡排序
这个算法的名字由来是因为越小的元素会经由交换慢慢“浮”到数列的顶端。
复杂度 O(n**2)
参考文章：https://www.cnblogs.com/onepixel/p/7674659.html
"""

import random
import time


def run(data):
    """

    :param data:
    :return:
    """
    for _x in range(len(data) - 1):
        for _y in range(_x+1, len(data)):
            if data[_x] > data[_y]:
                data[_x], data[_y] = data[_y], data[_x]

    return data


if __name__ == '__main__':
    """  """
    data = [random.randint(1, 100) for _ in xrange(10)]
    result = run(data)
    print result

