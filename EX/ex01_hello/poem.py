"""EX01 Poem.

2. Poem
Example output:

Roses are red,
violets are blue,
I love to code
And so will you!

"""


rose_color = "red"
flowers_name = "violets"
favourite_activity = "code"

# Ask for a rose color.
rose_color = input(f"Roses are {rose_color}. What color suits instead of '{rose_color}'? ")
# Ask for flowers name in plural.
flowers_name = input(f"{flowers_name} are blue. What flowers suit instead of '{flowers_name}'? ")
# Ask for an activity.
favourite_activity = input(f"I love to {favourite_activity}. What activity suits instead of '{favourite_activity}'? ")

# Print the poem with user-entered values.
print(f"Roses are {rose_color},\n{flowers_name} are blue,\nI love to {favourite_activity}\nAnd so will you!")
