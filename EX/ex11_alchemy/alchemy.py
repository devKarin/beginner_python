"""
EX11.1 - Alchemy.

This program organises alchemical elements.

Available classes:
AlchemicalElement; AlchemicalElement class
AlchemicalStorage; AlchemicalStorage class
AlchemicalRecipes; AlchemicalRecipes class
DuplicateRecipeNamesException; DuplicateRecipeNamesException class, extends the Exception class.
RecipeOverlapException; RecipeOverlapException class, extends the Exception class.
Cauldron; Cauldron class, extends the AlchemicalStorage class.
Catalyst; Catalyst class, extends the AlchemicalElement class.
Purifier; Purifier class, extends the AlchemicalStorage class.

Methods in AlchemicalElement class:
__init__; AlchemicalElement constructor. Every element has a name.
__repr__; AlchemicalElement representation. Returns element name as a formatted string.

Methods in AlchemicalStorage class:
__init__; AlchemicalStorage constructor. Storage is initially an empty list.
add(self, element: AlchemicalElement); Adds object with the type of AlchemicalElement into storage.
pop(self, element_name: str) -> AlchemicalElement | None;
    -> Removes and returns previously added element from storage by its name.
extract(self) -> list[AlchemicalElement]; Returns a list of all the elements from storage and empties the storage.
get_content(self) -> str; Returns a string that gives an overview of the contents of the storage.

Methods in AlchemicalRecipes class:
__init__(self); AlchemicalRecipes constructor. Recipes object is initially an empty dictionary.
add_recipe(self, first_component_name: str, second_component_name: str, product_name: str);
    -> Determines if recipe is valid and then add it to recipes.
get_product_name(self, first_component_name: str, second_component_name: str) -> str or None;
    -> Returns the name of the product for the two components in recipe.
get_component_names(self, product_name: str) -> tuple[str, str] or None;
    -> Return the names of the components for the product in recipe.

Methods in Cauldron class:
__init__(self, recipes: AlchemicalRecipes); Cauldron class constructor.
    -> Uses base class (AlchemicalStorage) constructor and extends it with recipes from AlchemicalRecipes class.
add(self, element: AlchemicalElement);
    -> Adds element to storage and checks if it can combine with anything already inside.

Methods in Catalyst class:
__init__(self, name: str, uses: int); Catalyst class constructor.
    -> Uses base class (AlchemicalElement) constructor and extends it with uses attribute.
__repr__(self) -> str; AlchemicalElement representation. Returns element name as a formatted string.

Methods in Purifier class:
__init__(self, recipes: AlchemicalRecipes); Purifier class constructor.
    -> Uses base class (AlchemicalStorage) constructor and extends it with recipes from AlchemicalRecipes class.
add(self, element: AlchemicalElement); Adds element to storage and checks whether it can be split into anything.

"""


class AlchemicalElement:
    """
    AlchemicalElement class.

    Every element must have a name.
    """

    def __init__(self, name: str):
        """
        Initialize the AlchemicalElement class.

        Every element has a name.
        """
        self.name = name

    def __repr__(self) -> str:
        """
        Representation of AlchemicalElement.

        Returns element name as a formatted string.
        :return:
        """
        return f"<AE: {self.name}>"


