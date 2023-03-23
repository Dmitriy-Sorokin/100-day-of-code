import time


def speed_calc_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        difference_time = end_time - start_time
        return print(f"{func.__name__} run speed: {difference_time} sec")

    return wrapper


@speed_calc_decorator
def fast_function(r):
    for i in range(10000000):
        i * r


@speed_calc_decorator
def slow_function(r):
    for i in range(100000000):
        i * r


fast_function()
slow_function()

# def speed_calc_decorator(function):
#     def wrapper_function():
#         start_time = time.time()
#         function()
#         end_time = time.time()
#         print(f"{function.__name__} run speed: {end_time - start_time}s")
#
#     return wrapper_function
#
#
# @speed_calc_decorator
# def fast_function():
#     for i in range(10000000):
#         i * i
#
#
# @speed_calc_decorator
# def slow_function():
#     for i in range(100000000):
#         i * i
#
#
# fast_function()
# slow_function()
