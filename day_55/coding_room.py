def logging_decorator(func):
    def wrapper(*args):
        print(f"You called {func.__name__}")
        result = func(*args)
        print(f"It returned: {result}")

    return wrapper


@logging_decorator
def plus_name_func(a, b, c):
    return a + b + c


plus_name_func(1, 2, 3)
