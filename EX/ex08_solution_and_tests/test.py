"""
EX08.2 - Solution and tests. Tests.

This program consists tests for the module solution.py.

Available tests:
test__students_study__evening_no_coffee_needed()
    -> Tests evening time 18-24 regardless the coffee.
test__students_study__morning_coffee_true()
    -> Tests morning time 5-17 with coffee.
test__students_study__morning_coffee_false()
    -> Tests morning time 5-17 without coffee.
test__students_study__night_no_study()
    -> Tests night time 1-4 regardless the coffee.
test_students_study__invalid_time_0()
    -> Tests out of range time 0 regardless the coffee.
test_students_study__invalid_time_28()
    -> Tests out of range time 28 regardless the coffee.
test__students_study__invalid_time_negative()
    -> Tests out of range time -2 regardless the coffee.
test__lottery__all_winning_numbers()
    -> Tests all winning numbers.
test__lottery__all_equal_numbers()
    -> Tests all equal numbers but not winning numbers.
test__lottery__b_and_c_equal_but_not_a()
    -> Tests numbers b and c are equal with each other but not equal with a.
test__lottery__all_numbers_different()
    -> Tests all different numbers.
test__lottery__one_number_equal_to_a()
    -> Tests number b or c are equal to a.
test__fruit_order__no_amount()
    -> Tests fruit amount 0 - the order can not be placed.
test__fruit_order__no_big_baskets()
    -> Tests big baskets 0.
test__fruit_order__no_small_baskets()
    -> Tests small baskets 0.
test__fruit_order__incorrect_amount()
    -> Tests incorrect amount which doesn't add up - the order can not be placed.
test__fruit_order__correct_amount()
    -> Tests correct amount which adds up - the order can be placed.
test__fruit_order__negative_amount()
    -> Tests negative fruit amount - the order can not be placed.
test__fruit_order__negative_baskets()
    -> Tests negative basket values - the order can not be placed.

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
    assert students_study(5, False) is False
    assert students_study(17, False) is False


def test__students_study__night_no_study():
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
    assert students_study(1, True) is False
    assert students_study(1, False) is False
    assert students_study(4, True) is False
    assert students_study(4, False) is False


def test_students_study__invalid_time_0():
    """
    If the time falls out of range, students do not study.

    Test case:
    time 0
    coffee is True or False

    Expected: False
    :return:
    """
    assert students_study(0, False) is False
    assert students_study(0, True) is False


def test_students_study__invalid_time_28():
    """
    If the time falls out of range, students do not study.

    Test case:
    time 28
    coffee is True or False

    Expected: False
    :return:
    """
    assert students_study(28, False) is False
    assert students_study(28, True) is False


def test__students_study__invalid_time_negative():
    """
    If the time falls out of range, students do not study.

    Test case:
    time -2
    coffee is True or False

    Expected: False
    :return:
    """
    assert students_study(-2, False) is False
    assert students_study(-2, True) is False


def test__lottery__all_winning_numbers():
    """
    All numbers are winning numbers.

    Test case:
    a == b == c == 5

    Expected: 10
    :return:
    """
    assert lottery(5, 5, 5) == 10


def test__lottery__all_equal_numbers():
    """
    All numbers are equal numbers, but not winning numbers.

    Test case:
    a == b == c != 5

    Expected: 5
    :return:
    """
    assert lottery(3, 3, 3) == 5
    assert lottery(0, 0, 0) == 5
    assert lottery(10, 10, 10) == 5
    assert lottery(10203, 10203, 10203) == 5
    assert lottery(-102, -102, -102) == 5


def test__lottery__b_and_c_equal_but_not_a():
    """
    Numbers b and c are equal with each other but not equal with a.

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


def test__lottery__one_number_equal_to_a():
    """
    Number b or c are equal to a.

    Test case:
    a == b or a== c

    Expected: 0
    :return:
    """
    assert lottery(5, 5, 3) == 0
    assert lottery(5, 4, 5) == 0
    assert lottery(5000, 5000, 5) == 0
    assert lottery(89, 52, 89) == 0
    assert lottery(-8, -8, 8) == 0
    assert lottery(-7, -8, -7) == 0
    assert lottery(-66, 66, -66) == 0


def test__fruit_order__no_amount():
    """
    Fruit amount ordered is 0 and order can not be placed.

    Test case:
    small_baskets == any
    big_baskets == any
    ordered_amount == 0

    Expected: -1
    :return:
    """
    assert fruit_order(5, 5, 0) == -1
    assert fruit_order(0, 0, 0) == -1
    assert fruit_order(23, 1, 0) == -1


def test__fruit_order__no_big_baskets():
    """
    No big baskets are ordered.

    Test case:
    small_baskets == any
    big_baskets == 0
    ordered_amount == any

    Expected: small_baskets
    :return:
    """
    assert fruit_order(12, 0, 12) == 12
    assert fruit_order(9, 0, 9) == 9
    assert fruit_order(230, 0, 230) == 230


def test__fruit_order__no_small_baskets():
    """
    No big small baskets are ordered.

    Test case:
    small_baskets == 0
    big_baskets == any
    ordered_amount == any

    Expected: 0
    :return:
    """
    assert fruit_order(0, 2, 10) == 0
    assert fruit_order(0, 5, 25) == 0
    assert fruit_order(0, 9999, 49995) == 0


def test__fruit_order__incorrect_amount():
    """
    The amount of fruits in big and small baskets doesn't add up.

    Test case:
    big_baskets == any
    small_baskets == any
    big_baskets * 5 + small_baskets != ordered_amount


    Expected: -1
    :return:
    """
    assert fruit_order(1, 4, 16) == -1
    assert fruit_order(0, 5, 40) == -1
    assert fruit_order(101, 0, 5) == -1
    assert fruit_order(1, 3, 15) == -1
    assert fruit_order(12, 12, 12) == -1


def test__fruit_order__correct_amount():
    """
    The amount of fruits in big and small baskets adds up.

    Test case:
    big_baskets == any
    small_baskets == any
    big_baskets * 5 + small_baskets == ordered_amount


    Expected: small_baskets
    :return:
    """
    assert fruit_order(1, 4, 21) == 1
    assert fruit_order(1, 3, 16) == 1
    assert fruit_order(101, 0, 101) == 101
    assert fruit_order(55, 3, 70) == 55
    assert fruit_order(12, 12, 72) == 12


def test__fruit_order__negative_amount():
    """
    The amount of fruits is negative and the order can not be placed.

    Test case:
    big_baskets == any
    small_baskets == any
    ordered_amount == -any


    Expected: -1
    :return:
    """
    assert fruit_order(1, 4, -21) == -1
    assert fruit_order(1, 3, -16) == -1
    assert fruit_order(101, 0, -101) == -1
    assert fruit_order(55, 3, -70) == -1
    assert fruit_order(12, 12, -0) == -1


def test__fruit_order__negative_baskets():
    """
    The amount of fruits is negative and the order can not be placed.

    Test case:
    big_baskets == any
    small_baskets == any
    ordered_amount == -any


    Expected: -1
    :return:
    """
    assert fruit_order(1, -4, 21) == -1
    assert fruit_order(-1, 3, 16) == -1
    assert fruit_order(-101, 0, -101) == -1
    assert fruit_order(-55, -3, 70) == -1
    assert fruit_order(55, -3, -70) == -1
    assert fruit_order(12, -12, -0) == -1
