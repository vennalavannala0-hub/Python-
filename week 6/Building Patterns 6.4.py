# Building Patterns

import re

# Pattern for valid Python variable names
variable_pattern = r'^[A-Za-z_][A-Za-z0-9_]*$'
test_variables = ["_count2", "2fast", "total_sum"]

for var in test_variables:
    if re.fullmatch(variable_pattern, var):
        print(f"'{var}' is a valid Python variable name.")
    else:
        print(f"'{var}' is NOT a valid Python variable name.")

# Pattern for matching "cat", "dog", or "bird"
pet_pattern = r'\b(cat|dog|bird)\b'
sentence = "I have a cat and a dog, but not a bird."
pets = re.findall(pet_pattern, sentence)
print("Pets found in the sentence:", pets)

# Pattern for matching hexadecimal color codes
hex_color_pattern = r'#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})\b'
test_colors = ["#FFAA00", "#000", "#123456", "#abc",
    "#12345", "#GHIJKL"]

for color in test_colors:
    if re.fullmatch(hex_color_pattern, color):
        print(f"'{color}' is a valid hexadecimal color code.")
    else:
        print(f"'{color}' is NOT a valid hexadecimal color code.")

# Pattern for parsing log lines
log_pattern = r'(?P<date>\d{4}-\d{2}-\d{2}) (?P<time>\d{2}:\d{2}:\d{2}) (?P<level>[A-Z]+) (?P<message>.+)'
log_line = "2024-06-01 08:15:32 ERROR Disk full"
match = re.fullmatch(log_pattern, log_line)
if match:
    print("Parsed log line:")
    print(f"  Date: {match.group('date')}")
    print(f"  Time: {match.group('time')}")
    print(f"  Level: {match.group('level')}")
    print(f"  Message: {match.group('message')}")