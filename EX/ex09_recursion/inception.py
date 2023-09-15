"""
EX09.2 - Recursion: Inception.

This program makes different operations using loop-based functions and offering recursion-based
alternatives to them.

Available functions:
x_sum_loop(nums: list, x: int) -> int;
    -> Returns sum of every x-th number in the list on integers given, called iteratively.
x_sum_recursion(nums: list, x: int) -> int;
    -> Returns sum of every x-th number in the list on integers given, called recursively.
sum_squares(nested_list: list) -> int; Sums squares of numbers in list.
count_strings(data: list, pos=None, result: dict = None) -> dict; Counts strings in list.

"""


def x_sum_loop(nums: list, x: int) -> int:
    """
    Given a list of integers and a number called x iteratively return sum of every x-th number in the list.

    "Indexing" starts from 1, so if x = 2 and nums = [2, 3, 4, -9], the output is -6 (3 + -9).

    X can also be negative, in that case indexing starts from the end of the list, see examples below.

    If x is 0, the sum is 0.

    Examples:
    print(x_sum_loop([], 3))  # 0
    print(x_sum_loop([2, 5, 6, 0, 15, 5], 3))  # 11
    print(x_sum_loop([0, 5, 6, -5, -9, 3], 1))  # 0
    print(x_sum_loop([43, 90, 115, 500], -2))  # 158
    print(x_sum_loop([1, 2], -9))  # 0
    print(x_sum_loop([2, 3, 6], 5))  # 0
    print(x_sum_loop([6, 5, 3, 2, 9, 8, 6, 5, 4], 3))  # 15

    :param nums: list of integers
    :param x: number indicating every which num to add to sum
    :return: sum of every x-th number in the list
    """
    result = 0
    if x == 0:
        return 0
    if x < 0:
        nums.reverse()
        x = -x

    for iterator in range(x - 1, len(nums), x):
        result += nums[iterator]
    return result


def x_sum_recursion(nums: list, x: int) -> int:
    """
    Given a list of integers and a number called x recursively return sum of every x-th number in the list.

    "Indexing" starts from 1, so if x = 2 and nums = [2, 3, 4, -9], the output is -6 (3 + -9).

    X can also be negative, in that case indexing starts from the end of the list, see examples below.

    If x = 0, the sum is 0.

    Examples:
    print(x_sum_recursion([], 3))  # 0
    print(x_sum_recursion([2, 5, 6, 0, 15, 5], 3))  # 11
    print(x_sum_recursion([0, 5, 6, -5, -9, 3], 1))  # 0
    print(x_sum_recursion([43, 90, 115, 500], -2))  # 158
    print(x_sum_recursion([1, 2], -9))  # 0
    print(x_sum_recursion([2, 3, 6], 5))  # 0
    print(x_sum_recursion([6, 5, 3, 2, 9, 8, 6, 5, 4], 3))  # 15

    :param nums: list of integers
    :param x: number indicating every which num to add to sum
    :return: sum of every x-th number in the list
    """
    result = 0
    if x == 0:
        return 0
    # It is easier to reverse the list when x is negative than hack the main part of the function.
    if x < 0:
        nums.reverse()
        x = -x
    # As long as there are elements in list call the function recursively.
    if len(nums) >= x:
        # Take the first x-th number from list and add every next x-th number to it.
        # In order to find the next x-th number call the function again for the rest of the list starting from
        # the next number after the one which was added already.
        result = nums[x - 1] + x_sum_recursion(nums[x:], x)
    return result


def sum_squares(nested_list: list) -> int:
    """
    Sum squares of numbers in list.

    That list may contain additional lists.
    (Hint use the type() or isinstance() function)

    sum_squares([1, 2, 3]) -> 14
    sum_squares([[1, 2], 3]) -> sum_squares([1, 2]) + 9 -> 1 + 4 + 9 -> 14
    sum_squares([[[[[[[[[2]]]]]]]]]) -> 4

    :param nested_list: list of lists of lists of lists of lists ... and ints
    :return: sum of squares
    """
    result = 0
    if len(nested_list) > 0:
        # If the first element of the list is a list itself, call the function again separately for the first
        # element (list) and the rest of the list which elements may or may not be lists themselves.
        if isinstance(nested_list[0], list):
            result += sum_squares(nested_list[0]) + sum_squares(nested_list[1:])
        # If the first element of the list is not a list calculate the square for it and call the function
        # again for the rest of the list.
        else:
            result += nested_list[0] ** 2 + sum_squares(nested_list[1:])
    return result


