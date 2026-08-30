student = {
    "name": "Rahul",
    "age": 20,
    "course": "Python"
}

key = "age"

if key in student:
    print("Key exists.")
    print("Value:", student[key])
else:
    print("Key does not exist.")
