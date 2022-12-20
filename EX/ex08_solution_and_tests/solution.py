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
    # If there is no amount, zero small baskets are needed.
    if ordered_amount == 0:
        return 0
    # If there is equal amount of basket capacity and ordered fruit amount
    # or the basket capacity is greater than the fruit amount ordered, check other conditions.
    elif big_baskets * 5 + small_baskets >= ordered_amount:
        # If there are no big baskets, the amount of small baskets needed is the ordered amount.
        if big_baskets == 0:
            return ordered_amount
        # If the capacity of available big baskets is equal to the ordered amount, no small baskets are needed.
        elif big_baskets * 5 == ordered_amount:
            return 0
        # If the capacity of available big baskets exceeds the ordered amount,
        # place fruits in the big baskets first.
        elif big_baskets * 5 > ordered_amount:
            # The amount of small baskets needed is the ordered amount minus the amount placed into big baskets.
            small_baskets_needed = ordered_amount - (ordered_amount // 5) * 5
        # Otherwise the amount of small baskets needed is the amount that exceeds big basket's capacity.
        else:
            small_baskets_needed = ordered_amount - big_baskets * 5

        # If there is enough small baskets, return the amount of small baskets needed.
        if small_baskets_needed <= small_baskets:
            return small_baskets_needed
            # Otherwise the order can not be placed.
        else:
            return -1
    else:
        return -1
