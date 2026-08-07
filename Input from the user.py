# Input from the user
first_name = input("Enter first name: ")
roll_number = input("Enter roll number: ")

# Generate username
username = first_name.lower() + roll_number[-2:]

# Display the username
print("Generated Username:", username)