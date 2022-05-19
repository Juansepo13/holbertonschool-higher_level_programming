#!/usr/bin/python3
def uniq_add(my_list=[]):
        num = 0
        for i in list(set(my_list)):
            num += i
        return num
