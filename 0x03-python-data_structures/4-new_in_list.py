#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    Rep = my_list[:]
    if idx >= 0 and idx < len(Rep):
        Rep[idx] = element
    return Rep
