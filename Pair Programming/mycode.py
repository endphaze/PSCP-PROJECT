"""Kangaroo"""


def main():
    """Function Main"""

    kang1 = int(input())
    kang2 = int(input())
    kang3 = int(input())

    dist = max((kang2-kang1)-1, (kang3-kang2)-1)
    print(dist)


main()
