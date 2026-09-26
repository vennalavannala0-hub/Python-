def student_info(name, roll_no, branch):
    """Print the details of a student."""
    print("Name:", name)
    print("Roll No:", roll_no)
    print("Branch:", branch)


# Calling using positional arguments
print("Using Positional Arguments:")
student_info("Asha", 101, "CSE")

print()

# Calling using keyword arguments in a different order
print("Using Keyword Arguments:")
student_info(branch="CSE", name="Asha", roll_no=101)