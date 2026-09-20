#  Password Strength Checker

import re

def check_password(pw):
    failed_rules = []
    
    # Check length
    if len(pw) < 8:
        failed_rules.append("Password must be at least 8 characters long")
    
    # Check for uppercase letter
    if not re.search(r'[A-Z]', pw):
        failed_rules.append("Password must contain at least one uppercase letter")
    
    # Check for lowercase letter
    if not re.search(r'[a-z]', pw):
        failed_rules.append("Password must contain at least one lowercase letter")
    
    # Check for digit
    if not re.search(r'\d', pw):
        failed_rules.append("Password must contain at least one digit")
    
    # Check for symbol
    if not re.search(r'[!@#$%^&*]', pw):
        failed_rules.append("Password must contain at least one symbol from !@#$%^&*")
    
    return failed_rules