"""
EX08.2 - Solution and tests. Tests.

This program consists tests for the module solution.py.

Available tests:
test__students_study__evening_no_coffee_needed()
    -> Tests evening time 18-24 regardless the coffee.
test__students_study__evening_edge_case_no_coffee_needed():
    -> Tests evening time 18 or 24 regardless the coffee
test__students_study__morning_coffee_true()
    -> Tests morning time 5-17 with coffee.
test__students_study__morning_edge_case_coffee_true()
    -> Tests morning time 5 or 17 with coffee.
test__students_study__morning_coffee_false()
    -> Tests morning time 5-17 without coffee.
test__students_study__morning_edge_case_coffee_false()
    -> Tests morning time 5 or 17 without coffee.
test__students_study__night_no_coffee_needed()
    -> Tests nighttime 1-4 regardless the coffee.
test__students_study__night_edge_case_no_coffee_needed()
    -> Tests nighttime 1 or 4 regardless the coffee.

test__lottery__all_winning_numbers()
    -> Tests all winning numbers.
test__lottery__all_equal_positive_numbers()
    -> Tests all equal positive numbers but not winning numbers.
test__lottery__all_equal_zero()
    -> Tests all zeros.
test__lottery__all_equal_negative_numbers()
    -> Tests all equal negative numbers.
test__lottery__b_and_c_equal_but_not_a()
    -> Tests numbers b and c are equal with each other but not equal with a.
test__lottery__all_numbers_different()
    -> Tests all different numbers.
test__lottery__b_equal_to_a_c_different()
    -> Tests number b and number a are equal with each other but not equal to c.
test__lottery__c_equal_to_a_b_different()
    -> Tests number c and number a are equal with each other but not equal to b.

test__fruit_order__amount_zero()
    -> Tests fruit amount 0 - the order can not be placed.
test__fruit_order__no_big_baskets_no_small_baskets()
    -> Tests when there are no big and no small baskets - the order can not be placed.
test__fruit_order__no_big_baskets_not_enough_small_baskets()
    -> Tests when there are no big baskets and not enough small baskets - the order can not be placed.
test__fruit_order__no_big_baskets_enough_small_baskets()
    -> Tests when there are no big baskets but enough small baskets.
test__fruit_order__not_enough_big_baskets_no_small_baskets()
    -> Tests when there are no small baskets and not enough amount of big baskets.
test__fruit_order__not_enough_big_baskets_not_enough_small_baskets()
    -> Tests when there is not enough big baskets and the amount of fruits left does not fit into small baskets -
    the order can not be placed.
test__fruit_order__not_enough_big_baskets_enough_small_baskets()
    -> Tests when there is not enough big baskets, but the fruit amount left can be covered using small baskets.
test__fruit_order__enough_big_baskets_no_small_baskets()
    -> Tests when there is enough big baskets but there are no small baskets.
test__fruit_order__enough_big_baskets_but_not_enough_small_baskets()
    -> Tests when the amount left from big_baskets doesn't fit into small baskets - the order can not be placed.
test__fruit_order__enough_both_baskets_exact_amount()
    -> Test when the ordered amount fits into big and small baskets exactly.
test__fruit_order__enough_both_baskets_all_big_baskets_used()
    -> Tests when there is exact amount of big baskets and abundance of small baskets.
test__fruit_order__enough_both_baskets_all_small_baskets_are_used()
    -> Tests when there is abundance of big baskets and exact amount of small baskets.
test__fruit_order__enough_both_baskets()
    -> Tests when there is abundance of both (small and big) baskets.

"""


from solution import students_study
from solution import lottery
from solution import fruit_order


def test__students_study__evening_no_coffee_needed():
    """
    In the evening it doesn't matter whether we have coffee or not, students study anyway.

    Test case:
    time 18-24 (evening)
    coffee is True or False (coffee not needed).

    Expected: True
    :return:
    """
    assert students_study(20, True) is True
    assert students_study(20, False) is True
    assert students_study(22, True) is True
    assert students_study(22, False) is True


def test__students_study__evening_edge_case_no_coffee_needed():
    """
    In the evening it doesn't matter whether we have coffee or not, students study anyway.

    Test case:
    time 18 or 24 (evening)
    coffee is True or False (coffee not needed).

    Expected: True
    :return:
    """
    assert students_study(18, True) is True
    assert students_study(18, False) is True
    assert students_study(24, True) is True
    assert students_study(24, False) is True


