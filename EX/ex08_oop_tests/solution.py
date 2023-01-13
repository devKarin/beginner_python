"""
EX08.3 - OOP tests. Solution.

This program makes operations with cakes and factory which produces them and is tested using module test.py.

This program gets information about bank clients.

Available classes:
Factory; Factory class
Cake; Cake class
WrongIngredientsAmountException; WrongIngredientsAmountException class, extends the built-in Exception class.

Functions in Factory class:
__init__(self); Factory constructor.
__repr__(self); Factory representation.
__str__(self); Factory's string representation, contains information about the amount of cakes the factory has.
bake_cake(self, toppings: int, base: int) -> int; Bake cakes from ingredients, returns the amount of cakes baked.
get_last_cakes(self, n: int) -> list; Gets last n cakes baked as a list.
get_cakes_baked(self) -> list; Gets the list of all cakes baked.

Functions in Cake class:
__init__(self, base_amount, toppings_amount);
    -> Cake constructor. Every cake has toppings, a base and a type based on the amount of toppings and base.
@property def type(self);
    -> Determines the type of the cake. If the type of te cake can not be determined, a WrongIngredientsAmountException
    exception will be raised during cake initialisation.
__repr__(self); Cake representation.
__eq__(self, other) -> bool; Compares the equality of cakes.

"""


class Factory:
    """
    Factory class.

    The Factory class describes the factory.
    """

    def __init__(self):
        """
        Initialise the Factory class.

        Every factory contains cakes represented as a list.
        """
        self.cakes = []

    def __repr__(self):
        """
        Return factory representation.

        Returns Factory data as a formatted string containing the amount of cakes factory has.
        :return: string representation of factory data containing the amount of cake it has
        """
        return f"Factory with {len(self.cakes)} cake."

    def bake_cake(self, toppings: int, base: int) -> int:
        """
        Bake cakes from ingredients.

        First try bake large cakes, then medium cakes and finally small cakes.
        One big cake requires 5kg toppings and 5kg base, medium cake requires 2kg toppings and 2kg base and
        small cake requires 1kg toppings and 1kg base.
        :param toppings: the amount of toppings to bake cakes
        :param base: the amount of base to bake cakes
        :return: the amount of cakes baked
        """
        # One big cake requires 5kg toppings and 5kg base.
        # Calculate how many big cakes can be baked.
        big_cakes = min([toppings // 5, base // 5])
        # One medium cake requires 2kg toppings and 2kg base.
        # Subtract big cakes before calculating the amount of medium cakes.
        medium_cakes = min([(toppings - big_cakes * 5) // 2, (base - big_cakes * 5) // 2])
        # Warning! The minimum value can be negative and thereby must be verified.
        small_cakes = min([toppings - big_cakes * 5 - medium_cakes * 2, base - big_cakes * 5 - medium_cakes * 2])

        # If there is not enough ingredients, do not bake small cakes.
        if small_cakes < 0:
            small_cakes = 0

        for i in range(big_cakes):
            cake = Cake(5, 5)
            self.cakes.append(cake)
        for i in range(medium_cakes):
            cake = Cake(2, 2)
            self.cakes.append(cake)
        for i in range(small_cakes):
            cake = Cake(1, 1)
            self.cakes.append(cake)

        return big_cakes + medium_cakes + small_cakes

    def get_last_cakes(self, n: int) -> list:
        """
        Get last n cakes baked.

        Returns last n cakes baked as a list.
        :param n: the amount of last cakes to get
        :return: list of last n baked cakes
        """
        # If last 0 cakes are requested, there can not be cakes to return.
        if n <= 0:
            return []
        else:
            return self.cakes[-n:]

    def get_cakes_baked(self) -> list:
        """
        Get the list of all cakes baked.

        Returns the list of cakes the factory has.
        :return: list of all cakes
        """
        return self.cakes

    def __str__(self):
        """
        Factory's string representation.

        Returns Factory data as a formatted string containing the amount of cakes factory has.
        :return: string containing factory data - the amount of cakes the factory has
        """
        if len(self.cakes) == 1:
            singular_or_plural = "cake"
        else:
            singular_or_plural = "cakes"
        return f"Factory with {len(self.cakes)} {singular_or_plural}."


class Cake:
    """
    Cake class.

    The Cake class describes the cake.
    """

    def __init__(self, base_amount, toppings_amount):
        """
        Initialise the Cake class.

        Every cake has toppings, a base and a type based on the amount of toppings and base.
        When cake can not be typed, it has a wrong amount of ingredients and an exception will be raised when
        initialising.
        :param base_amount: the amount of base the cake has
        :param toppings_amount: the amount of toppings the cake has
        """
        self.base_amount = base_amount
        self.toppings_amount = toppings_amount
        # If there is a wrong amount of ingredients, raise an exception when cake is initialised.
        if not self.type:
            raise WrongIngredientsAmountException

    @property
    def type(self):
        """
        Type the cake.

        Returns the type of the cake - basic, medium or large.
        Large cake has 5kg of toppings and the same amount of base, medium cake has 2 kg toppings and 2kg base and
        the basic cake has 1kg toppings and 1kg base.
        :return: the type of cake as a string
        """
        if self.base_amount == self.toppings_amount == 1:
            return "basic"
        elif self.base_amount == self.toppings_amount == 2:
            return "medium"
        elif self.base_amount == self.toppings_amount == 5:
            return "large"

    def __repr__(self):
        """
        Cake representation.

        Returns the cake data as a formatted string containing cake type.
        :return: string representation of cake data containing its type
        """
        return f"Cake({self.type})"

    def __eq__(self, other) -> bool:
        """
        Compare cake equality.

        Cakes are considered to be equal if their toppings amount and base amounts are equal to each other.
        :param other: a cake to compare
        :return: boolean value (True or False) about cake equality
        """
        return self.base_amount == other.base_amount and self.toppings_amount == other.toppings_amount


class WrongIngredientsAmountException(Exception):
    """
    WrongIngredientsAmountException class.

    WrongIngredientsAmountException extends the built-in Exception class and is raised when the cake has wrong amount
    of ingredients.
    """

    pass


if __name__ == "__main__":
    factory = Factory()

    # print("Bake 1 small cake: ", factory.bake_cake(1, 1))
    # print("Bake 1 medium cake: ", factory.bake_cake(2, 2))
    factory.bake_cake(9, 9)
    print("Last cakes: ", factory.get_last_cakes(0), len(factory.get_last_cakes(0)))
    print("Last cakes: ", factory.get_last_cakes(1), len(factory.get_last_cakes(1)))
    print("Last cakes: ", factory.get_last_cakes(2), len(factory.get_last_cakes(2)))
    print("Last cakes: ", factory.get_last_cakes(3), len(factory.get_last_cakes(3)))
    print(factory.cakes)
