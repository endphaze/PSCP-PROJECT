"""PointInCircle"""

import math


def day():
    """PointInCircle"""
    price_goods = float(input())
    years = int(input())
    for _ in range(years):
        price_goods = float((str(price_goods)[:str(price_goods).find('.')+3]))
        print(f"debug log : {price_goods}")
    print((str(price_goods)[:str(price_goods).find('.')+3]))


day()
