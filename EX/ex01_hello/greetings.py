"""EX01 Greetings."""

"""
3. GreetingsGreetingsGreetings
Example output:

Enter a greeting: Hello
Enter a recipient: world
How many times to repeat: 3
Hello world! Hello world! Hello world!

"""


greeting = "Hello"
recipient = "world"
repetitions = 3

# Ask for a type of greeting.
greeting = input("Enter a greeting: ")
# Ask for a greeting recipient.
recipient = input("Enter a recipient: ")
# Ask for repetitions number.
repetitions = int(input("How many times to repeat: "))

# Capitalize greeting
greeting = greeting.capitalize()

# Print the greeting required amount of times.
print(f"{greeting} {recipient}! " * repetitions)
