#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def garmony(*args):
    if args:
        values = [float(arg) for arg in args]
        p = 1
        n = len(values)
        for value in values:
            p *= value
        return n / (sum(values) / p)
    else:
        return None


if __name__ == "__main__":
    print(garmony())
    print(garmony(60, 4))
    print(garmony(1, 5, 8, 4, 3, 9))
