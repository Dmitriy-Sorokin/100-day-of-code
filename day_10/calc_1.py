def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divine(n1, n2):
    return n1 / n2


operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divine
}

num1 = 2  # int(input("first number"))
num2 = 4  # int(input("second number"))

for op in operators:
    print(op)
operator_symbols = "+"  # input("operator symbol ")

calc_func = operators[operator_symbols]


print(f"{num1}{operator_symbols}{num2}= {operators[operator_symbols](num1, num2)} ")