def test__students_study__morning_coffee_true():
    """
    In the morning it's crucial to have coffee in order students can study.

    Test case:
    time 5-17 (morning)
    coffee is True

    Expected: True
    :return:
    """
    assert students_study(8, True) is True
    assert students_study(12, True) is True
    assert students_study(15, True) is True


def test__students_study__morning_edge_case_coffee_true():
    """
    In the morning it's crucial to have coffee in order students can study.

    Test case:
    time 5 or 17 (morning)
    coffee is True

    Expected: True
    :return:
    """
    assert students_study(5, True) is True
    assert students_study(17, True) is True


def test__students_study__morning_coffee_false():
    """
    In the morning it's crucial to have coffee in order students can study.

    Test case:
    time 5-17 (morning)
    coffee is False

    Expected: False
    :return:
    """
    assert students_study(9, False) is False
    assert students_study(12, False) is False
    assert students_study(13, False) is False


def test__students_study__morning_edge_case_coffee_false():
    """
    In the morning it's crucial to have coffee in order students can study.

    Test case:
    time 5 or 17 (morning)
    coffee is False

    Expected: False
    :return:
    """
    assert students_study(5, False) is False
    assert students_study(17, False) is False


def test__students_study__night_no_coffee_needed():
    """
    In the night it doesn't matter whether students receive coffee or not - they sleep.

    Test case:
    time 1-4 (night)
    coffee is True or False (coffee not needed).

    Expected: False
    :return:
    """
    assert students_study(2, True) is False
    assert students_study(2, False) is False
    assert students_study(3, True) is False
    assert students_study(3, False) is False


def test__students_study__night_edge_case_no_coffee_needed():
    """
    In the night it doesn't matter whether students receive coffee or not - they sleep.

    Test case:
    time 1 or 4 (night)
    coffee is True or False (coffee not needed).

    Expected: False
    :return:
    """
    assert students_study(1, True) is False
    assert students_study(1, False) is False
    assert students_study(4, True) is False
    assert students_study(4, False) is False


# def test_students_study__invalid_time_0():
    """
    If the time falls out of range, students do not study.

    Test case:
    time 0
    coffee is True or False

    Expected: False
    :return:
    """
    # assert students_study(0, False) is False
    # assert students_study(0, True) is False


# def test_students_study__invalid_time_28():
    """
    If the time falls out of range, students do not study.

    Test case:
    time 28
    coffee is True or False

    Expected: False
    :return:
    """
    # assert students_study(28, False) is False
    # assert students_study(28, True) is False


# def test__students_study__invalid_time_negative():
    """
    If the time falls out of range, students do not study.

    Test case:
    time -2
    coffee is True or False

    Expected: False
    :return:
    """
    # assert students_study(-2, False) is False
    # assert students_study(-2, True) is False


def test__lottery__all_winning_numbers():
    """
    All numbers are winning numbers.

    Test case:
    a == b == c == 5

    Expected: 10
    :return:
    """
    assert lottery(5, 5, 5) == 10


def test__lottery__all_equal_positive_numbers():
    """
    All numbers are equal positive numbers, but not winning numbers.

    Test case:
    a == b == c != 5

    Expected: 5
    :return:
    """
    assert lottery(3, 3, 3) == 5
    assert lottery(10, 10, 10) == 5
    assert lottery(10203, 10203, 10203) == 5


def test__lottery__all_equal_zero():
    """
    All numbers are zero.

    Test case:
    a == b == c == 0

    Expected: 5
    :return:
    """
    assert lottery(0, 0, 0) == 5


def test__lottery__all_equal_negative_numbers():
    """
    All numbers are equal negative numbers.

    Test case:
    a == b == c == -any

    Expected: 5
    :return:
    """
    assert lottery(-102, -102, -102) == 5


def test__lottery__b_and_c_equal_but_not_a():
    """
    Numbers b and c are equal with each other but not equal with number a.

    Test case:
    b == c != a

    Expected: 1
    :return:
    """
    assert lottery(5, 3, 3) == 1
    assert lottery(0, 12, 12) == 1
    assert lottery(3, 10000000000, 10000000000) == 1
    assert lottery(17, -1, -1) == 1


