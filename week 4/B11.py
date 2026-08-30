data = ("Python", [10, 20, 30], "Programming")

# Modify the nested list
data[1].append(40)

print(data)

# This is possible because the tuple is immutable, but the list inside it
# is mutable. The tuple still contains the same list object; only the
# contents of that list have been changed.
