# def uppercase(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args,**kwargs)
#         return result.upper()
#     return wrapper
# @uppercase
# def greet(name):
#     return f"Hello, {name}"
#
#
# result = greet("john")
# print(result)
#
#

#
# import time
#
# def time_decorater(func):
#     def timer_func(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f"{func.__name__} took {end_time - start_time:.2f} seconds to execute")
#         return result
#
#     return timer_func  # Corrected this line (no parentheses)
#
# @time_decorater
# def funcvalu():
#     a = 0
#     for i in range(9999999):
#         a += 5
#
# funcvalu()


