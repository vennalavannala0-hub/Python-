# Phone Number Extractor

# Given a block of text containing phone numbers in mixed formats (555-123-4567, (555) 123-4567,

# 555.123.4567), write a single pattern that extracts all of them regardless of format, and normalize each
# result to 555-123-4567 style using re.sub().

phone_pattern = r'\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})'

text = "Call me at 555-123-4567 or (555) 123-4567 or 555.123.4567"
phone_numbers = re.findall(phone_pattern, text)

normalized_numbers = [f"{area}-{prefix}-{line}" for area, prefix, line in phone_numbers]
print("Extracted and normalized phone numbers:", normalized_numbers)