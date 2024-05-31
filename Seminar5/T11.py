from time import time

def decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        res = func(args[0], args[1])
        end_time = time()
        return res, end_time - start_time
    return wrapper

#@decorator
def power_x(x, y):
    return x ** y

#print(power_x(2, 3))

print(decorator(power_x)(2, 3))