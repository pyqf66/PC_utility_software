# -*- coding:utf-8 -*-
import random
import sys


def get_random_number(begin_num, last_num):
    num = int((last_num - begin_num) * random.random() + begin_num)
    return num


def condition_gennerator(count, begin_num, last_num):
    for i in range(int(count)):
        print(get_random_number(int(begin_num), int(last_num)))

if len(sys.argv) == 1:
    condition_gennerator(11, 1, 10)
else:
    condition_gennerator(sys.argv[1], sys.argv[2], sys.argv[3])
wait = input()
