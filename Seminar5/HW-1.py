"""
Задача 26: Напишите программу, которая на вход принимает
два числа A и B, и возводит число А в целую степень B с
помощью рекурсии.
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8
"""

# def f_1(a, b):
#     res = 1
#     for _ in range(b):
#         res *= a
#     return res

def f(a, b, res = 1):
    if b == 0:
        return res
    return f(a, b - 1, res * a)

a = 3
b = 5
print(f(a, b))