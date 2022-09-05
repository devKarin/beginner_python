"""EX01 Cashier."""

"""
4. Cashier
This program gets a number (always 1-100) as input and prints to the console
the minimum amount of coins a cashier needs to return as an exchange to cover
the entered sum of cents with as few coins as possible.

Example output:

Enter a sum: 63
Amount of coins needed: 5

"""


amount = int(input("Enter a sum: "))
amount_of_coins_returned = 0
available_coins = [50, 20, 10, 5, 1]

# Loop over available coins array
for coin in available_coins:
    # Increase the number of coins to be returned by
    # truncated quotient of amount entered and the coin value.
    amount_of_coins_returned += int(amount / coin)
    # Reassign the modulo of amount and coin quotient to the amount
    # i.e. the amount left to return.
    amount = amount % coin

print(f"Amount of coins needed: {amount_of_coins_returned}")