def test__lottery__all_numbers_different():
    """
    All numbers are different.

    Test case:
    a != b != c

    Expected: 1
    :return:
    """
    assert lottery(5, 4, 3) == 1
    assert lottery(0, 5, 1) == 1
    assert lottery(50, 5000, 5) == 1
    assert lottery(89, 52, 44) == 1
    assert lottery(-9, 2, 4) == 1
    assert lottery(9, -20, 40) == 1
    assert lottery(7, -30, 30) == 1
    assert lottery(8, 60, -60) == 1
    assert lottery(-2, 68, 2) == 1
    assert lottery(-4, 4, 2) == 1


def test__lottery__b_equal_to_a_c_different():
    """
    Number b is equal to number a.

    Test case:
    a == b != c

    Expected: 0
    :return:
    """
    assert lottery(5, 5, 3) == 0
    assert lottery(5000, 5000, 5) == 0
    assert lottery(-8, -8, 8) == 0


def test__lottery__c_equal_to_a_b_different():
    """
    Number c is equal to number a, but not equal to number b.

    Test case:
    a == c != b

    Expected: 0
    :return:
    """
    assert lottery(-7, -8, -7) == 0
    assert lottery(-66, 66, -66) == 0
    assert lottery(5, 4, 5) == 0
    assert lottery(89, 52, 89) == 0


def test__fruit_order__amount_zero():
    """
    Fruit amount ordered is 0 and order can not be placed.

    Test case:
    small_baskets == any
    big_baskets == any
    ordered_amount == 0

    Expected: 0
    :return:
    """
    assert fruit_order(5, 5, 0) == 0
    assert fruit_order(0, 0, 0) == 0
    assert fruit_order(23, 1, 0) == 0
    assert fruit_order(0, 4, 0) == 0
    assert fruit_order(200, 0, 0) == 0


def test__fruit_order__no_big_baskets_no_small_baskets():
    """
    There are no big and no small baskets.

    Test case:
    small_baskets == 0
    big_baskets == 0
    ordered_amount == any

    Expected: -1
    :return:
    """
    assert fruit_order(0, 0, 1) == -1
    assert fruit_order(0, 0, 89789) == -1


def test__fruit_order__no_big_baskets_not_enough_small_baskets():
    """
    There are no big baskets and not enough small baskets.

    Test case:
    small_baskets < ordered_amount
    big_baskets == 0
    ordered_amount == any

    Expected: -1
    :return:
    """
    assert fruit_order(8, 0, 12) == -1
    assert fruit_order(10, 0, 99999) == -1
    assert fruit_order(1, 0, 2) == -1


def test__fruit_order__no_big_baskets_enough_small_baskets():
    """
    There are no big baskets but enough small baskets.

    Test case:
    small_baskets >= ordered_amount
    big_baskets == 0
    ordered_amount == any

    Expected: ordered_amount
    :return:
    """
    assert fruit_order(1, 0, 1) == 1
    assert fruit_order(9, 0, 4) == 4
    assert fruit_order(23302, 0, 10203) == 10203
    assert fruit_order(485, 0, 485) == 485


def test__fruit_order__not_enough_big_baskets_no_small_baskets():
    """
    There are no small baskets and the amount of big baskets is not enough.

    Test case:
    small_baskets == 0
    big_baskets * 5 < ordered amount

    Expected: -1
    :return:
    """
    assert fruit_order(0, 5, 26) == -1
    assert fruit_order(0, 10, 60) == -1
    assert fruit_order(0, 300, 30000) == -1


def test__fruit_order__not_enough_big_baskets_not_enough_small_baskets():
    """
    There is not enough big baskets and the amount of fruits left does not fit into small baskets.

    Test case:
    small_baskets < ordered_amount - big_baskets * 5
    big_baskets < ordered_amount // 5
    ordered amount == any

    Expected: -1
    :return:
    """
    assert fruit_order(2, 1, 10) == -1
    assert fruit_order(1, 8, 45) == -1
    assert fruit_order(4, 1, 14) == -1
    assert fruit_order(5, 6000, 30010) == -1
    assert fruit_order(1, 50000, 250020) == -1
    assert fruit_order(23, 5, 50) == -1


