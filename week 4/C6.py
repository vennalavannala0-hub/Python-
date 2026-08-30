student = {
    "name": "Rahul",
    "age": 20,
    "course": "Python"
}

# Print all keys
print("Keys:")
for key in student.keys():
    print(key)

# Print all values
print("\nValues:")
for value in student.values():
    print(value)

# Print all key-value pairs
print("\nKey-Value Pairs:")
for key, value in student.items():
    print(key, ":", value)
