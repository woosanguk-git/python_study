from decimal import Decimal



if __name__ == "__main__":
    print(sum(0.1 for i in range(10)) == 1.0)
    print(sum(Decimal("0.1") for i in range(10)) == Decimal("1.0"))
    num = 0.1
    num_s = "0.1"
    print(num)
    print(Decimal(num))
    print(num_s)
    print(Decimal(num_s))
    print(sum(0.1 for i in range(10)))