def test__fruit_order__not_enough_big_baskets_enough_small_baskets():
    """
    There is not enough big baskets, but the fruit amount left can be covered using small baskets.

    Test case:

    small_baskets >= ordered_amount - big_baskets * 5
    big_baskets < ordered_amount // 5
    ordered_amount == any

    Expected: ordered_amount - big_baskets * 5
    :return:
    """
    assert fruit_order(5, 1, 10) == 5
    assert fruit_order(5, 8, 45) == 5
    assert fruit_order(9, 1, 14) == 9
    assert fruit_order(10, 6000, 30010) == 10
    assert fruit_order(25, 70, 374) == 24
    assert fruit_order(10, 10, 60) == 10
    assert fruit_order(43289, 1, 43220) == 43215


def test__fruit_order__enough_big_baskets_no_small_baskets():
    """
    There is enough big baskets but there are no small baskets.

    Test case:
    small_baskets == 0
    big_baskets >= ordered_amount // 5
    ordered_amount == any

    Expected: 0 or -1
    :return:
    """
    assert fruit_order(0, 10, 50) == 0
    assert fruit_order(0, 2, 11) == -1
    assert fruit_order(0, 100, 5) == 0
    assert fruit_order(0, 4000, 9) == -1
    assert fruit_order(0, 10203, 5008) == -1
    assert fruit_order(0, 9, 50) == -1
    assert fruit_order(0, 90, 52) == -1


def test__fruit_order__enough_big_baskets_but_not_enough_small_baskets():
    """
    Amount left from big_baskets doesn't fit into small baskets.

    Test case:
    small_baskets < ordered_amount - (ordered_amount // 5 ) * 5
    big_baskets >= ordered_amount // 5
    ordered_amount == any

    Expected: -1
    :return:
    """
    assert fruit_order(1, 1, 7) == -1
    assert fruit_order(1, 14, 7) == -1
    assert fruit_order(2, 8001, 40009) == -1
    assert fruit_order(3, 2, 14) == -1
    assert fruit_order(3, 100, 504) == -1
    assert fruit_order(3, 7890, 14) == -1
    assert fruit_order(3, 8521, 1244) == -1


def test__fruit_order__enough_both_baskets_exact_amount():
    """
    Ordered amount fits into big and small baskets exactly.

    small_baskets == ordered_amount - big_baskets
    big_baskets == ordered_amount // 5
    ordered_amount == any

    Expected: small_baskets
    :return:
    """
    assert fruit_order(1, 1, 6) == 1
    assert fruit_order(4, 50, 254) == 4
    assert fruit_order(2, 11, 57) == 2
    assert fruit_order(3, 98765, 493828) == 3


def test__fruit_order__enough_both_baskets_all_big_baskets_used():
    """
    There is exact amount of big baskets and abundance of small baskets.

    Test case:
    small_baskets > ordered_amount - big_baskets * 5
    big_baskets == ordered_amount // 5
    ordered_amount == any

    Expected: ordered_amount - big_baskets * 5
    :return:
    """
    assert fruit_order(8, 1, 6) == 1
    assert fruit_order(30, 24, 123) == 3
    assert fruit_order(45630, 2, 12) == 2
    assert fruit_order(1, 1, 5) == 0
    assert fruit_order(5890, 3000, 15000) == 0
    assert fruit_order(50, 10, 50) == 0
    assert fruit_order(50, 4, 20) == 0
    assert fruit_order(1234, 1000, 5123) == 123


def test__fruit_order__enough_both_baskets_all_small_baskets_are_used():
    """
    There is abundance of big baskets and exact amount of small baskets.

    Test case:
    small_baskets == ordered_amount - (ordered_amount // 5) * 5
    big_baskets > ordered_amount // 5
    ordered_amount == any

    Expected: small_baskets
    :return:
    """
    assert fruit_order(1, 4000, 11) == 1
    assert fruit_order(2, 100, 457) == 2
    assert fruit_order(3, 54, 28) == 3
    assert fruit_order(4, 2, 9) == 4


def test__fruit_order__enough_both_baskets():
    """
    There is abundance of both (small and big) baskets.

    Test case:
    small_baskets > ordered_amount - (ordered_amount // 5) * 5
    big_baskets > ordered_amount // 5
    ordered_amount == any

    Expected: ordered_amount - (ordered_amount // 5) * 5
    :return:
    """
    assert fruit_order(8, 114, 64) == 4
    assert fruit_order(25, 8, 34) == 4
    assert fruit_order(10, 15, 59) == 4
    assert fruit_order(123456, 7891011, 39455056) == 1
    assert fruit_order(4, 80, 352) == 2
    assert fruit_order(3, 11, 52) == 2
