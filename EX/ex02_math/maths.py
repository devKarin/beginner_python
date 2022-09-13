"""
EX02 Math.

2. Maths.
This program defines following functions:
def average(a: int, b: int, c: int, d: int)
def school_pressure(ects: int, weeks: int)
def add_fractions(a: int, b: int, c: int, d: int)

"""


def average(a: int, b: int, c: int, d: int) -> float:
    """
    Implement a function that has 4 numeric parameters.

    Each parameter must be multiplied by number of its position in the function (x, y, z = 1, 2, 3).
    Calculate and return the average.

    Examples:
    average(0, 0, 0, 4) === 4
    average(1, 2, 3, 4) == 7.5
    average(5, 0, 5, 1) == 6
    """
    input_arguments = [a, b, c, d]
    # Convert all given arguments into integers just in case
    for input_argument in input_arguments:
        input_argument = int(input_argument)
    return (a * 1 + b * 2 + c * 3 + d * 4) / 4


def school_pressure(ects: int, weeks: int) -> float:
    """
    Implement a function to know how many hours are needed per week if each ECTS is 26 hours.

    If it's not possible in time then return -1.

    Examples:
    school_pressure(30, 12) == 65
    school_pressure(1, 1) == 26
    school_pressure(1, 0) == -1
    """
    # Hours of work required to earn entered ects
    total_hours_needed = ects * 26
    if weeks <= 0:
        return float(-1)
    else:
        # Weekly hours of work required to earn the ects within entered timeframe
        hours_in_week_needed = total_hours_needed / weeks
        if hours_in_week_needed > 168:
            return float(-1)
        else:
            return hours_in_week_needed


def add_fractions(a: int, b: int, c: int, d: int) -> str:
    """
    Implement a function that takes 4 parameters.

    Parameters a and b denote the first fraction like a/b.
    Parameters c and d denote the second fraction like c/d.

    Find and return a fraction in string format that is the sum of a/b and c/d.

    NB! the fraction does not have to be in the simplest form.
    NB! the answer should not contain any commas.

    Examples:
    add_fractions(1, 3, 1, 3) # 1/3 + 1/3 => there are many correct answers like "2/3" and "6/9"
    add_fractions(2, 5, 1, 5) # 2/5 + 1/5 => there are many correct answers like "3/5" and "15/25"
    """
    input_arguments = [a, b, c, d]
    # Convert all given arguments into integers just in case
    for input_argument in input_arguments:
        input_argument = int(input_argument)
        if input_argument == 0:
            return
    # Find common denominator
    common_denominator = b * d
    # Find the numerator
    numerator = a * d + b * c
    return f"{numerator}/{common_denominator}"


if __name__ == '__main__':
    print(average(0, 0, 0, 4))  # 4
    print(average(1, 2, 3, 4))  # 7.5
    print(average(5, 0, 5, 1))  # 6
    print(school_pressure(30, 12))  # 65.0
    print(school_pressure(1, 1))  # 26.0
    print(school_pressure(1, 0))  # -1.0
    print(school_pressure(0, 0))  # -1.0
    print(school_pressure(0, 2))  # 0.0
    print(school_pressure(1, 2))  # 13.0
    print(add_fractions(1, 3, 1, 3))  # 1/3 + 1/3 => "2/3", "6/9"
    print(add_fractions(2, 5, 1, 5))  # 2/5 + 1/5 => "3/5", "15/25"
    print(add_fractions(1, 2, 1, 2))  # 1/2 + 1/2 => "1/1", "4/4", "2/2"
    print(add_fractions(3, 1, 1, 1))  # 3/1 + 1/1 => "4/1", "16/4", "8/2"
    print(add_fractions(1, 6, 3, 5))  # 1/6 + 3/5 => "23/30", "46/60"
    print(add_fractions(0.5, 6, 3, 5))  # None
