"""
EX02 Math.

3. Prime.
This program identifies whether the given argument is a prime number or not.

"""


def is_prime_number(number: int) -> bool:
    """
    Check if the number is a prime number.

    Prime number is a natural number which is only divisible by 1 and itself. 0 and 1 are not prime numbers.

    Conditions:
    1. If number is a prime number then return boolean True
    2. If number is not a prime number then return boolean False

    :param number: integer, The number to check.
    :return: boolean, True if number is a prime number or False if number is not a prime number.
    """
    # Numbers equal to or smaller than 1 are not prime numbers.
    # In order to avoid ZeroDivision error, this is handled before the loop.
    if number <= 1:
        return False
    # Loop through all integers smaller than the argument
    # Check for the prime number conditions.
    # Check whether the argument (possible prime number) divides by some number
    # smaller than itself. If so, the number can't be a prime number.
    for integer in range(2, number):
        if number % integer == 0:
            return False
    else:
        return True


if __name__ == '__main__':
    print(is_prime_number(2))  # -> True
    print(is_prime_number(89))  # -> True
    print(is_prime_number(23))  # -> True
    print(is_prime_number(4))  # -> False
    print(is_prime_number(7))  # -> True
    print(is_prime_number(88))  # -> False
    print(is_prime_number(47))  # -> True
    print(is_prime_number(0))  # -> False
    print(is_prime_number(1))  # -> False
