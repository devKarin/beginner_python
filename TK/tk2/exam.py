"""
TK2.

This is the first of two tests in this programming course.

Instructions:

Each exercise gives 1 point.
Total possible points: 5. The test is passed if you get at least 2.5 points.

You can commit-push as many times as you with.
The best result counts. Style points count, so make sure you have style fixed.

You can still solve the exercises after 90 minutes, you just get a bit less points.
The maximum time to solve the exercises is 2 hours.
If you have gathered some points and submit something after the deadline,
all the gathered points remain and penalty is applied only to that newly added part.

"""


def middle_value(a: int, b: int, c: int) -> int:
    """
    Return the middle value out of three values.

    The middle value is the one where there is other value which is smaller or equal
    and there is another value which is larger or equal.

    If the values are 6 2 4, then the middle value is 4.

    middle_value(6, 2, 4) => 4
    middle_value(2, 2, 4) => 2
    middle_value(2, 6, 2) => 2
    middle_value(88, 88, 88) => 88
    """
    # Create a list and sort it.
    middle_value = sorted([a, b, c])
    # Return the middle value from the sorted list.
    return middle_value[1]


def lucky_guess(n: int) -> bool:
    """
    Determine whether the given number gives you points for this task or not.

    The number gives you points if it is:
    * either 1, 3 or 7
    * greater or equal than -6 and smaller or equals than 121 and
      divisible by 13 (-6 and 121 are inclusive)
    * smaller than 0 and does not contain number 5 or 6

    print(lucky_guess(7))  # True
    print(lucky_guess(26))  # True
    print(lucky_guess(-35))  # False

    :param n: given number
    :return: boolean - points or no points
    """
    return (n in [1, 3, 7]) or (n >= -6 and n <= 121 and n % 13 == 0) or (n <= 0 and n not in [5, 6])


def without_end(s: str) -> str:
    """
    Given a string, return a version without the first and last char, so "Hello" yields "ell".

    The string length will be at least 2.

    without_end('Hello') → 'ell'
    without_end('java') → 'av'
    without_end('coding') → 'odin'

    :param s: String
    :return: String without first and last char.
    """
    # Return a slice from the sring without the first and last character.
    return s[1:-1]


def non_decreasing_list(nums: list) -> bool:
    """
    Given a list of numbers.

    If given list is a non-decreasing list, return True, otherwise False.
    Non-decreasing means every next element in the list must not be smaller than the previous one.

    non_decreasing_list([0, 1, 2, 3, 98]) => True
    non_decreasing_list([50, 49]) => False
    non_decreasing_list([12, 12]) => True

    :param nums:
    :return:
    """
    decreasing_list = sorted(nums, reverse=True)
    return nums != decreasing_list or nums[0] == nums[-1]


def max_duplicate(nums: list) -> int | None:
    """
    Return the largest element which has at least one duplicate.

    If no element has duplicate element (an element with the same value), return None.

    max_duplicate([1, 2, 3]) => None
    max_duplicate([1, 2, 2]) => 2
    max_duplicate([1, 2, 2, 1, 1]) => 2

    :param nums: List of integers
    :return: Maximum element with duplicate. None if no duplicate found.
    """
    # Find the largest element.
    max_element = max(nums)
    # Count how many max_elements are in the list and if there are at least two, return the element.
    # Otherwise return nothing.
    if nums.count(max_element) >= 2:
        return max_element


if __name__ == '__main__':
    print(middle_value(6, 2, 4))  # = > 4
    print(middle_value(2, 2, 4))  # = > 2
    print(middle_value(2, 6, 2))  # = > 2
    print(middle_value(88, 88, 88))  # = > 88

    print(lucky_guess(7))  # True
    print(lucky_guess(26))  # True
    print(lucky_guess(-35))  # False

    print(without_end('Hello'))  # → 'ell'
    print(without_end('java'))  # → 'av'
    print(without_end('coding'))  # → 'odin'

    print(non_decreasing_list([0, 1, 2, 3, 98]))  # = > True
    print(non_decreasing_list([50, 49]))  # = > False
    print(non_decreasing_list([12, 12]))  # = > True

    print(max_duplicate([1, 2, 3]))  # = > None
    print(max_duplicate([1, 2, 2]))  # = > 2
    print(max_duplicate([1, 2, 2, 1, 1]))  # = > 2
