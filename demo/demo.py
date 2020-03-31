# -*- coding: utf-8 -*-
import re

if __name__ == "__main__":
    aa = [{"var": 1, "name": 1, "cbvar": 1, "nameda": 1, "aename": 1}, {"nameb": 2}]

    # bb = {"a": 1, "b": 1, "c": 1, "d": 1, "e": 1}
    bb = {k: v for k, v in aa[0].items() if re.match(r'^var$|^name$', k)}
    # print(bb.items())

    # for k, v in bb.items():
    #     print(k, v)

    # bb = [k for k, v in aa[0]]

    # new_dict = {key:val for key, val in test_dict.items() if key != 'Zhihu'}

    print(bb)
    # print(aa,type(aa))
