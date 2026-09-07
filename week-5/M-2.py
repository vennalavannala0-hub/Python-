s = input("Enter a string: ")

result = ""

for char in s:
    if not char.isspace():
        result += char

print("String without whitespace:", result)