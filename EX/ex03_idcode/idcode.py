"""
EX03 ID code.

1. ID code
This program checks whether the ID code given as a string has a right amount of
numbers and if so, whether the control number provided by the ID code
itself is correct.
The program uses "Module 11" method to calculate the control number.
Available functions:
find_id_code(text: str) -> str
the_first_control_number_algorithm(text: str) -> str
is_valid_gender_number(year_number: int) -> bool
get_gender(year_number: int) -> str
is_valid_year_number(year_number: int) -> bool
is_valid_month_number(month_number: int) -> bool
is_valid_birth_number(birth_number: int) -> bool
is_leap_year(year_number: int) -> bool
get_full_year(gender_number: int, year_number: int) -> int
get_birth_place(birth_number: int) -> str
is_valid_control_number(id_code: str) -> bool
is_valid_day_number(gender_number: int, year_number: int, month_number: int, day_number: int) -> bool
is_id_valid(id_code: str) -> bool
get_data_from_id(id_code: str) -> str

"""


def find_id_code(text: str) -> str:
    """
    Find ID-code from given text.

    Given string may include any number of numbers, characters and other symbols mixed together.
    The numbers of ID-code may be between other symbols - they must be found and concatenated.
    ID-code contains of exactly 11 numbers. If there are not enough numbers, return 'Not enough numbers!',
    if there are too many numbers, return 'Too many numbers!' If ID-code can be found, return that code.
    You don't have to validate the ID-code here. If it has 11 numbers, then it is enough for now.

    :param text: string
    :return: string
    """
    # Remove redundant spaces from both ends of the string.
    text = text.strip()
    # Initiate variable for id code.
    id_code = ""
    # Loop through letters in text which was given as an argument
    # in order to extract only numbers.
    for letter in text:
        if letter.isdigit():
            id_code += letter

    # Validate the length of the id code
    if len(id_code) > 11:
        return "Too many numbers!"
    elif len(id_code) < 11:
        return "Not enough numbers!"
    else:
        return id_code


def the_first_control_number_algorithm(text: str) -> str:
    """
    Check if given value is correct for control number in ID code only with the first algorithm.

    The first algorithm can be calculated with ID code's first 10 numbers.
    Each number must be multiplied with its corresponding digit
    (in this task, corresponding digits are: 1 2 3 4 5 6 7 8 9 1), after which all the values are summarized
    and divided by 11. The remainder of calculation should be the control number.

    If the remainder is less than 10 and equal to the last number of ID code,
    then that's the correct control number and the function should return the ID code.
    Otherwise, the control number is either incorrect or the second algorithm should be used.
    In this case, return "Needs the second algorithm!".

    If the string contains more or less than 11 numbers, return "Incorrect ID code!".
    In other case use the previous algorithm to get the code number out of the string
    and find out, whether its control number is correct.

    :param text: string
    :return: string
    """
    # Call the find_id_code function with the argument provided and save the result
    # into a variable.
    id_code = find_id_code(text)
    # Actually the length check was conducted in previous function too.
    if len(id_code) < 11 or len(id_code) > 11:
        return "Incorrect ID code!"
    else:
        # Initiate the control number.
        control_number = 0
        # Loop through all numbers from 0 to 9.
        for element in range(10):
            # If the number is 9, then add to the control number
            # the number which index in id code is 9.
            if element == 9:
                control_number += int(id_code[element])
            # If the number i.e. element is other than 9
            # take the number with index equal to the element
            # and multiply it through with the number which is
            # greater than the element by 1
            # (because indexes start at 0).
            else:
                control_number += int(id_code[element]) * (element + 1)

        # After all the numbers are multiplied with the weight and
        # summarised, find the modulo by dividing the sum with 11
        # and reassign the modulo to the control number.
        control_number = control_number % 11

        # If the control number doesn't match the control
        # number provided by id code (at index 10)
        # consider the id code incorrect.
        if control_number < 10 and control_number != int(id_code[10]):
            return "Incorrect ID code!"
        elif control_number >= 10:
            return "Needs the second algorithm!"
        else:
            return id_code


