"""
EX08.2 - Solution and tests. Solution.

This program consists functions written in testing purpose and to be tested using module test.py.

Available functions:
students_study(time: int, coffee_needed: bool) -> bool; Returns True if students study in given circumstances.
lottery(a: int, b: int, c: int) -> int; Return Lottery victory result according to input values.
fruit_order(small_baskets: int, big_baskets: int, ordered_amount: int)-> int;
    Returns number of small fruit baskets if it's possible to finish the order, otherwise returns -1.

"""


def students_study(time: int, coffee_needed: bool) -> bool:
    """
    Return True if students study in given circumstances.

    (19, False) -> True
    (1, True) -> False.
    """
    # In the evening coffee is not important, students study anyway.
    if 18 <= time <= 24:
        return True
    # In the morning coffee is extremely important, students study only with coffee.
    elif 5 <= time <= 17 and coffee_needed:
        return True
    # In the night coffee is not important, students do not study, but sleep.
    # Actually this is redundant condition - in any other case students do not study.
    elif 1 <= time <= 4:
        return False
    else:
        return False


def lottery(a: int, b: int, c: int) -> int:
    """
    Return Lottery victory result 10, 5, 1, or 0 according to input values.

    (5, 5, 5) -> 10
    (2, 2, 1) -> 0
    (2, 3, 1) -> 1
    """
    # If all the numbers are equal to 5, max winning result is received.
    if a == b == c == 5:
        return 10
    # If all the numbers are equal, but not equal to 5, medium winning result is received.
    elif a == b == c != 5:
        return 5
    # If b and c differ from a at the same time, the winning result is 1.
    elif a != b and a != c:
        return 1
    # If b or c are equal to a, the winning result is 0.
    elif b == a or a == c:
        return 0


def fruit_order(small_baskets: int, big_baskets: int, ordered_amount: int) -> int:
    """
    Return number of small fruit baskets if it's possible to finish the order, otherwise return -1.

    (4, 1, 9) -> 4
    (3, 1, 10) -> -1
    """
    # If there's no amount, the order can not be placed.
    if ordered_amount == 0:
        return -1
    # If big baskets are zero, don't divide by zero
    # and if there's not enough small baskets, the order can't be fulfilled.
    elif big_baskets == 0 and small_baskets < ordered_amount:
        return -1
    # If there are no big baskets, but enough small baskets, small baskets' count is equal to ordered amount.
    elif big_baskets == 0:
        return ordered_amount
    # If there are big and small baskets, but the amount left doesn't fit into small baskets,
    # the order can not be fulfilled.
    elif ordered_amount - big_baskets * 5 > small_baskets:
        return -1
    # If there are enough big and small baskets, return how many small baskets are needed and thereby used.
    else:
        return ordered_amount - big_baskets * 5

