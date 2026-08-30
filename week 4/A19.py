numbers = [5, -2, 8, -7, 3, -1, 10]

result = [0 if number < 0 else number for number in numbers]

print("Original list:", numbers)
print("Modified list:", result)
