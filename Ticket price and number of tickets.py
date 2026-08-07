# Ticket price and number of tickets
ticket_price = 250
tickets = 4

# Calculate total bill
total = ticket_price * tickets

# Apply discount if total bill is above 500
if total > 500:
    total -= 100

# Display the final amount payable
print("Final Amount Payable =", total)