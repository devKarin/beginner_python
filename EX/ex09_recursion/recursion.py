"""
EX09 - Recursion.

This program makes different operations using loop-based functions and offering recursion-based alternatives to them.

Available functions:
loop_reverse(s: str) -> str; Reverse a string using a loop.
recursive_reverse(s: str) -> str; Reverse a string using recursion.
loop_sum(n: int) -> int; Calculate the sum of all numbers from 0 up to n (including n) using a loop.
recursive_sum(n: int) -> int; Calculate the sum of all numbers from 0 up to n (including n) using recursion.
countdown(n: int) -> list; Recursive function that returns a list of numbers that count down from n.
add_commas(n: int) -> str; Recursive function which adds commas into a number to separate three digit groups of it.
sum_digits_recursive(number: int) -> int; Returns the sum of the digits in number.
pair_star_recursive(s: str) -> str; Adds star between identical adjacent characters.
stonks(coins: float, rate: float, years: int) -> int; A recursive function that calculates the net worth
of coins for an investment after some years, rounded down to the nearest integer.

quic_mafs(a: int, b: int) -> list; Recursive function that changes its arguments depending on conditions.

"""

import math


def loop_reverse(s: str) -> str:
    """
    Reverse a string using a loop.

    loop_reverse("hey") => "yeh"
    loop_reverse("aaa") => "aaa"
    loop_reverse("") => ""
    loop_reverse("1") => "1"

    :param s: input string
    :return: reversed input string
    """
    p = ""
    for iterator in range(len(s)):
        p += s[-(iterator + 1)]
    return p


def recursive_reverse(s: str) -> str:
    """
    Reverse a string using recursion.

    recursive_reverse("hey") => "yeh"
    recursive_reverse("aaa") => "aaa"
    recursive_reverse("") => ""
    recursive_reverse("1") => "1"

    :param s: input string
    :return: reversed input string
    """
    p = ""
    # If the input string exists, add its last letter to the final string and
    # call the function again recursively without the last letter.
    if len(s) > 0:
        p = s[-1] + recursive_reverse(s[:-1])
    return p


def loop_sum(n: int) -> int:
    """
    Calculate the sum of all numbers up to n (including n) using a loop.

    loop_sum(0) => 0
    loop_sum(3) => 6
    loop_sum(5) => 15

    :param n: the last number to add to the sum
    :return: sum
    """
    summary = 0
    for iterator in range(n + 1):
        summary += iterator
    return summary


def recursive_sum(n: int) -> int:
    """
    Calculate the sum of all numbers up to n (including n) using recursion.

    recursive_sum(0) => 0
    recursive_sum(3) => 6
    recursive_sum(5) => 15

    :param n: the last number to add to the sum
    :return: sum
    """
    summary = 0
    if n >= 0:
        summary = n + recursive_sum(n-1)
    return summary


def countdown(n: int) -> list:
    """
    Recursive function that returns a list of numbers that count down from n.

    countdown(5) -> [5, 4, 3, 2, 1, 0]
    countdown(8) -> [8, 7, 6, 5, 4, 3, 2, 1, 0]
    countdown(-1) -> []

    :param n: start
    :return: countdown sequence
    """
    start_list = []
    if n >= 0:
        start_list.append(n)
        start_list.extend(countdown(n - 1))
    return start_list


def add_commas(n: int) -> str:
    """
    Recursive function which adds commas into a number to separate three digit groups of it.

    In representing large numbers, from the right side to the left,
    English texts usually use commas to separate each group of three digits in front of the decimal.

    add_commas(1245) -> '1,245'
    add_commas(123456789) -> '123,456,789'
    add_commas(1011) -> '1,011'

    :param n: int
    :return: string of the formatted int
    """
    formatted_int = ""
    # If the input is greater than 3, a comma needs to be added before the 3 last numbers.
    # For the rest of the numbers, call the function again and add previous slices to the result string.
    if len(str(n)) > 3:
        formatted_int = add_commas(int(str(n)[:-3])) + "," + str(n)[-3:]
    # If the input has less or equal to 3, but still more numbers than 0,
    # add it before the last previous result without adding a comma.
    elif len(str(n)) > 0:
        return str(n) + formatted_int
    return formatted_int


def sum_digits_recursive(number: int) -> int:
    """
    Return the sum of the digits in number.

    Given a non-negative int n, return the sum of its digits recursively.

    sum_digits_recursive(123) => 6
    sum_digits_recursive(1) => 1
    sum_digits_recursive(0) => 0
    sum_digits_recursive(999) => 27

    Hint: turn the number into string and take one digit at a time.

    :param number: non-negative number
    :return: sum of digits in the number
    """
    sum_of_digits = 0
    # If there are more than 1 digits in input number, take the last one and
    # add the recursive call for the rest of the slice to it.
    if len(str(number)) > 1:
        sum_of_digits = int(str(number)[-1]) + sum_digits_recursive(int(str(number)[:-1]))
    # If there is only one number left, add it to the sum.
    elif len(str(number)) == 1:
        sum_of_digits += int(str(number)[-1])
    return sum_of_digits


