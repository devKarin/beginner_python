"""
EX08.3 - OOP tests, tests.

This program consists tests for the module solution.py.

Helper function:
factory() -> Factory; Creates a Factory instance.

Available tests:
test_produce_cake_only_basic(factory);
    -> Tests the amount of basic cakes produced from given amount of toppings and base.
test_produce_cake_only_medium(factory);
    -> Tests the amount of medium cakes produced from given amount of toppings and base.
test_produce_cake_only_large(factory);
    -> Tests the amount of large cakes produced from given amount of toppings and base.
test_produce_cake_medium_remaining_ingredients_produce_more_cakes(factory);
    -> Tests the amount of medium cakes produced from given amount of toppings and base when there is more ingredients
    than needed for a medium cake.
test_produce_cake_large_remaining_ingredients_produce_more_cakes(factory);
    -> Tests the amount of large cakes produced from given amount of toppings and base when there is more ingredients
    than needed for a large cake.
test_produce_cake_get_cakes(factory);
    -> Tests the amount and instance type of cakes produced from given amount of toppings and base.
test_produce_cakes_get_last_cakes(factory);
    -> Tests the amount of cakes baked from te given ingredients amount and the correct data structure they are
    stored in (list).
test_produce_cakes_order_medium_before(factory);
    -> Tests the correct priority order of baking cakes (medium before basic).
test_produce_cakes_order_large_before(factory);
    -> Test the correct priority order of baking cakes (large before basic).
test_get_cakes_correct_amount(factory);
    -> Tests the amount of cakes baked.
test_get_last_cakes_correct_amount(factory);
    -> Tests the querying of last cakes produced (using function get_last_cakes).
test_get_cakes_returns_cakes(factory);
    -> Tests whether the factory stores and returns cakes as Cake instances when queried using get_cakes_baked function.
test_get_last_cakes_returns_cakes(factory);
    -> Tests whether the factory stores and returns cakes as Cake instances when queried using get_last_cakes function.
test_produce_cakes_order(factory);
    -> Tests the correct priority order of baking cakes ("large", "medium", "basic").
test_cake_basic();
    -> Tests the correctness of "basic" cake type.
test_cake_medium();
    -> Tests the correctness of "medium" cake type.
test_cake_large();
    -> Tests the correctness of "large" cake type.
test_cake_wrong_ingredients_throws_exception();
    -> Tests whether wrong amount of ingredients raises the WrongIngredientsAmountException.
test_cake_equals();
    -> Tests comparing cakes.
test_cake_repr();
    -> Tests the correctness of Cake representation.
test_factory_str_amount(factory);
    -> Test the string representation of Factory when factory has at least 2 cakes.
test_factory_str_single(factory);
    -> Test the string representation of Factory when factory has only 1 cake.

"""


import random
import pytest
from solution import Factory, Cake, WrongIngredientsAmountException


@pytest.fixture
def factory() -> Factory:
    """
    Create a Factory instance.

    :return: a Factory class instance
    """
    return Factory()


def test_produce_cake_only_basic(factory):
    """
    Test the amount of cakes produced from given amount of toppings and base.

    Test case:
    Bake only basic cake.
    1kg toppings and 1kg base.

    Expected: 1 basic cake

    :param factory: factory which produces cakes
    :return:
    """
    amount = factory.bake_cake(1, 1)
    assert amount == 1


@pytest.mark.dependency()
def test_produce_cake_only_medium(factory):
    """
    Test the amount of cakes produced from given amount of toppings and base.

    Test case:
    Bake only medium cakes.
    2kg toppings and 2kg base -> expected 1 medium cake
    4kg toppings and 4kg base -> expected 2 medium cakes

    :param factory: factory which produces cakes
    :return:
    """
    assert factory.bake_cake(2, 2) == 1
    assert factory.bake_cake(4, 4) == 2