def is_valid_gender_number(gender_number: int) -> bool:
    """
    Check if given value is correct for gender number in ID code.

    Check whether the gender number is in range 1-6.

    :param gender_number: integer
    :return: boolean
    """
    valid_gender_numbers = [1, 2, 3, 4, 5, 6]
    # If the year number is in valid_year_numbers array, it's valid.
    return gender_number in valid_gender_numbers


def get_gender(gender_number: int) -> str:
    """Define persons gender by ID's gender number."""
    # Define valid gender numbers for males and females.
    gender_numbers = {"male": [1, 3, 5], "female": [2, 4, 6]}
    if gender_number in gender_numbers["male"]:
        return "male"
    elif gender_number in gender_numbers["female"]:
        return "female"


def is_valid_year_number(year_number: int) -> bool:
    """Check if given value is correct for year number in ID code."""
    # If the year number is between 0 and 99, it's valid.
    return year_number in range(0, 100)


def is_valid_month_number(month_number: int) -> bool:
    """Check if given value is correct for month number in ID code."""
    # Month number is considered valid if it's between 1 and 12 (included).
    return month_number in range(1, 13)


def is_valid_birth_number(birth_number: int) -> bool:
    """Check if given value is correct for birth number in ID code."""
    # Birth number is valid if it's between 1 and 999 (included).
    return birth_number in range(1, 1000)


def is_leap_year(year_number: int) -> bool:
    """Check whether the given year is a leap year."""
    # Leap year divides by 400 or by 4 and at the same time
    # not by 100.
    return year_number % 400 == 0 or (year_number % 4 == 0 and (True if year_number < 100 else year_number % 100 != 0))


def get_full_year(gender_number: int, year_number: int) -> int:
    """Define the 4-digit year when given person was born."""
    # Define gender number and year prefix relationship.
    year_number_prefix = {"18": [1, 2], "19": [3, 4], "20": [5, 6]}
    # Convert year number into string.
    year_number = str(year_number)
    # Add leading zero if year number has one digit
    if len(year_number) == 1:
        year_number = "0" + year_number

    for key, value in year_number_prefix.items():
        if gender_number in value:
            return int(str(key) + year_number)


def get_birth_place(birth_number: int) -> str:
    """Find the place where the person was born."""
    # Define birthplaces
    valid_birth_places = {
        "Kuressaare": list(range(1, 11)),
        "Tartu": list(range(11, 21)) + list(range(271, 371)),
        "Tallinn": list(range(21, 221)) + list(range(471, 711)),
        "Kohtla-Järve": list(range(221, 271)),
        "Narva": list(range(371, 421)),
        "Pärnu": list(range(421, 471)),
        "undefined": list(range(711, 1000))
    }

    # Check whether the input is valid.
    if is_valid_birth_number(birth_number):
        # Loop through key-value pairs of valid_birth_places.
        for key, value in valid_birth_places.items():
            # If the birth number is present, return birthplace.
            if birth_number in value:
                return key
    else:
        return "Wrong input!"


def is_valid_control_number(id_code: str) -> bool:
    """Check if given value is correct for control number in ID code."""
    # Clean the possibly dirty argument.
    # Although the_first_control_number_algorithm already does it, the cleaned
    # ID code is needed later in the code.
    id_code = find_id_code(id_code)
    # Define the pre-check result.
    first_control_result = the_first_control_number_algorithm(id_code)
    # Decide by the outcome of the_first_control_number_algorithm
    # whether the control number is valid.
    match first_control_result:
        case "Incorrect ID code!":
            return False
        case "Needs the second algorithm!":
            # Initiate the control number for the second check.
            control_number = 0
            index = 0
            # Conduct the second check.
            # Loop through all weight numbers for the second check.
            for element in [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]:
                control_number += int(id_code[index]) * element
                index += 1

            # After all the numbers are multiplied with the weight and
            # summarised, find the modulo by dividing the sum with 11
            # and reassign the modulo to the control number.
            control_number = control_number % 11

            # If the control number doesn't match the control
            # number provided by id code (at index 10)
            # consider the id code incorrect.
            return control_number == int(id_code[10]) or (control_number == 10 and int(id_code[10]) == 0)
        # Return default True when the first algorithm returned something
        # else than "Incorrect..." or "Needs the second algorithm"
        # because then it returned the ID code.
        case _:
            return True