def pair_star_recursive(s: str) -> str:
    """
    Add star between identical adjacent characters.

    Given a string, compute recursively a new string
    where identical characters that are adjacent in the original string
    are separated from each other by a "*".

    pair_star_recursive("abc") => "abc"
    pair_star_recursive("aa") => "a*a"
    pair_star_recursive("aaa") => "a*a*a"
    pair_star_recursive("") => ""

    :param s: input string
    :return: string with stars between identical chars.
    """
    new_string = ""
    # If there are more than one character in input string,
    # compare the last and the second from the last characters and
    # if they are equal, add the last character and a star before recursively calling the function
    # to the rest of the slice of the word.
    if len(s) > 1 and s[-1] == s[-2]:
        new_string = pair_star_recursive(s[:-1]) + "*" + s[-1]
    # Otherwise, if the characters are not equal, but the rest of the word still has
    # more than 0 characters, add the last of them to the result and call the function
    # recursively to the last of the slice.
    elif len(s) > 0:
        new_string = pair_star_recursive(s[:-1]) + s[-1]
    return new_string


def stonks(coins: float, rate: float, years: int) -> int:
    """
    Write a recursive function that calculates the net worth of coins for a crypto-investment after some years.

    The result is rounded down to the nearest integer.

    stonks(1000, 10, 10) -> 2593
    stonks(100000, 12, 3) -> 140492

    :param coins: starting amount (0-10000)
    :param rate: rate percentage (0-100)
    :param years: number of years (0-50)
    :return: coins after years
    """
    # Initially netto worth is the amount of coins.
    net_worth = coins
    # With every cycle, years number decreases by one.
    if years - 1 >= 0:
        # Netto worth for a year is initial amount of coins plus the increase
        # which is coins multiplied with the rate.
        # For each following year the amount of coins equals the result of the last year.
        net_worth = stonks(coins + coins * rate / 100, rate, years - 1)
    return math.floor(net_worth)


def quic_mafs(a: int, b: int) -> list:
    """
    Recursive function that applies the following operations.

    i) If a = 0 or b = 0, return [a,b]. Otherwise, go to step (ii);
    ii) If a >= 2*b, set a = a - 2*b, and repeat step (i). Otherwise, go to step (iii);
    iii) If b >= 2*a, set b = b - 2*a, and repeat step (i). Otherwise, return [a,b].

    quic_mafs(6, 19) -> [6, 7]
    quic_mafs(2, 1) -> [0, 1]
    quic_mafs(22, 5) -> [0, 1]
    quic_mafs(8796203,7556) -> [1019,1442]

    :param a: int
    :param b: int
    :return: result
    """
    if a != 0 and b != 0:
        if a >= 2 * b:
            return quic_mafs(a - 2 * b, b)
        elif b >= 2 * a:
            return quic_mafs(a, b - 2 * a)
    return [a, b]


if __name__ == "__main__":
    print(loop_reverse("hello"))  # -> "olleh"
    print(loop_reverse(""))  # -> ""
    print(loop_reverse("123"))  # -> "321"
    print(loop_reverse("hey"))  # - > "yeh"
    print(loop_reverse("aaa"))  # - > "aaa"
    print(loop_reverse("1"))  # - > "1"

    print(recursive_reverse("hello"))  # -> "olleh"
    print(recursive_reverse(""))  # -> ""
    print(recursive_reverse("123"))  # -> "321"
    print(recursive_reverse("hey"))  # - > "yeh"
    print(recursive_reverse("aaa"))  # - > "aaa"
    print(recursive_reverse("1"))  # - > "1"

    print(loop_sum(0))  # -> 0
    print(loop_sum(3))  # -> 6
    print(loop_sum(5))  # -> 15
    print(loop_sum(10))  # -> 55

    print(recursive_sum(0))  # -> 0
    print(recursive_sum(3))  # -> 6
    print(recursive_sum(5))  # -> 15
    print(recursive_sum(10))  # -> 55

    print(countdown(5))  # -> [5, 4, 3, 2, 1, 0]
    print(countdown(8))  # -> [8, 7, 6, 5, 4, 3, 2, 1, 0]
    print(countdown(-1))  # -> []

    print(add_commas(1245))  # -> '1,245'
    print(add_commas(123456789))  # -> '123,456,789'
    print(add_commas(1011))  # -> '1,011'

    print(sum_digits_recursive(123))  # -> 6
    print(sum_digits_recursive(0))  # -> 0
    print(sum_digits_recursive(1000000000000000))  # -> 1
    print(sum_digits_recursive(1))  # -> 1
    print(sum_digits_recursive(999))  # -> 27

    print(pair_star_recursive("abc"))  # -> "abc"
    print(pair_star_recursive("aaa"))  # -> a*a*a
    print(pair_star_recursive(""))  # -> ""
    print(pair_star_recursive("aa"))  # -> "a*a"

    print(stonks(1000, 10, 10))  # -> 2593
    print(stonks(100000, 12, 3))  # -> 140492

    print(quic_mafs(6, 19))  # -> [6, 7]
    print(quic_mafs(2, 1))  # -> [0, 1]
    print(quic_mafs(22, 5))  # -> [0, 1]
    print(quic_mafs(8796203, 7556))  # -> [1019,1442]