@pytest.mark.dependency()
def test_produce_cake_only_large(factory):
    """
    Test the amount of cakes produced from given amount of toppings and base.

    Test case:
    Bake only large cakes.
    5kg toppings and 5kg base -> expected 1 large cake
    10kg toppings and 10kg base -> expected 2 large cakes

    :param factory: factory which produces cakes
    :return:
    """
    assert factory.bake_cake(5, 5) == 1
    assert factory.bake_cake(10, 10) == 2


@pytest.mark.dependency(depends=["test_produce_cake_only_medium"])
def test_produce_cake_medium_remaining_ingredients_produce_more_cakes(factory):
    """
    Test the amount of cakes produced from given amount of toppings and base.

    Test case:
    Bake medium cakes but take the priority order of baking cakes into account (large -> medium -> basic).
    3kg toppings and 3kg base -> expected not 1 medium cake (but 1 medium and 1 basic cake)
    5kg toppings and 5kg base -> expected not 2 medium cakes (but 1 large cake)

    :param factory: factory which produces cakes
    :return:
    """
    assert factory.bake_cake(3, 3) != 1
    assert factory.bake_cake(5, 5) != 2


@pytest.mark.dependency(depends=["test_produce_cake_only_large"])
def test_produce_cake_large_remaining_ingredients_produce_more_cakes(factory):
    """
    Test the amount of cakes produced from given amount of toppings and base.

    Test case:
    Bake large cakes but take the priority order of baking cakes into account (large -> medium -> basic).
    6kg toppings and 6kg base -> expected not 1 large cake (but 1 large and 1 basic cake)
    11kg toppings and 11kg base -> expected not 2 large cakes (but 2 large cakes and 1 basic cake)

    :param factory: factory which produces cakes
    :return:
    """
    assert factory.bake_cake(6, 6) != 1
    assert factory.bake_cake(11, 11) != 2


def test_produce_cake_get_cakes(factory):
    """
    Test the amount and instance type of cakes produced from given amount of toppings and base.

    Test case:
    Bake a basic cake (1kg toppings and 1kg base). Get baked cakes and get the last cake baked.

    Expected: List with 1 cake, the last cake baked is not None and is an instance of Cake class.

    :param factory: factory which produces cakes
    :return:
    """
    factory.bake_cake(1, 1)
    assert len(factory.get_cakes_baked()) == 1
    cake = factory.get_last_cakes(1)[0]
    assert cake is not None
    assert type(cake) == Cake


def test_produce_cakes_get_last_cakes(factory):
    """
    Test the amount of cakes baked from te given ingredients amount and the correct data structure they are stored in.

    Test whether amount of cakes baked is correct and the cakes are stored in factory cake list.
    Test whether the get_last_cakes function returns requested amount of last baked cakes as a list.

    Test case:
    Cake with 3kg toppings and 3kg base.

    Expected:
    1) amount of cakes 2
    2) function get_last_cakes returns cakes as a list when 2 last cakes is requested
    3) the length of the cake list is 2 when 2 last cakes are requested
    4) function get_last_cakes returns cakes as a list even when only 1 last cake is requested
    5) the length of the cake list is 1 when 1 last cake is requested

    :param factory: factory which produces cakes
    :return:
    """
    amount = factory.bake_cake(3, 3)
    assert amount == 2
    cakes = factory.get_last_cakes(2)
    assert type(cakes) == list
    assert len(cakes) == 2
    cakes = factory.get_last_cakes(1)
    assert type(cakes) == list
    assert len(cakes) == 1


def test_produce_cakes_order_medium_before(factory):
    """
    Test the correct priority order of baking cakes.

    Test whether the medium type of cake is produced before basic type of cake when there is abundance of ingredients.

    Test case:
    3 kg toppings, 3kg base

    Expected:
    Cakes should be produced and stored in order: "medium" , not "medium" (basic).

    :param factory: factory which produces cakes
    :return:
    """
    factory.bake_cake(3, 3)
    cakes = factory.get_last_cakes(2)
    assert cakes
    assert cakes[0].type == "medium"
    assert cakes[1].type != "medium"


