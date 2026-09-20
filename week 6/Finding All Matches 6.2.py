# #  Finding All Matches
import re

paragraph = "NASA and USA are both countries. The USA has a large economy."
capital_words = re.findall(r"\b[A-Z]+\b", paragraph)
print("Capital words:", capital_words)

long_words = re.finditer(r"\b\w{7,}\b", paragraph)
print("Long words and their positions:")
for match in long_words:
    print(f"  '{match.group()}' at index {match.start()}")

prices = "apples: $3.50, bananas: $1.20, mango: $4.75"
dollar_amounts = re.findall(r"\$\d+\.\d+", prices)
print("Dollar amounts:", dollar_amounts)

print("Number of dollar amounts found:", len(dollar_amounts))