"""WeightStation"""


def weight():
    """WeightStation"""
    average_weight = float(input())
    half_average = average_weight/2
    weight2 = float(input())
    weight3 = float(input())
    weight4 = float(input())
    weight1 = ((average_weight*4) - weight2 - weight3 - weight4)
    #(average_weight + half_average) - weight1
    if (weight1+weight2+weight3+weight4) > 15000:
        print("Overweight")
    elif abs(average_weight - weight1) > half_average:
        print("Unbalance")
    elif abs(average_weight - weight2) > half_average:
        print("Unbalance")
    elif abs(average_weight - weight3) > half_average:
        print("Unbalance")
    elif abs(average_weight - weight4) > half_average:
        print("Unbalance")
    else:
        print("Pass", "%.2f" % weight1)


weight()
