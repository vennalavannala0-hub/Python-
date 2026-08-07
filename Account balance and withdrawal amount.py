# Account balance and withdrawal amount
balance = 10000
withdraw_amount = 4500

# Check if withdrawal is valid
if withdraw_amount <= balance and withdraw_amount % 100 == 0:
    print("Withdrawal is valid.")
else:
    print("Withdrawal is not valid.")