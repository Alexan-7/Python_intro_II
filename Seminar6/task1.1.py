lst_1 = [3, 1, 3, 4, 2, 4, 12]
lst_2 = [4, 15, 43, 1, 15, 1]
# традиционный итератор с функцией append
res = []
for elem in lst_1:
    if elem not in lst_2:
        res.append(elem)
print(res)

# list comprehension
print([elem for elem in lst_1 if elem not in lst_2])
print(*list(filter(lambda x: x not in lst_2, lst_1)))

# включение списковое, множественное, словарное