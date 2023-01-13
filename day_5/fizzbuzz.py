for score in range(1, 101):
    if score % 3 == 0 and score % 5 == 0:
        print("FizzBuzz")
    elif score % 5 == 0:
        print("Buzz")
    elif score % 3 == 0:
        print("Fizz")
    else:
        print(score)
