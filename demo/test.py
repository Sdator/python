# -*- coding: utf-8 -*-

from collections.abc import Iterable

abc = [v*v for v in range(10)]


# print(next(abc), 11)
# print(next(abc), 22)


print(abc, isinstance(abc, Iterable), type(abc))
