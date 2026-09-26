def build_profile(**details):
    """Print a neatly formatted profile card using keyword arguments."""
    print("\n--- Profile Card ---")

    for key, value in details.items():
        print(f"{key.capitalize()}: {value}")

    print("--------------------")


# First profile
build_profile(
    name="Asha",
    age=20,
    city="Hyderabad",
    hobby="Reading"
)

# Second profile with a different set of details
build_profile(
    name="Ravi",
    age=21,
    course="Computer Science",
    hobby="Cricket"
)

# Third profile
build_profile(
    name="Priya",
    city="Mumbai",
    hobby="Painting",
    language="Python"
)