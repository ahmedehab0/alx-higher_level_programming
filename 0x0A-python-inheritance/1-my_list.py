#!/usr/bin/python3

"""module that defines Mylist class"""


class MyList(list):
    """Mylist class that inherits from the built in fuction list."""

    def print_sorted(self):
        """print_sorted method: prints a sorted list"""

        print(sorted(self))
