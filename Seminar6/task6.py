"""
Задание 32.
✔ Напишите функцию, которая принимает строку текста.
✔ Сформируйте список с уникальными кодами Unicode каждого
символа введённой строки отсортированный по убыванию.

Решите через lc
"""

def func(data):
    return sorted(set([ord(el) for el in data])), reverse=True)

print(func())