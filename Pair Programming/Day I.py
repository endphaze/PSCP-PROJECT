"""Day I"""


def day():
    """Day I"""
    my_year = int(input())
    if ((my_year % 4 == 0) and (my_year % 100 != 0)) or ((my_year % 4 == 0) and \
        (my_year % 100 == 0) and (my_year % 400 == 0)):
        print("Yes")
    else:
        print("No")


day()