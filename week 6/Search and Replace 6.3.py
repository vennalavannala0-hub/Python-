# # Search and Replace

import re

def redact_emails(text):
    return re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', '[EMAIL HIDDEN]', text)

def convert_name_format(name):
    return re.sub(r'(\w+),\s*(\w+)', r'\2 \1', name)

def double_numbers(match):
    return str(int(match.group()) * 2)

def collapse_punctuation(text):
    return re.subn(r'([.!?])\1+', r'\1', text)