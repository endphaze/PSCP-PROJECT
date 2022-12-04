"""Frame"""


def main():
    """Frame"""
    inp = int(input())

    SpaceCounter = (inp*3)-3
    Counter = 1
    BackCounter = 0

    for i in range(inp):
        for Space in range(SpaceCounter):
            print(" ", end="")
        for l in range(1, Counter+1):
            print("{:02d}".format(l), end=" ")
        for e in range(BackCounter, 0, -1):
            print("{:02d}".format(e), end=" ")
        SpaceCounter -= 3
        Counter += 1
        BackCounter += 1
        if Counter-1 < inp:
            print("\n",end="")

main()
