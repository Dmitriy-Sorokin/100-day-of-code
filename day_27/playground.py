def add(*args):
    total_value = 0
    for num in args:
        total_value += num
    return total_value


# print(add(3, 5, 6))


def calculate(n, **kwargs):
    n *= kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)
