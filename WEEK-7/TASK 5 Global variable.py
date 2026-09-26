counter = 0  # Global variable


def show_local():
    counter = 10  # Local variable
    print("Local counter:", counter)


show_local()

print("Global counter:", counter)


counter = 0


def increment_counter():
    global counter
    counter += 1


for i in range(5):
    increment_counter()
    print("Counter after call", i + 1, ":", counter)




    counter = 10


# This function causes UnboundLocalError
def wrong_function():
    counter += 1
    print(counter)


print("Calling wrong_function():")
try:
    wrong_function()
except UnboundLocalError as e:
    print("Error:", e)


# Fixed version using global
def correct_function():
    global counter
    counter += 1
    print("Counter after correction:", counter)


print("\nCalling correct_function():")
correct_function()


def make_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


counter = make_counter()

print("First call:", counter())
print("Second call:", counter())
print("Third call:", counter())
print("Fourth call:", counter())


balance = 1000


def deposit(amount):
    global balance
    if amount > 0:
        balance += amount
        print("Amount deposited:", amount)
        print("Updated balance:", balance)
    else:
        print("Invalid deposit amount.")


def withdraw(amount):
    global balance

    if amount <= 0:
        print("Invalid withdrawal amount.")
    elif amount > balance:
        print("Insufficient funds.")
    else:
        balance -= amount
        print("Amount withdrawn:", amount)
        print("Updated balance:", balance)


while True:
    print("\n===== Bank Account Menu =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        deposit(amount)

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        withdraw(amount)

    elif choice == "3":
        print("Current balance:", balance)

    elif choice == "4":
        print("Thank you for using the bank account system.")
        break

    else:
        print("Invalid choice. Please try again.")