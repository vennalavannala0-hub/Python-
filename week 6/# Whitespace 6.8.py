# Whitespace and HTML Clean
def clean_text(html):
    # Strip HTML tags
    clean = re.sub(r'<[^>]+>', '', html)
    # Collapse multiple whitespace characters
    clean = re.sub(r'\s+', ' ', clean)
    # Trim leading and trailing whitespace
    return clean.strip()