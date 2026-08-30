dict1 = {"name": "Rahul", "age": 20}
dict2 = {"course": "Python", "city": "Hyderabad"}

# Merge using update()
merged_dict1 = dict1.copy()
merged_dict1.update(dict2)

print("Using update():", merged_dict1)

# Merge using | operator
merged_dict2 = dict1 | dict2

print("Using | operator:", merged_dict2)