class AlchemicalStorage:
    """AlchemicalStorage class."""

    def __init__(self):
        """
        Initialize the AlchemicalStorage class.

        Storage is initially an empty list.
        """
        self.storage = []

    def add(self, element: AlchemicalElement):
        """
        Add element to storage.

        Check whether the element is an instance of AlchemicalElement, and if not
        raise the built-in TypeError exception.

        :param element: Input object to add to storage.
        """
        # Check whether the element is a type of AlchemicalElement before adding it into storage.
        # If not, raise a TypeError.
        if not isinstance(element, AlchemicalElement):
            raise TypeError
        self.storage.append(element)
        return element

    def pop(self, element_name: str) -> AlchemicalElement | None:
        """
        Remove and return previously added element from storage by its name.

        If there are multiple elements with the same name, remove only the one that was added most recently to the
        storage. If there are no elements with the given name, do not remove anything and return None.

        :param element_name: Name of the element to remove.
        :return: The removed AlchemicalElement object or None.
        """
        # Use the built-in reversed function to loop storage backwards.
        for item in reversed(self.storage):
            # If the element name matches item name, then find the index of it and remove it from storage using
            # pop method.
            # Pop method returns the element which it removes so return that (and stop looping).
            # If the element can not be found, the function returns None anyway so there is no need to specify it.
            if item.name == element_name:
                return self.storage.pop(self.storage.index(item))

    def extract(self) -> list[AlchemicalElement]:
        """
        Return a list of all the elements from storage and empty the storage itself.

        Order of the list must be the same as the order in which the elements were added.

        Example:
            storage = AlchemicalStorage()
            storage.add(AlchemicalElement('Water'))
            storage.add(AlchemicalElement('Fire'))
            storage.extract() # -> [<AE: Water>, <AE: Fire>]
            storage.extract() # -> []

        In this example, the second time we use .extract() the output list is empty because we already extracted
         everything.

        :return: A list of all the elements that were previously in the storage.
        """
        # Make a copy from the list. The new list points into different location in memory, but the objects should
        # be still the same, because only the references were stored in storage list. I hope I am not wrong.
        # This way the list still can be returned after clearing the storage.
        previously_stored = self.storage[0:]
        self.storage = []
        return previously_stored

    def get_content(self) -> str:
        """
        Return a string that gives an overview of the contents of the storage.

        Example:
            storage = AlchemicalStorage()
            storage.add(AlchemicalElement('Water'))
            storage.add(AlchemicalElement('Fire'))
            print(storage.get_content())

        Output in console:
            Content:
             * Fire x 1
             * Water x 1

        The elements must be sorted alphabetically by name.

        :return: Content as a string.
        """
        # Initiate the final output string.
        output = "Content:"
        # Initiate a dictionary for easier counting of elements.
        element_dictionary = {}
        if not self.storage:
            output += "\n Empty."
        else:
            # If the storage is not empty loop its elements in alphabetical order (by name) and store the
            # amount of elements with the same name in dictionary.
            for item in sorted(self.storage, key=lambda element: element.name):
                if item.name not in element_dictionary:
                    element_dictionary[item.name] = 1
                else:
                    element_dictionary[item.name] += 1
            # Loop through the dictionary and create output string.
            for key, value in element_dictionary.items():
                output += f"\n * {key} x {value}"
        return output


