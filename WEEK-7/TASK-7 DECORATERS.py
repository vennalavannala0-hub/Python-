# (a) Assigning a function to another variable

def greet(name):
    return f"Hello, {name}!"

new_greet = greet
print(new_greet("Alice"))


# (b) Passing a function as an argument

def apply_function(func, value):
    return func(value)

result = apply_function(greet, "Bob")
print(result)


# (c) Returning a function from another function

def create_greeting():
    def greeting(name):
        return f"Welcome, {name}!"
    
    return greeting

my_greeting = create_greeting()
print(my_greeting("Charlie"))


def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} args={args} kwargs={kwargs}")

        result = func(*args, **kwargs)

        print(f"{func.__name__} returned {result}")
        return result

    return wrapper


@log_call
def add(a, b):
    return a + b


# Test
result = add(10, 20)
print("Final result:", result)

import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()
        elapsed_time = end_time - start_time

        print(f"{func.__name__} took {elapsed_time:.6f} seconds")

        return result

    return wrapper


@timer
def calculate_sum():
    total = 0

    for i in range(10_000_000):
        total += i

    return total


result = calculate_sum()
print("Sum:", result)

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat(3)
def greet():
    print("Hello! Welcome to Python.")


# Test
greet()


from functools import wraps

is_logged_in = False


def require_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if is_logged_in:
            return func(*args, **kwargs)
        else:
            print("Access denied. Please log in first.")

    return wrapper


@require_login
def view_profile():
    print("Welcome to your profile!")


# Test when user is NOT logged in
print("When logged out:")
is_logged_in = False
view_profile()


# Test when user IS logged in
print("\nWhen logged in:")
is_logged_in = True
view_profile()


import time
from functools import wraps


def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} args={args} kwargs={kwargs}")

        result = func(*args, **kwargs)

        print(f"{func.__name__} returned {result}")
        return result

    return wrapper


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()

        print(f"{func.__name__} took {end_time - start_time:.6f} seconds")

        return result

    return wrapper


@log_call
@timer
def multiply(a, b):
    return a * b


# Test
result = multiply(5, 6)
print("Final result:", result)

