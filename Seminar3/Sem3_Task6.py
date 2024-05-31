list_1 = [5, 10, 653, 876, 3, 0]
last = list_1.pop()
first = list_1.pop(0)

list_1.insert(0, last)
list_1.append(first)

print(list_1)