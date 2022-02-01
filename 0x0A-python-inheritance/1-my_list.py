#!/usr/bin/python3

"""
class
   MyList
"""


class MyList(list):
    """
    class MyList
    """

    def print_sorted(self):
        """
        Function that prints a list, sorted (asceding sort).
        Args:
            self: Mylist
        """
        print(sorted(self))