class AlchemicalRecipes:
    """AlchemicalRecipes class."""

    def __init__(self):
        """
        Initialize the AlchemicalRecipes class.

        'AlchemicalRecipes' has a recipe's dictionary.
        """
        # Initially recipes dictionary is empty.
        self.recipes = {}

    def add_recipe(self, first_component_name: str, second_component_name: str, product_name: str):
        """
        Determine if recipe is valid and then add it to recipes.

        A recipe consists of three strings, two components and their product.
        If any of the parameters are the same, raise the 'DuplicateRecipeNamesException' exception.
        If there already exists a recipe for the given pair of components, raise the 'RecipeOverlapException' exception.

        :param first_component_name: The name of the first component element.
        :param second_component_name: The name of the second component element.
        :param product_name: The name of the product element.
        """
        # If in the set of components are less than 3 items, there must be duplicates and exception will be raised.
        if len({first_component_name, second_component_name, product_name}) < 3:
            raise DuplicateRecipeNamesException()
        # If the set of components already exist, raise exception for recipe overlapping.
        if {first_component_name, second_component_name} in self.recipes.values():
            raise RecipeOverlapException()
        # Otherwise update recipe dictionary.
        self.recipes[product_name] = {first_component_name, second_component_name}

    def get_product_name(self, first_component_name: str, second_component_name: str) -> str or None:
        """
        Return the name of the product for the two components in recipe.

        The order of the first_component_name and second_component_name is interchangeable, so search for combinations
        of (first_component_name, second_component_name) and (second_component_name, first_component_name).

        If there are no combinations for the two components, return None

        Example:
            recipes = AlchemicalRecipes()
            recipes.add_recipe('Water', 'Wind', 'Ice')
            recipes.get_product_name('Water', 'Wind')  # ->  'Ice'
            recipes.get_product_name('Wind', 'Water')  # ->  'Ice'
            recipes.get_product_name('Fire', 'Water')  # ->  None
            recipes.add_recipe('Water', 'Fire', 'Steam')
            recipes.get_product_name('Fire', 'Water')  # ->  'Steam'

        :param first_component_name: The name of the first component element.
        :param second_component_name: The name of the second component element.
        :return: The name of the product element or None.
        """
        # Find the product for given components from recipes dictionary and return it.
        # If the product is not in dictionary, returns None.
        for product, components in self.recipes.items():
            if components == {first_component_name, second_component_name}:
                return product

    def get_component_names(self, product_name: str) -> tuple[str, str] or None:
        """
        Return the names of the components for the product in recipe.

        If the product is in the recipe, returns its components, if not, returns None.

        :param product_name:
        :return: components for the product according to recipe
        """
        if product_name in self.recipes:
            return tuple(self.recipes[product_name])


class DuplicateRecipeNamesException(Exception):
    """Raised when attempting to add a recipe that has same names for components and product."""

    pass


class RecipeOverlapException(Exception):
    """Raised when attempting to add a pair of components that is already used for another existing recipe."""

    pass


class Cauldron(AlchemicalStorage):
    """
    Cauldron class.

    Extends the 'AlchemicalStorage' class.
    """

    def __init__(self, recipes: AlchemicalRecipes):
        """
        Initialize the Cauldron class.

        Use the base constructor and extend it with recipes from AlchemicalRecipes class.
        """
        super().__init__()
        self.recipes = recipes

    def add(self, element: AlchemicalElement):
        """
        Add element to storage and check if it can combine with anything already inside.

        Use the 'recipes' object that was given in the constructor to determine the combinations.

        Example:
            recipes = AlchemicalRecipes()
            recipes.add_recipe('Water', 'Wind', 'Ice')
            cauldron = Cauldron(recipes)
            cauldron.add(AlchemicalElement('Water'))
            cauldron.add(AlchemicalElement('Wind'))
            cauldron.extract() # -> [<AE: Ice>]

        :param element: Input object to add to storage.
        """
        # Although the type checking is already in the base class method add, type needs to be checked here before
        # accessing attributes which may not exist.
        if not isinstance(element, AlchemicalElement):
            raise TypeError
        # Check the storage starting from last added element.
        for item in reversed(self.storage):
            # If the storage item which is currently checked combined with element which is added is
            # already described in recipes then next check whether the storage item or element is a catalyst.
            if self.recipes.get_product_name(item.name, element.name):
                # If both of the items are catalysts and can be used (uses > 0), reduce uses for both of them,
                # add the new element into the storage and
                # add the product of them into the storage also and break the loop.
                if isinstance(element, Catalyst) and element.uses > 0 and isinstance(item, Catalyst) and item.uses > 0:
                    item.uses -= 1
                    element.uses -= 1
                    super().add(element)
                # If only the new element is a catalyst and can be used reduce the usage of it and remove the
                # other item from storage, add the product of them into the storage and break the loop.
                elif isinstance(element, Catalyst) and element.uses > 0 and not isinstance(item, Catalyst):
                    element.uses -= 1
                    super().pop(item.name)
                # If only the item already in storage is a useful catalyst, reduce the usage of it,
                # add the product of it with the new element into the storage and break the loop.
                elif isinstance(item, Catalyst) and item.uses > 0 and not isinstance(element, Catalyst):
                    item.uses -= 1
                # In case one of the items is a useless catalysts, continue looping.
                # If the item in the storage is the useless catalyst, next combination will be checked.
                # It the new element is a useless catalyst, it finally results in adding it into storage.
                elif isinstance(item, Catalyst) or isinstance(element, Catalyst):
                    continue
                # If neither of the items is a catalyst, then remove the storage item from storage and add
                # the product of both of them into storage and break the loop.
                else:
                    # Using super() here in order to specify, this is AlchemicalStorage method pop, not the general list
                    # method pop().
                    # Since the storage list is checked in reverse order the last item with the same name is removed.
                    super().pop(item.name)
                # First get product name using AlchemicalRecipes class method get_product_name.
                # Then create the instance of AlchemicalElement using product name found from recipes.
                # Then add the element into storage using base class AlchemicalStorage method add
                # which also checks the correct type.
                super().add(AlchemicalElement(self.recipes.get_product_name(element.name, item.name)))
                break
        # If the loop was running to the end without break, the element was not found
        # and needs to be added into the storage.
        else:
            super().add(element)


