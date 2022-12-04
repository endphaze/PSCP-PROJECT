"""BTSMRT"""

def main():
    """2354234234"""
    this_day = input()
    customer_age = float(input())
    customer_height = float(input())

    if this_day == "Normal Day":
        if customer_age < 14 and customer_height < 90:
            print("FREE")
        else:
            print("PAY")

    if this_day == "Children Day":
        if customer_age < 14 and customer_height <= 140:
            print("FREE")
        else:
            print("PAY")

    if this_day == "Senior Day":
        if customer_age >= 60:
            print("FREE")
        else:
            print("PAY")

main()