def is_valid_day_number(gender_number: int, year_number: int, month_number: int, day_number: int) -> bool:
    """Check if given value is correct for day number in ID code."""
    # Comment out following code since the tester doesn't count invalid gender numbers.
    # Do not proceed if the gender number is wrong.
    # if not is_valid_gender_number(gender_number):
    #    return False

    # If the year number is valid, get full year, else do not proceed.
    if is_valid_year_number(year_number) and is_valid_gender_number(gender_number):
        full_year = get_full_year(gender_number, year_number)
    else:
        return False

    # Define how many days there can be in a month.
    valid_days_in_months = {"30": [4, 6, 9, 11], "31": [1, 3, 5, 7, 8, 10, 12]}
    # If the month number is valid, start checking days.
    if is_valid_month_number(month_number):
        # In case February and leap year, consider the day to be correct when in range 1-29.
        if month_number == 2 and is_leap_year(full_year) and day_number in range(1, 30):
            return True
        # In case February and not a leap year, consider the day to be correct when in range 1-28.
        elif month_number == 2 and not is_leap_year(full_year) and day_number in range(1, 29):
            return True
        # In case other months validate against predefined valid_days_in_months.
        elif month_number in valid_days_in_months["30"] and day_number in range(1, 31):
            return True
        elif month_number in valid_days_in_months["31"] and day_number in range(1, 32):
            return True
        else:
            return False
    else:
        return False


def is_id_valid(id_code: str) -> bool:
    """Check if given ID code is valid and return the result (True or False)."""
    # Clean the input string.
    id_code = find_id_code(id_code)
    # Check whether the control number and birthday is valid.
    # is_valid_control_number function also runs the_first_control_number_algorithm check on ID code and
    # is_valid_day_number runs is_valid_gender_number, is_valid_year_number,
    # is_valid_month number checks behind the scenes.
    # Define variables for readability.
    is_control_number_check_passed = is_valid_control_number(id_code)
    if is_control_number_check_passed:
        is_valid_day = is_valid_day_number(int(id_code[0]), int(id_code[1:3]), int(id_code[3:5]), int(id_code[5:7]))
    else:
        return False
    return is_control_number_check_passed and is_valid_day and is_valid_birth_number(int(id_code[7:10]))


def get_data_from_id(id_code: str) -> str:
    """Get possible information about the person."""
    # Clean the input string.
    id_code = find_id_code(id_code)

    if is_id_valid(id_code):
        gender = get_gender(int(id_code[0]))
        birthday = id_code[5:7]
        birth_month = id_code[3:5]
        year_number = int(id_code[1:3])

        birth_year = get_full_year(int(id_code[0]), year_number)
        birth_location = get_birth_place(int(id_code[7:10]))
        if birth_location == "Wrong input!":
            return "Given invalid ID code!"
        else:
            return f"This is a {gender} born on {birthday}.{birth_month}.{birth_year} in {birth_location}."
    else:
        return "Given invalid ID code!"


