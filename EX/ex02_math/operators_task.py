"""EX02 Math operators."""

"""
1. Operators task.
This program defines following functions:
add(x: int, y: int)
sub(x: int, y: int)
multiply(x: int, y: int)
div(x: int, y: int)
modulus(x: int, y: int)
floor_div(x: int, y: int)
exponent(x: int, y: int)
first_greater_or_equal(x: int, y: int)
second_less_or_equal(x: int, y: int)
x_is_y(x: int, y: int)
x_is_not_y(x: int, y: int)
if_else(a: int, b: int, c: int, d: int)
surface()
volume()

Example output:

Enter a sum: 63
Amount of coins needed: 5

"""


import math


def add(x: int, y: int) -> int:
    """Add x to y."""
    return x + y


def sub(x: int, y: int) -> int:
    """Subtract y from x."""
    return x - y


def multiply(x: int, y: int) -> int:
    """Multiply x by y."""
    return x * y


def div(x: int, y: int) -> float:
    """Divide x by y."""
    return round(x / y)


def modulus(x: int, y: int) -> int:
    """Divide x by y and return remainder. Use an arithmetic operator."""
    return x % y


def floor_div(x: int, y: int) -> int:
    """Divide x by y and floor the value. Use an arithmetic operator."""
    return math.floor(x / y)


def exponent(x: int, y: int) -> int:
    """Calculate x raised to the power of y."""
    return round(math.pow(x, y))


def first_greater_or_equal(x: int, y: int) -> bool:
    """If x is greater or equal than y then return True. Else return False."""
    if x >= y:
        return True
    else:
        return False


def second_less_or_equal(x: int, y: int) -> bool:
    """If y is less or equal than x then return True. Else return False."""
    if y <= x:
        return True
    else:
        return False


def x_is_y(x: int, y: int) -> bool:
    """If x value is the same as y value then return True. Else return False."""
    if x is y:
        return True
    else:
        return False


def x_is_not_y(x: int, y: int) -> bool:
    """If x value is not the same as y value then return True. Else return False."""
    if x != y:
        return True
    else:
        return False


def if_else(a: int, b: int, c: int, d: int) -> float:
    """
    Create a program that has 4 numeric parameters.

    Multiply parameters 1-2 (multiply a by b) by each other
    and divide parameters 3-4 (divide c by d) by each other.
    Next check and return the greater value.
    If both values are the same then return 0 (number zero).
    """
    if (a * b) > (c / d):
        return a * b
    elif (a * b) < (c / d):
        return c / d
    elif a * b == c / d:
        return 0
    else:
        return


def surface(rectangle_width: int, rectangle_height: int) -> int:
    """
    Calculate and return the value of the surface of a rectangle.

    Add the missing parameters to calculate the surface of a rectangle.
    Calculate and return the value of the surface.
    """
    return rectangle_width * rectangle_height


def volume(cuboid_width: int, cuboid_height: int, cuboid_depth: int) -> int:
    """
    Calculate and return the value of the volume of a cuboid.

    Add the missing parameters to calculate the volume of a cuboid.
    Calculate and return the value of the volume.
    """
    return cuboid_width * cuboid_height * cuboid_depth


def clock(days: int, hours: int, minutes: int, seconds: int) -> float:
    """
    Convert the time into minutes and return it.

    Convert the inserted days, hours, minutes and seconds into minutes,
    add them up, round the answer to the 0 decimal places and returns it.
    """
    minutes = minutes + 24 * 60 * days + 60 * hours + (1 / 60) * seconds
    return round(minutes, 2)

def calculate(operation: int, first_operand: int, second_operand: int) -> float:
    """
    Calculate the value of operations.

    Calculate the value of operations based on arguments given.
    Operation type is defined as follows:
    0 - add
    1 - subtract
    2 - multiply
    3 - divide

    Round the results to the 2 decimal places.
    """

    if operation == 0:
        return round((first_operand + second_operand), 2)
    elif operation == 1:
        return round((first_operand - second_operand), 2)
    elif operation == 2:
        return round((first_operand * second_operand), 2)
    elif operation == 3:
        if second_operand == 0:
            return
        return round((first_operand / second_operand), 2)
    else:
        return


if __name__ == '__main__':
    print(add(1, -2))  # -1
    print(sub(5, 5))  # 0
    print(multiply(5, 5))  # 25
    print(div(15, 5))  # 3
    print(modulus(9, 3))  # 0
    print(floor_div(3, 2))  # 1
    print(exponent(5, 5))  # 3125
    print(first_greater_or_equal(1, 2))  # False
    print(second_less_or_equal(5, 5))  # True
    print(x_is_y(1, 2))  # False
    print(x_is_not_y(1, 2))  # True
    print(if_else(1, 3, 5, 99))  # 3
    print(if_else(2, 1, 10, 5))  # 0
    print(surface(1, 2)) # 2
    print(volume(5, 5, 5)) # 125
    print(clock(0, 0, 1, 15))  # 1.25
    print(clock(0, 1, 5, 0))  # 65
    # Try "calculate" here
    print(calculate(1, 5, 2))  # 3
    print(calculate(0, 0, 5))  # 5
    print(calculate(1, 0, 5))  # -5
    print(calculate(2, 0, 5))  # 0
    print(calculate(3, 0, 5))  # 0
    print(calculate(3, 25, 5))  # 5
    print(calculate(3, 10, 3))  # 3.34

