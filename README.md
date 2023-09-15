# iti0102-2022

## Description
This project contains solutions for exercises given in the course [iti0102-2022 - Programming for beginners](https://moodle.taltech.ee/enrol/index.php?id=32301). <br>

Lecturer: Ago Luberg<br />
This project is written in Python3 and is for my personal use but you are welcome to browse it as well.<br />


## Sections
This project is divided into sections starting from basics to advanced.

### [ex00_intro](./EX/ex00_intro)

#### [Exercise](./EX/ex00_intro/hello.py)

Write a program which prints out `Hello world!`.

### [ex01_hello](./EX/ex01_hello)

#### Exercise 1: [Print Hello](./EX/ex01_hello/hello.py)

Write a program, which:

- asks the user for a name: `"What is your name? "`
- prints out the entered name and asks for two numbers  <br />
`"Hello, [name]! Enter a random number: "` <br />
`"Great! Now enter a second random number: "` <br />
- prints out the sum of the two numbers: `[num1] + [num2] is [sum]`. <br />

***Example output:***<br />

**What is your name?** *John* <br />
**Hello, John! Enter a random number:** *7* <br />
**Great! Now enter a second random number:** *8* <br />
**7 + 8 is 15**<br /><br />

#### Exercise 2: [Poem](./EX/ex01_hello/poem.py)

Create a program, which helps you to write a poem.<br />
The structure of the poem looks like this:<br />

**Roses are [*some color*],**<br />  
**[*some plural noun*] are blue,**<br />    
**I love to [*some verb*]**<br />    
**And so will you!**<br /><br />

- Ask the user what would suit instead of [..] and print out the result.
- You will need to use `input()` and many different variables.
- The names of the variables should be short, simple, easily distinguishable and understandable.

#### Exercise 3: [Greetings](./EX/ex01_hello/greetings.py)

Create a program, which asks the user for a type of greeting, the recipient and how many times to repeat the entered greeting. Then the program prints out the greeting required number of times.<br />

***Example output:***<br />

**Enter a greeting:** *Hello*<br />
**Enter a recipient:** *world*<br />
**How many times to repeat:** *3*<br />
**Hello world! Hello world! Hello world!**<br />

#### Exercise 4: [Cashier](./EX/ex01_hello/cashier.py)

You are a cashier.<br />
You have to give back an x sum of cents to a client and you would like to know what is the minimum amount of coins you have to give back.<br />

Create a program, <br />
- which gets a number (always 1-100) as input,
- prints to the console the minimum amount of coins you need to give back to cover the entered sum of cents.
- The goal is to cover the sum with as few coins as possible.
- The cash register has cents with the following values: (1, 5, 10, 20, 50).

***Example with the input as 63:***<br />

**Enter a sum:** *63*<br />
**Amount of coins needed:** *5*<br /><br />

*The returned coins would be: 50, 10, 1, 1, 1*

### [ex02_math](./EX/ex02_math)

#### Exercise 1: [Operators](./EX/ex02_math/operators_task.py)

Complete the following functions:<br />

- **add(x: int, y: int):**<br />
Define a function, the parameters of which are whole numbers x and y.<br />
The function gets two whole numbers as arguments.<br />
The function returns the result of adding the arguments together.<br />

- **sub(x: int, y: int):**<br />
Define a function, the parameters of which are whole numbers x and y.<br />
The function gets two whole numbers as arguments.<br />
The function returns the result of subtracting the arguments.<br />

- **multiply(x: int, y: int):**<br />
Define a function, the parameters of which are whole numbers x and y.<br />
The function gets two whole numbers as arguments.<br />
The function returns the result of multiplying the arguments.<br />

- **div(x: int, y: int):**<br />
Define a function, the parameters of which are whole numbers x and y.<br />
The function gets two whole numbers as arguments.<br />
The function returns the result of dividing the arguments.<br />

- **modulus(x: int, y: int):**<br />
Define a function, the parameters of which are whole numbers x and y.<br />
The function gets two whole numbers as arguments.<br />
The function returns the remainder of x from y.<br />

- **floor_div(x: int, y: int):**<br />
Define a function, the parameters of which are whole numbers x and y.<br />
The function gets two whole numbers as arguments.<br />
The function returns the result of dividing the arguments using integer division.<br />

- **exponent(x: int, y: int):**<br />
Define a function, the parameters of which are whole numbers x and y.<br />
The function gets two whole numbers as arguments.<br />
The function returns the result of x to the power of y.<br />

- **first_greater_or_equal(x: int, y: int):**<br />
Define a function, the parameters of which are whole numbers x and y.<br />
The function gets two whole numbers as arguments.<br />
The function returns `True` if x is greater than or equal to y.<br />

- **second_less_or_equal(x: int, y: int):**<br />
Define a function, the parameters of which are whole numbers x and y.<br />
The function gets two whole numbers as arguments.<br />
The function returns `True` if y is less than or equal to x.<br />

- **x_is_y(x: int, y: int):**<br />
Define a function, the parameters of which are whole numbers x and y.<br />
The function gets two whole numbers as arguments.<br />
The function returns `True` if x is equal to y.<br />
There are multiple ways to achieve this: both using `is` and `==` are considered to be correct.

- **x_is_not_y(x: int, y: int):**<br />
Define a function, the parameters of which are whole numbers x and y.<br />
The function gets two whole numbers as arguments.<br />
The function returns `True` if x is not equal to y.<br />
There are multiple ways to achieve this: both using `is not` and `!=` are considered to be correct.<br />

- **if_else(a: int, b: int, c: int, d: int):**<br />
Define a function, the parameters of which are whole numbers a, b, c and d.<br />
The function gets four whole numbers as arguments.<br />
The first and the second argument need to be multiplied.<br />
The third argument needs to be divided by the fourth one.<br />
Compare which of the results is bigger - the multiplication result or the division result and return that result.<br />
If the results of both operations are exactly the same, return 0.<br />

- **surface():**<br />
Define a function, the parameters of which are two whole numbers.<br />
The function gets two whole numbers as arguments.<br />
Use the arguments to calculate the surface area of a rectangle and return it.<br />

- **volume():**<br />
Define a function, the parameters of which are three whole numbers.<br />
The function gets three whole numbers as arguments.<br />
Use the arguments to calculate the volume of a cuboid and return it.<br />

- **the function `clock`**<br />
Define a function, the parameters of which are 4 whole numbers: days, hours, minutes, seconds.<br />
The function converts all the times passed as arguments to minutes.<br />
The function returns the total amount of minutes.<br />

```Python3
print(clock(0, 0, 1, 15))  # 1.25
print(clock(0, 1, 5, 0))  # 65

```

- **the function `calculate`**<br />
Define a function similarly to the previous one.<br />
The function should be named `calculate`.<br />
Function's parameters are 3 whole numbers.<br /><br />

The first number indicates the operation:<br />
0 - addition<br />
1 - subtraction<br />
2 - multiplication<br />
3 - division<br /><br />

The second and third parameter are operands.<br />
The function chooses the correct operation based on the received .<br />
The function returns the result of the operation.<br /><br />

`calculate(1, 5, 2)` would return 3, because the chosen operation is subtraction, and 5 - 2 = 3.<br />

Test your solution by adding lines of code calling your calculate function with arguments corresponding to different operations to the if __name__ == '__main__': section at the bottom of the program.<br />

### [ex03_idcode](./EX/ex03_idcode)
### [ex04_lists](./EX/ex04_lists)
### [ex05_hobbies](./EX/ex05_hobbies)
### [ex06_regex](./EX/ex06_regex)
### [ex07_files](./EX/ex07_files)
Notes:
```Python3
# Opens file with the name "some_file.txt" in reading mode.
file = open("some_file.txt", "r")
# Reads n characters from file. If !n, reads the whole file.
# Attempt to read from closed file raises ValueError: I/O operation on closed file.
file.read(n)
# Reads a text row from file, but not more than n characters from it.
# Returns \n also.
file.readline(n)
# Reads n rows from file.
# Returns a list of lines.
# Returns \n at the end of the element.
file.readlines(n)
# Closes the file.
file.close()
# Opens file with name of "some_file.txt" and closes it afterwards automatically.
with open("some_file") as file:
    for line in file:  # Loops over the lines in file.
        # Do something
# For reading csv files, csv module needs to be imported.
import csv
# Opens the file for operation.
with open("some_file.csv") as csv_file:
    # Saves the file as a csv.reader object and separates the lines in file to list of strings
    # which were separated by the delimiter.
    csv_reader = csv.reader(csv_file, delimiter=",")
    # Loops over the lines in file.
    for row in csv_reader:
        # Do something

```

```Python3
# Opens file with the name "some_file.txt" in writing mode and creates it if it does not exist.
file = open("some_file.txt", "w")
# Writes text to the file. If there is some content already, overwrites it.
file.write("Some text to write.")
# Adds text right after the last text (no new line).
file.write("Write some more.")
# Closes file
file.close()
# Opens the file to add text to the end.
file = open("some_file.txt", "a")
# For writing into csv file, csv module needs to be imported.
import csv

data_to_write = [
    ['First', 'Second', 'Third'],
    [1, 2, 3]
]
# Newline needs to be "", because csv-writer adds \n by itself.
with open("some_file.csv"), "w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=";")
    # Write header.
    csv_writer.writerow(['First column', 'Second column', 'Third column'])
    for row in data:
        # Write list of values
        csv_writer.writerow(row)
```
### [ex08_ex05_hobbies](./EX/ex08_ex05_hobbies)
### [ex08_oop_tests](./EX/ex08_oop_tests)
### [ex08_solution_and_tests](./EX/ex08_solution_and_tests)
### [ex09_recursion](./EX/ex09_recursion)
### [ex10_oop](./EX/ex10_oop)
Notes:
```Python3


```
### [ex11_alchemy](./EX/ex11_alchemy)
### [ex12_adventure](./EX/ex12_adventure)
### [ex13_api](./EX/ex13_api)
### [ex14_robot](./EX/ex14_robot)
### [ex15_santas_workshop](./EX/ex15_santas_workshop)
