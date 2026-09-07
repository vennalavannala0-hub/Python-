s = input("Enter a string: ")
ch = input("Enter the character to count: ")

count = 0

for char in s:
    if char == ch:
        count += 1

print("Occurrences:", count)