# Date Extraction and Reformatting

# Given text containing dates in DD/MM/YYYY format, extract all of them with re.findall() using groups,
# then use re.sub() with back-references to rewrite every date into YYYY-MM-DD (ISO) format.

date_pattern = r'(\d{2})/(\d{2})/(\d{4})'
text = "Today is 01/15/2024 and tomorrow is 01/16/2024."

dates = re.findall(date_pattern, text)
reformatted_dates = [f"{year}-{month}-{day}" for day, month, year in dates]
print("Extracted and reformatted dates:", reformatted_dates)