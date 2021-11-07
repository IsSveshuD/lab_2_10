#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def sm(*args):
    if args:
        values = [float(arg) for arg in args]
        print(sum(map(abs, values[values.index(0) + 1:])))
    else:
        return None


if __name__ == "__main__":
    print(sm())
    print(sm(3, 0, 0, -6, 9))
    print(sm(1, 0, 0, 4, 3, 9))
