"""Circular I"""

import math


def main():
    """Circular I"""
    my_x = float(input())
    my_y = float(input())
    radius = float(input())
    enemy_x = float(input())
    enemy_y = float(input())
    new_x = my_x - enemy_x
    new_y = my_y - enemy_y
    enemy_distance = math.sqrt(new_x**2 + new_y**2)
    if enemy_distance > radius:
        print("No")
    else:
        print("Yes")


main()
