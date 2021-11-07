#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def sredgeometr(*args):
    if args:
        values = [float(arg) for arg in args]

        n = len(values)
        return pow(sum(values), 1 / n)
    else:
        return None


if __name__ == "__main__":
    print(sredgeometr())
    print(sredgeometr(60, 4))
    print(sredgeometr(1, 5, 8, 4, 3, 9))
