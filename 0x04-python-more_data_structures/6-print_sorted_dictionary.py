#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for s in sorted(a_dictionary.keys()):
        print("{:s}: {}".format(s, a_dictionary[s]))
