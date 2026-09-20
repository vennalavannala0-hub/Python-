#  Email Validatity
def is_valid_email(s):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$'
    return bool(re.fullmatch(pattern, s))

# Test cases
valid_emails = ["user@example.com", "test.email@domain.co.uk", "a@b.c", "user123@test-domain.org"]
invalid_emails = ["no-at-sign.com", "user@domain", "user..user@domain.com", "user@domain."]

for email in valid_emails:
    print(f"'{email}' is valid: {is_valid_email(email)}")

for email in invalid_emails:
    print(f"'{email}' is valid: {is_valid_email(email)}");