def test_produce_cakes_order_large_before(factory):
    """
    Test the correct priority order of baking cakes.

    Test whether the large type of cake is produced before other types of cake when there is abundance of ingredients.

    Test case:
    6kg toppings, 6kg base

    Expected:
    Cakes should be produced and stored in order: "large" , not "large" (basic).

    :param factory: factory which produces cakes
    :return:
    """
    factory.bake_cake(6, 6)
    cakes = factory.get_last_cakes(2)
    assert cakes[0].type == "large"
    assert cakes[1].type != "large"


@pytest.mark.dependency()
def test_get_cakes_correct_amount(factory):
    """
    Test the amount of cakes baked.

    Test the amount of cakes baked when different type of cakes can be produced from the amount of ingredients given.

    Test case:
    Bake cakes from 9kg toppings and 9kg base.

    Expected: 3

    :param factory: factory which produces cakes
    :return:
    """
    factory.bake_cake(9, 9)
    assert len(factory.get_cakes_baked()) == 3


@pytest.mark.dependency()
def test_get_last_cakes_correct_amount(factory):
    """
    Test the querying of last cakes produced.

    Tests whether the function get_last_cakes returns the list of cakes last produced with the correct length.

    Test case:
    Bake cakes from 9kg toppings and 9kg base.
    Get the last:
    1) 0 cakes,
    2) 1 cake,
    3) 2 cakes.

    Expected:
    The length of list last baked cakes is:
    1) 0
    2) 1
    3) 2

    :param factory: factory which produces cakes
    :return:
    """
    factory.bake_cake(9, 9)
    for i in range(0, 3):
        assert len(factory.get_last_cakes(i)) == i


@pytest.mark.dependency(depends=["test_get_cakes_correct_amount"])
def test_get_cakes_returns_cakes(factory):
    """
    Test whether the factory stores cakes as Cake instances.

    Tests whether the function get_cakes_baked returns Cake instances stored in factory.

    Test case:
    Bake cakes from 9kg toppings and 9kg base.
    Query all cakes using function get_cakes_baked.
    Check the type of all cakes listed.

    Expected: Type of Cake

    :param factory: factory which produces cakes
    :return:
    """
    factory.bake_cake(9, 9)
    assert all(type(cake) == Cake for cake in factory.get_cakes_baked())


@pytest.mark.dependency(depends=["test_get_cakes_correct_amount"])
def test_get_last_cakes_returns_cakes(factory):
    """
    Test whether the factory stores cakes as Cake instances.

    Tests whether the function get_last_cakes returns Cake instances stored in factory.

    Test case:
    Bake cakes from 9kg toppings and 9kg base.
    Query all cakes using function get_last_cakes.
    Check the type of all cakes listed.

    Expected: Type of Cake

    :param factory: factory which produces cakes
    :return:
    """
    factory.bake_cake(9, 9)
    assert all(type(cake) == Cake for cake in factory.get_last_cakes(4))


@pytest.mark.dependency(depends=["test_get_cakes_correct_amount", "test_get_last_cakes_correct_amount"])
def test_produce_cakes_order(factory):
    """
    Test the correct priority order of baking cakes.

    Tests whether the cakes are produced in correct priority order: first large, then medium and finally basic cakes.

    Test case:
    Bake cakes from 8kg toppings and 8kg base.

    Expected:
    1) 3 cakes baked (the length of cake list when queried using function get_cakes_baked).
    2) the types of cakes returned by function get_last_cakes are in following order: "large", "medium", "basic".

    :param factory: factory which produces cakes
    :return:
    """
    factory.bake_cake(8, 8)
    assert len(factory.get_cakes_baked()) == 3
    cakes = factory.get_last_cakes(3)
    assert cakes[2].type == "basic"
    assert cakes[1].type == "medium"
    assert cakes[0].type == "large"


