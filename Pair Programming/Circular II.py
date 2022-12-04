"""Circular II"""

import math


def main():
    """Circular II"""
    my_x = float(input())
    my_y = float(input())
    radius1 = float(input())
    friend_x = float(input())
    friend_y = float(input())
    radius2 = float(input())
    new_x = my_x - friend_x
    new_y = my_y - friend_y
    friend_distance = math.sqrt(new_x**2 + new_y**2)
    if friend_distance >= radius1 + radius2:
        print("No")
    else:
        print("Yes")


main()
