#!/usr/bin/env python3
# -*- coding: utf-8 -*-


a = int(input())
b = int(input())
c = int(input())

m = a
if m < b:
    m = b
if m < c:
    m = c

print(m)

n = a
if n > b:
    n = b
if n > c:
    n = c

print(n)