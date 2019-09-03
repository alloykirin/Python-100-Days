#!/usr/bin/env python3
# -*- coding: utf-8 -*-

for i in range(1, 6):
    print('*' * i)

for i in range(1, 6):
    print(' ' * (5 - i) + '*' * i)

for i in range(1, 6):
    print(' ' * (5 - i) + '*' * (2 * i - 1))