class Catalyst(AlchemicalElement):
    """Catalyst class."""

    def __init__(self, name: str, uses: int):
        """
        Initialize the Catalyst class.

        :param name: The name of the Catalyst.
        :param uses: The number of uses the Catalyst has.
        """
        super().__init__(name)
        self.uses = uses

    def __repr__(self) -> str:
        """
        Representation of the Catalyst class.

        Example:
            catalyst = Catalyst("Philosophers' stone", 3)
            print(catalyst) # -> <C: Philosophers' stone (3)>

        :return: String representation of the Catalyst.
        """
        return f"<C: {self.name} ({self.uses})>"


class Purifier(AlchemicalStorage):
    """
    Purifier class.

    Extends the 'AlchemicalStorage' class.
    """

    def __init__(self, recipes: AlchemicalRecipes):
        """
        Initialize the Purifier class.

        Use the base constructor and extend it with recipes from AlchemicalRecipes class.
        """
        super().__init__()
        self.recipes = recipes

    def add(self, element: AlchemicalElement):
        """
        Add element to storage and check whether it can be split into anything.

        Use the 'recipes' object that was given in the constructor to determine the combinations.

        Example:
            recipes = AlchemicalRecipes()
            recipes.add_recipe('Water', 'Wind', 'Ice')
            purifier = Purifier(recipes)
            purifier.add(AlchemicalElement('Ice'))
            purifier.extract() # -> [<AE: Water>, <AE: Wind>]   or  [<AE: Wind>, <AE: Water>]

        :param element: Input object to add to storage.
        """
        # Although the type checking is already in the base class method add, type needs to be checked here before
        # accessing attributes which may not exist.
        if not isinstance(element, AlchemicalElement):
            raise TypeError
        # Get the components from recipes. If there is no recipe for that element, results in None.
        components = self.recipes.get_component_names(element.name)
        if not components:
            super().add(element)
        # If there is a recipe for the element, create AlchemicalElement instances from its components and
        # add them into storage using base class add method.
        else:
            super().add(AlchemicalElement(components[0]))
            super().add(AlchemicalElement(components[1]))


