# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# def greet(name="Angela", location="Denver"):
#     print(f"Hello {name}\nWhat is it like in {location}")
# greet("Sara", "Shop")
# import math
#
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
#
#
# def paint_calc(height=test_h, width=test_w, cover=coverage):
#     kr = math.ceil((test_h * test_w) / coverage)
#     print(f"You'll need {kr} cans of paint.")
#
#
# paint_calc(test_h, test_w, coverage)

n = 1  # int(input("Check this number: "))


def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


prime_checker(number=n)