if __name__ == '__main__':
    print("\nFind ID code:")
    print(find_id_code(""))  # -> "Not enough numbers!"
    print(find_id_code("123456789123456789"))  # -> "Too many numbers!"
    print(find_id_code("ID code is: 49403136526"))  # -> "49403136526"
    print(find_id_code(
        "efs4  9   #4aw0h 3r 1a36g5j2!!6-"
    ))  # -> "49403136526"

    print(the_first_control_number_algorithm(""))  # -> "Incorrect ID code!"
    print(the_first_control_number_algorithm(
        "123456789123456789"
    ))  # -> "Incorrect ID code!"
    print(the_first_control_number_algorithm(
        "ID code is: 49403136526"
    ))  # -> "49403136526"
    print(the_first_control_number_algorithm(
        "efs4  9   #4aw0h 3r 1a36g5j2!!6-"
    ))  # -> "49403136526"
    print(the_first_control_number_algorithm(
        "50412057633"
    ))  # -> "50412057633"
    print(the_first_control_number_algorithm(
        "Peeter's ID is euf50weird2fs0fsk51ef6t0s2yr7fyf4"
    ))  # -> "Needs the second algorithm!"
    print(the_first_control_number_algorithm(
        "50207094560"
    ))  # -> Incorrect ID code!

    print("\nGender number:")
    for i in range(9):
        print(f"{i} {is_valid_gender_number(i)}")
        # 0 -> False
        # 1...6 -> True
        # 7...8 -> False

    print("\nGet gender:")
    print(get_gender(2))  # -> "female"
    print(get_gender(5))  # -> "male"

    print("\nYear number:")
    print(is_valid_year_number(100))  # -> False
    print(is_valid_year_number(50))  # -> True
    print(is_valid_year_number(0))  # -> False

    print("\nMonth number:")
    print(is_valid_month_number(0))  # -> False
    print(is_valid_month_number(2))  # -> True
    print(is_valid_month_number(13))  # -> False
    print(is_valid_month_number(15))  # -> False
    print(is_valid_month_number(99))  # -> False
    print(is_valid_month_number(100))  # -> False

    print("\nBorn order number:")
    print(is_valid_birth_number(0))  # -> False
    print(is_valid_birth_number(1))  # -> True
    print(is_valid_birth_number(850))  # -> True

    print("\nLeap year:")
    print(is_leap_year(4))  # -> True
    print(is_leap_year(1804))  # -> True
    print(is_leap_year(1800))  # -> False

    print("\nGet full year:")
    print(get_full_year(1, 28))  # -> 1828
    print(get_full_year(4, 85))  # -> 1985
    print(get_full_year(5, 1))  # -> 2001

    print("\nChecking where the person was born")
    print(get_birth_place(0))  # -> "Wrong input!"
    print(get_birth_place(1))  # -> "Kuressaare"
    print(get_birth_place(273))  # -> "Tartu"
    print(get_birth_place(220))  # -> "Tallinn"

    print("\nControl number:")
    print(is_valid_control_number("49808270244"))  # -> True
    print(is_valid_control_number("60109200187"))  # -> False, it must be 6
    print(is_valid_control_number("euf50weird2fs0fsk51ef6t0s2yr7fyf4"))  # -> True

    print("\nDay number:")
    print(is_valid_day_number(4, 5, 12, 25))  # -> True
    print(is_valid_day_number(3, 10, 8, 32))  # -> False
    print("\nFebruary check:")
    print(
        is_valid_day_number(4, 96, 2, 30))  # -> False (February cannot contain more than 29 days in any circumstances)
    print(is_valid_day_number(4, 99, 2, 29))  # -> False (February contains 29 days only during leap year)
    print(is_valid_day_number(4, 8, 2, 29))  # -> True
    print("\nMonth contains 30 or 31 days check:")
    print(is_valid_day_number(4, 22, 4, 31))  # -> False (April contains max 30 days)
    print(is_valid_day_number(4, 18, 10, 31))  # -> True
    print(is_valid_day_number(4, 15, 9, 31))  # -> False (September contains max 30 days)
    print(is_valid_day_number(6, 1, 9, 20))  # -> True

    print("\nOverall ID check::")
    print(is_id_valid("49808270244"))  # -> True
    print(is_id_valid("12345678901"))  # -> False
    print(is_id_valid("60109200187"))  # -> False
    print(is_id_valid("60114200187"))  # -> False
    print(is_id_valid("49804310244"))  # -> False
    print(is_id_valid("49804370244"))  # -> False
    print(is_id_valid("09804370244"))  # -> False
    print(is_id_valid("49808270244"))  # -> True
    print(is_id_valid("0980437244"))  # -> False
    print(is_id_valid("49808270244"))  # -> True
    print(is_id_valid("49l08270244"))  # -> False

    print("\nFull message:")
    print(get_data_from_id("49808270244"))  # -> "This is a female born on 27.08.1998 in Tallinn."
    print(get_data_from_id("50308226018"))  # -> "This is a male born on 22.08.2003 in Tallinn."
    print(get_data_from_id("60109200187"))  # -> "Given invalid ID code!"
    print(get_data_from_id("09804370244"))  # -> "Given invalid ID code!"

    # print("\nTest now your own ID code:")
    # personal_id = input()  # type your own id in command prompt
    # print(is_id_valid(personal_id))  # -> True
