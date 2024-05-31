"""
На столе лежат n монеток. Некоторые из монеток лежат вверх решкой, а некоторые – гербом. Ваша задача - определить минимальное количество монеток, которые нужно перевернуть, чтобы все монетки лежали одной и той же стороной вверх.

Входные данные:

На вход программе подается список coins, где coins[i] равно 0, если i-я монетка лежит гербом вверх, и равно 1, если i-я монетка лежит решкой вверх. Размер списка не превышает 1000 элементов.

Выходные данные:

Программа должна вывести одно целое число - минимальное количество монеток, которые нужно перевернуть.
"""

coins = [0, 1, 0, 1, 1, 0, 1, 0, 0]

# Введите ваше решение ниже

per_resh = 0
per_gerb = 0

for el in coins:
    if el == 0:
        per_gerb += 1
    else:
        per_resh += 1
        
if per_gerb < per_resh:
    print(per_gerb)
elif per_gerb == per_resh:
    print(per_gerb)
else:
    print(per_resh)