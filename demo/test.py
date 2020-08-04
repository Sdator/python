# -*- coding: utf-8 -*-

# from collections.abc import Iterable


def a(b, *a, **data):
    # print(11, b, a, type(a), data, type(data))
    print(11, b, a, type(a), data, type(data))
    c(data)


def c(cc=22, aa=44, bb=56, a=1, b=543, c=45):
    print(22, cc, aa, bb, a, b, c)


b = {"a": 'b', 'b': 2, 'c': 3}

bb = [111, 5644]
c(*bb, 4445, **b)


# a = [1, 1, 1]
# b = [2, 2, 2]
# c = [3, 3, 3]

# arr = []

# for i in range(len(a)):
#     print(i)
#     arr.append({a[i], b[i], c[i]})

# print(arr)


# print(next(abc), 11)
# print(next(abc), 22)

# print(abc, isinstance(abc, Iterable), type(abc))
