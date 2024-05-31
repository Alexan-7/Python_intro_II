"""
Задача №1. Решение в группах
За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут 
длиной m километров? При решении этой задачи нельзя пользоваться условной 
инструкцией if и циклами.

Input:
n = 700
m = 750
Output:
2
"""

# from math import ceil
# m, n = 800, 700
# print(ceil(m/n))
"""
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
"""

# n = 385916
# if n // 100000 + n // 10000 % 10 + n // 1000 % 10 == n // 100 % 10 + n // 10 % 10 + n % 10:
#     print('yes')
# else:
#     print('no')

"""
Определите, можно ли от шоколадки размером a × b долек отломить c долек, 
если разрешается сделать один разлом по прямой между дольками (то есть разломить 
шоколадку на два прямоугольника).
"""

a = 3
b = 2
c = 1

if (c % b == 0 or c % a == 0):
    print("yes")
else:
    print("no")