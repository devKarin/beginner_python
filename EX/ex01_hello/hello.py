"""EX01 Hello."""

"""
1. Print Hello
Example output:

What is your name? Mari
Hello, Mari! Enter a random number: 5
Great! Now enter a second random number: 4
5 + 4 is 9

"""


# ask for a name
name = input("What is your name? ")
# Print the entered name and ask for first random number
number_1 = int(input(f"Hello, {name}! Enter a random number: "))
# ask for second random number
number_2 = int(input("Great! Now enter a second random number: "))
# calculate sum
sum_of_entered_numbers = number_1 + number_2
# print out sum
print(f"{number_1} + {number_2} is {sum_of_entered_numbers}")