def test_cake_basic():
    """
    Test cake type.

    Test case:
    Test the type of the cake when it has:
    1kg of toppings and
    1kg of base.

    Expected: "basic"

    :return:
    """
    basic_cake = Cake(1, 1)
    assert basic_cake.type == "basic"


def test_cake_medium():
    """
    Test cake type.

    Test case:
    Test the type of the cake when it has:
    2kg of toppings and
    2kg of base.

    Expected: "medium"

    :return:
    """
    medium_cake = Cake(2, 2)
    assert medium_cake.type == "medium"


def test_cake_large():
    """
    Test cake type.

    Test case:
    Test the type of the cake when it has:
    5kg of toppings and
    5kg of base.

    Expected: "large"

    :return:
    """
    large_cake = Cake(5, 5)
    assert large_cake.type == "large"


def test_cake_wrong_ingredients_throws_exception():
    """
    Test raising the WrongIngredientsAmountException when cake has wrong amount of ingredients.

    Test case:
    Ingredients amount between 0 and 1000 (exclusive).

    Expected: raise WrongIngredientsAmountException when trying to instantiate with other amounts than 1, 2 or 5.

    :return:
    """
    for i in {i for i in range(1000)} - {1, 2, 5}:
        with pytest.raises(WrongIngredientsAmountException):
            Cake(i, i)


def test_cake_equals():
    """
    Test comparing cakes.

    Test cases:
    1) cake with toppings amount of 1kg and base amount of 1kg compared to a cake with 1kg toppings and 1kg base
    2) cake with toppings amount of 2kg and base amount of 2kg compared to a cake with 2kg toppings and 2kg base
    3) cake with toppings amount of 5kg and base amount of 5kg compared to a cake with 5kg toppings and 5kg base

    Expected: True

    :return:
    """
    cake_basic_1 = Cake(1, 1)
    cake_basic_2 = Cake(1, 1)
    cake_medium_1 = Cake(2, 2)
    cake_medium_2 = Cake(2, 2)
    cake_large_1 = Cake(5, 5)
    cake_large_2 = Cake(5, 5)
    assert cake_basic_1 == cake_basic_2
    assert cake_medium_1 == cake_medium_2
    assert cake_large_1 == cake_large_2


def test_cake_repr():
    """
    Test the correctness of Cake representation.

    Test case:
    1) cake with 1kg toppings and 1kg base
    2) cake with 2kg toppings and 2kg base
    3) cake with 5kg toppings and 5kg base

    Expected:
    1) "Cake(basic)"
    2) "Cake(medium)"
    3)  "Cake(large)"

    :return:
    """
    cake_basic = Cake(1, 1)
    cake_medium = Cake(2, 2)
    cake_large = Cake(5, 5)
    assert cake_basic.__repr__() == "Cake(basic)"
    assert cake_medium.__repr__() == "Cake(medium)"
    assert cake_large.__repr__() == "Cake(large)"


def test_factory_str_amount(factory):
    """
    Test the string representation of Factory.

    Tests the correct formatting of string representing a Factory instance.

    Test case:
    A factory instance with random number of cakes ranging between 2 and 999.

    Expected: "Factory with <cake amount> cakes."
    :param factory: factory which produces cakes
    :return:
    """
    num = random.randint(3, 1000)
    for x in [(1, 1) for _ in range(2, num)]:
        factory.bake_cake(*x)
    assert str(factory) == f"Factory with {num - 2} cakes."


def test_factory_str_single(factory):
    """
    Test the string representation of Factory.

    Tests the correct formatting of string representing a Factory instance.

    Test case:
    A factory instance with 1 cake.

    Expected:
    "Factory with 1 cake."

    :param factory: factory which produces cakes
    :return:
    """
    factory.bake_cake(1, 1)
    assert str(factory) == "Factory with 1 cake."
