numbers = {10, 20, 30, 40, 50}

# remove() removes the element, but raises KeyError
# if the element does not exist.
numbers.remove(30)
print("After remove():", numbers)

# discard() removes the element, but does NOT raise an error
# if the element does not exist.
numbers.discard(100)
print("After discard():", numbers)