if __name__ == '__main__':
    print("1st PART: The Alchemist *************************************************")

    element_one = AlchemicalElement('Fire')
    element_two = AlchemicalElement('Water')
    element_three = AlchemicalElement('Water')
    element_four = AlchemicalElement('Wind')
    element_five = AlchemicalElement('Earth')
    storage = AlchemicalStorage()

    print(element_one)  # <AE: Fire>
    print(element_two)  # <AE: Water>

    storage.add(element_one)
    storage.add(element_two)

    print(storage.get_content())
    # Content:
    #  * Fire x 1
    #  * Water x 1

    print(storage.extract())  # [<AE: Fire>, <AE: Water>]
    print(storage.get_content())
    # Content:
    #  Empty

    storage.add(element_one)
    storage.add(element_two)
    storage.add(element_three)

    print(storage.pop('Water') == element_three)  # True
    print(storage.pop('Water') == element_two)  # True
    print(storage.pop('earth'))  # None
    print(storage.pop('fire') == element_one)  # False

    print(storage.extract())  # [<AE: Fire>]
    print(storage.get_content())
    # Content:
    #  Empty

    storage.add(element_one)
    storage.add(element_two)
    storage.add(element_three)
    storage.add(element_four)
    storage.add(element_five)
    storage.add(element_three)

    print(storage.get_content())
    # Content:
    #  * Earth x 1
    #  * Fire x 1
    #  * Water x 3
    #  * Wind x 1
    print(storage.extract())  # [<AE: Fire>, <AE: Water>, <AE: Water>, <AE: Wind>, <AE: Earth>, <AE: Water>]

    print("2nd PART: Empedocles *************************************************")

    recipes = AlchemicalRecipes()
    recipes.add_recipe('Fire', 'Water', 'Steam')
    recipes.add_recipe('Fire', 'Earth', 'Iron')
    recipes.add_recipe('Water', 'Iron', 'Rust')

    print(recipes.get_product_name('Water', 'Fire'))  # -> 'Steam'
    print(recipes.get_product_name('Water', 'Earth'))  # -> 'None'
    print(recipes.get_product_name('Fire', 'Water'))  # -> 'Steam'

    try:
        recipes.add_recipe('Fire', 'Something else', 'Fire')
        print('Did not raise, not working as intended.')

    except DuplicateRecipeNamesException:
        print('Raised DuplicateRecipeNamesException, working as intended!')

    try:
        recipes.add_recipe('Fire', 'Earth', 'Gold')
        print('Did not raise, not working as intended.')

    except RecipeOverlapException:
        print('Raised RecipeOverlapException, working as intended!')

    cauldron = Cauldron(recipes)
    cauldron.add(AlchemicalElement('Earth'))
    cauldron.add(AlchemicalElement('Water'))
    cauldron.add(AlchemicalElement('Fire'))

    print(cauldron.extract())  # -> [<AE: Earth>, <AE: Steam>]

    cauldron.add(AlchemicalElement('Earth'))
    cauldron.add(AlchemicalElement('Earth'))
    cauldron.add(AlchemicalElement('Earth'))
    cauldron.add(AlchemicalElement('Fire'))
    cauldron.add(AlchemicalElement('Fire'))
    cauldron.add(AlchemicalElement('Water'))

    print(cauldron.extract())  # -> [<AE: Earth>, <AE: Iron>, <AE: Rust>]

    print("3rd PART: Philosophers' stone *************************************************")

    philosophers_stone = Catalyst("Philosophers' stone", 2)
    catalyst_b = Catalyst("Catalyst B", 0)

    recipes = AlchemicalRecipes()
    recipes.add_recipe("Philosophers' stone", 'Mercury', 'Gold')
    recipes.add_recipe("Fire", 'Earth', 'Iron')

    cauldron = Cauldron(recipes)
    cauldron.add(philosophers_stone)
    cauldron.add(AlchemicalElement('Mercury'))
    print(cauldron.extract())  # -> [<C: Philosophers' stone (1)>, <AE: Gold>]

    cauldron.add(philosophers_stone)
    cauldron.add(AlchemicalElement('Mercury'))
    print(cauldron.extract())  # -> [<C: Philosophers' stone (0)>, <AE: Gold>]

    cauldron.add(philosophers_stone)
    # cauldron.add(catalyst_b)
    cauldron.add(AlchemicalElement('Mercury'))
    print(cauldron.extract())  # -> [<C: Philosophers' stone (0)>, <AE: Mercury>]

    purifier = Purifier(recipes)
    purifier.add(AlchemicalElement('Iron'))
    print(purifier.extract())  # -> [<AE: Fire>, <AE: Earth>]    or      [<AE: Earth>, <AE: Fire>]
