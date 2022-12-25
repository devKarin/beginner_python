"""
EX11.1 - Alchemy

This program organises people and their hobbies.

Available classes:
AlchemicalElement; AlchemicalElement class
AlchemicalStorage; AlchemicalStorage class

Functions in AlchemicalElement class:
__init__; AlchemicalElement constructor. Every element has a name.
__repr__; AlchemicalElement representation. Returns element name as a formatted string.

Functions in AlchemicalStorage class:
__init__; AlchemicalStorage constructor. Storage is initially and empty list.
add(self, element: AlchemicalElement); Adds object with the type of AlchemicalElement into storage.
pop(self, element_name: str) -> AlchemicalElement | None;
    -> Removes and returns previously added element from storage by its name.
extract(self) -> list[AlchemicalElement]; Returns a list of all the elements from storage and empties the storage.
get_content(self) -> str; Returns a string that gives an overview of the contents of the storage.

"""


class AlchemicalElement:
    """
    AlchemicalElement class.

    Every element must have a name.
    """
    def __init__(self, name: str):
        self.name = name

    def __repr__(self) -> str:
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
        try:
            # Check whether the element is a type of AlchemicalElement before adding it into storage.
            # If not, raise a TypeError and return.
            if not isinstance(element, AlchemicalElement):
                raise TypeError()
            self.storage.append(element)
            return element
        except TypeError:
            print("You are trying to add an element which is not a type of AlchemicalElement.")
            return

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
        output = f"Content:\n"
        # Initiate a dictionary for easier counting of elements.
        element_dictionary = {}
        if not self.storage:
            output += " Empty."
        else:
            # If the storage is not empty loop its elements in alphabetical order (by name) and store the
            # amount of elements with the same name in dictionary.
            for item in sorted(self.storage, key=lambda element: element.name):
                # In order to avoid double-counting, only add element into dictionary and count its amount
                # if it has not been done yet.
                if item.name not in element_dictionary:
                    element_dictionary[item.name] = self.storage.count(item)
            # Loop through the dictionary and create output string.
            for key, value in element_dictionary.items():
                output += f" * {key} x {value}\n"
        return output


if __name__ == '__main__':
    element_one = AlchemicalElement('Fire')
    element_two = AlchemicalElement('Water')
    element_three = AlchemicalElement('Water')
    element_four = AlchemicalElement('Wind')
    element_five = AlchemicalElement('Earth')
    storage = AlchemicalStorage()

    print(element_one)  # <AE: Fire>
    print(element_two)  # <AE: Water>

    # storage.add(2)  # -> You are trying to add an element which is not a type of AlchemicalElement.
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
    #  Empty
    print(storage.extract())
