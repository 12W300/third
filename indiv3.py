#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':

    N = int(input())

    for d in range(1, N):
        if N % d == 0:
            print(d, ' ', end='')
    print(N)
