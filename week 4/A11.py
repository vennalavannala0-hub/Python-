numbers = [5, 2, 8, 2, 1]

# append()
numbers.append(10)
print("After append():", numbers)

# insert()
numbers.insert(1, 7)
print("After insert():", numbers)

# extend()
numbers.extend([3, 6])
print("After extend():", numbers)

# remove()
numbers.remove(2)
print("After remove():", numbers)

# pop()
numbers.pop()
print("After pop():", numbers)

# sort()
numbers.sort()
print("After sort():", numbers)

# reverse()
numbers.reverse()
print("After reverse():", numbers)

# count()
print("Count of 2:", numbers.count(2))
print("List after count():", numbers)

# index()
print("Index of 7:", numbers.index(7))
print("List after index():", numbers)
