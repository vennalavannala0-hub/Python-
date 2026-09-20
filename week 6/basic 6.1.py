# #Basic Pattern Matching

import re
sentence = "1024 requests were served in 3 seconds"
pattern = r"\d"

# Test if the sentence starts with a digit
if re.match(pattern, sentence):
    print("The sentence starts with a digit.")
else:
    print("The sentence does not start with a digit.")

# Find the word "served" and print its position
match = re.search(r"served", sentence)
if match:
    print(f"The word 'served' is found at position {match.span()}.")

# Check if "12345" consists only of digits
if re.fullmatch(r"\d+", "12345"):
    print("The string '12345' consists only of digits.")

# Check if "123a5" consists only of digits
if re.fullmatch(r"\d+", "123a5"):
    print("The string '123a5' consists only of digits.")
else:
    print("The string '123a5' contains non-digit characters.");