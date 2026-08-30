student = {
    "name": "Rahul",
    "age": 20,
    "course": "Python"
}

# Remove an existing key using pop()
removed_value = student.pop("age")
print("Removed value:", removed_value)
print("After pop():", student)

# Safely check/remove a key that may not exist
key = "phone"

if student.get(key, None) is not None:
    student.pop(key)
else:
    print("Key", key, "does not exist.")

print("Final dictionary:", student)
