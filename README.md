# iti0102-2022

## Description
This project contains solutions for exercises given in the course iti0102-2022 - Programming for beginners. <br>

Lecturer: Ago Luberg
This project is written in Python3.

## Sections
This project is divided into sections starting from basics to advanced.

### [ex00_intro](./EX/ex00_intro)
### [ex01_hello](./EX/ex01_hello)
### [ex02_math](./EX/ex02_math)
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
