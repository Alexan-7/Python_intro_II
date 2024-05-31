"""
Задача №9. Решение в группах
По данному целому неотрицательному n вычислите
значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
чисел от 1 до N) 0! = 1 Решить задачу используя цикл
while
Input: 5
Output: 120
"""

# n = int(input("Введите число и мы найдём его факториал: "))
# factorial = 1
# while n > 1: # идем в сторону уменьшения
#     factorial *= n
#     n -= 1
# print(factorial)

# for el in range(1, n):
#     factorial *= n
#     n -= 1
# print(factorial)
num = 5
f = 1

def factoriall(num, f = 1):
    if num == 0:
        return f
    return factoriall(num - 1, f*num)

print(factoriall(num))