def count_strings(data: list, pos=None, result: dict = None) -> dict:
    """
    Count strings in list.

    Given a list of strings and lists, which may also contain strings and lists etc., collect these strings into a dict,
    where the key is the string and value is the amount of occurrences of that string in these lists.

    Example:
    print(count_strings([[], ["J", "*", "W", "f"], ["j", "g", "*"], ["j", "8", "5", "6", "*"], ["*", "*", "A", "8"]]))
    # {'J': 1, '*': 5, 'W': 1, 'f': 1, 'j': 2, 'g': 1, '8': 2, '5': 1, '6': 1, 'A': 1}
    print(count_strings([[], [], [], [], ["h", "h", "m"], [], ["m", "m", "M", "m"]]))  # {'h': 2, 'm': 4, 'M': 1}
    print(count_strings([]))  # {}
    print(count_strings([['a'], 'b', ['a', ['b']]]))  # {'a': 2, 'b': 2}

    :param data: given list of lists
    :param pos: index of the element which is currently processed
    :param result: dictionary holding occurrences of strings in list
    :return: dict of given symbols and their count
    """
    # Only set result to an empty dictionary and position to 0 if they were not given as arguments.
    # If they were given as arguments, they already hold some information.
    if not result:
        result = {}
    if not pos:
        pos = 0
    # The position number, i.e. index can not exceed the list length minus one.
    if len(data) - 1 >= pos:
        # If the element at given position is a list itself call the same function recursively to its
        # members and start the index from the beginning of this sub-list.
        # Then give the dictionary it returns as an argument to the next element in the list the function is called.
        if isinstance(data[pos], list):
            return count_strings(data, pos + 1, count_strings(data[pos], 0, result))
        # If the element at the given position is not in the dictionary then add it and if it is then increase
        # its count by one.
        else:
            if data[pos] not in result:
                result[data[pos]] = 1
            else:
                result[data[pos]] += 1
            # Then call the function to the next element.
            # If it is a list, then it lands on the first condition block and if not then the dictionary is updated.
            count_strings(data, pos + 1, result)
    # And return the dictionary for the list.
    return result


if __name__ == "__main__":
    print("x_sum_loop: ", x_sum_loop([], 3))  # 0
    print("x_sum_loop: ", x_sum_loop([2, 5, 6, 0, 15, 5], 3))  # 11
    print("x_sum_loop: ", x_sum_loop([0, 5, 6, -5, -9, 3], 1))  # 0
    print("x_sum_loop: ", x_sum_loop([43, 90, 115, 500], -2))  # 158
    print("x_sum_loop: ", x_sum_loop([1, 2], -9))  # 0
    print("x_sum_loop: ", x_sum_loop([2, 3, 6], 5))  # 0
    print("x_sum_loop: ", x_sum_loop([6, 5, 3, 2, 9, 8, 6, 5, 4], 3))  # 15

    print("x_sum_recursion: ", x_sum_recursion([], 3))  # 0
    print("x_sum_recursion: ", x_sum_recursion([2, 5, 6, 0, 15, 5], 3))  # 11
    print("x_sum_recursion: ", x_sum_recursion([0, 5, 6, -5, -9, 3], 1))  # 0
    print("x_sum_recursion: ", x_sum_recursion([43, 90, 115, 500], -2))  # 158
    print("x_sum_recursion: ", x_sum_recursion([1, 2], -9))  # 0
    print("x_sum_recursion: ", x_sum_recursion([2, 3, 6], 5))  # 0
    print("x_sum_recursion: ", x_sum_recursion([6, 5, 3, 2, 9, 8, 6, 5, 4], 3))  # 15

    print("sum_squares: ", sum_squares([1, 2, 3]))  # -> 14
    print("sum_squares: ", sum_squares([[1, 2], 3]))  # -> sum_squares([1, 2]) + 9 -> 1 + 4 + 9 -> 14
    print("sum_squares: ", sum_squares([[[[[[[[[2]]]]]]]]]))  # -> 4

    print("count_string: ",
          count_strings([[], ["J", "*", "W", "f"], ["j", "g", "*"], ["j", "8", "5", "6", "*"], ["*", "*", "A", "8"]]))
    # {'J': 1, '*': 5, 'W': 1, 'f': 1, 'j': 2, 'g': 1, '8': 2, '5': 1, '6': 1, 'A': 1}
    print("count_string: ",
          count_strings([[], [], [], [], ["h", "h", "m"], [], ["m", "m", "M", "m"]]))  # {'h': 2, 'm': 4, 'M': 1}
    print("count_string: ", count_strings([]))  # {}
    print("count_string: ", count_strings([['a'], 'b', ['a', ['b']]]))  # {'a': 2, 'b': 2}
