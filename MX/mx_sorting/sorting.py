"""
MX - Sorting.

This program introduces different sorting techniques.

Available classes:
Person; Person class

Functions in Person class:
__init__; Person constructor.
__repr__; Person representation. Returns the name, age ad height of the person as an f-string.
sort_people_by_name(people: list[Person]) -> list; Sort people by their name in alphabetical order.
sort_people_by_age_name_height(people: list[Person]) -> list; Sort people by their age, name and height.
sort_people_by_popularity_of_name(people: list[Person]) -> list;
    -> Sort people by the popularity of their name from most popular to least popular.

Available functions:
sort_numbers_using_sort(numbers: list[int]); Sort numbers in ascending order, using sort() list method.
sort_numbers_using_sorted(numbers: list[int]) -> list;
    -> Sort numbers in ascending order, using sorted() built-in function.
sort_numbers_reversed(numbers: list[int]) -> list; Sort numbers in descending order, using sorted() built-in function.
sort_tuples_by_length(tuples: list[tuple]) -> list;
    -> Sort tuples by their length in descending order, using sorted() built-in function.

"""


def sort_numbers_using_sort(numbers: list[int]):
    """
    Sort numbers in ascending order, using sort() list method.

    Performs sort() on the input list 'numbers', so that the values within the list are in ascending order
     (smallest to largest).
    NB: This function does not return value.

    :param numbers: List of integers in a random order.
    """
    # Sort the list of numbers by using sort function. Do not return anything!
    numbers.sort()
    # Print the sorted list out.
    print(numbers)


def sort_numbers_using_sorted(numbers: list[int]) -> list:
    """
    Sort numbers in ascending order, using sorted() built-in function.

    Returns a new sorted list with same values as 'numbers', but in ascending order (smallest to largest).
    NB: The input list 'numbers' remains unchanged.

    :param numbers: List of integers in a random order.
    :return: Sorted list of numbers in ascending order.
    """
    # Sort the list of numbers ascending by using built-in sorted function.
    sorted_list = sorted(numbers)
    return sorted_list


def sort_numbers_reversed(numbers: list[int]) -> list:
    """
    Sort numbers in descending order, using sorted() built-in function.

    Returns a new sorted list with same values as 'numbers', but in descending order (largest to smallest).
    NB: The input list 'numbers' remains unchanged.

    :param numbers: List of integers in a random order.
    :return: Sorted list of numbers in descending order.
    """
    # Sort the list of numbers descending by using built-in sorted function.
    sorted_list = sorted(numbers, reverse=True)
    return sorted_list


def sort_tuples_by_length(tuples: list[tuple]) -> list:
    """
    Sort tuples by their length in descending order, using sorted() built-in function.

    Given a list of tuples, returns a new list where the tuples are ordered based on the amount of elements
     within them (largest to smallest).
    NB: The content of each individual tuple does NOT change.

    Example:
      Input:                                               Output:
        [(1, 1), (1, 1, 1)]                         ->      [(1, 1, 1), (1, 1)]
        [(1, 1), (20000,), (10, 1), (4, 2, 1)]      ->      [(4, 2, 1), (1, 1), (10, 1), (20000,)]
        [([], [1, 2, 3]), ("Hello", 1000, 1, -60)]  ->      [("Hello", 1000, 1, -60), ([], [1, 2, 3])]

    :param tuples: List of tuples in a random order.
    :return: Sorted list of tuples in descending order based on their length.
    """
    # Sort the list of tuples by tuple length descending by using built-in sorted function and
    # anonymous lambda function.
    sorted_list = sorted(tuples, key=lambda item: len(item), reverse=True)
    return sorted_list


class Person:
    """
    Person class.

    This class is complete, nothing new was added to it.
    """

    def __init__(self, name: str, age: int, height: float):
        """
        Person constructor.

        :param name: First name of the person.
        :param age: Age of the person.
        :param height: Height of the person.
        """
        self.name = name
        self.age = age
        self.height = height

    def __repr__(self) -> str:
        """
        Person representation.

        You may change or remove this method, it is here purely for your convenience.

        :return: A way to represent the Person object as a str when printing it in a list.
        """
        return f"<name={self.name}, age={self.age}, height={self.height}>"


def sort_people_by_name(people: list[Person]) -> list:
    """
    Sort people by their name in alphabetical order.

    See examples provided in '__main__' of how this function should work.

    :param people: Input list of people (Objects of the Person class).
    :return: Sorted list of people.
    """
    # Sort people list by the name in lowercase using built-in sorted function and anonymous lambda function.
    sorted_list = sorted(people, key=lambda person: person.name.casefold())
    return sorted_list


def sort_people_by_age_name_height(people: list[Person]) -> list:
    """
    Sort people by their age, name and height.

    Sorts people by age, if two people happen to have the same age sorts them by name.
    If even their name is the same, sorts them by height.
    Everything in ascending order.

    See examples provided in '__main__' of how this function should work.

    :param people: Input list of people (Objects of the Person class).
    :return: Sorted list of people.
    """
    # Sort people list first by age, then by name in lowercase and then by height using
    # built-in sorted function and anonymous lambda function.
    sorted_list = sorted(people, key=lambda person: (person.age, person.name.casefold(), person.height))
    return sorted_list


def sort_people_by_popularity_of_name(people: list[Person]) -> list:
    """
    Sort people by the popularity of their name from most popular to least popular.

    The popularity of a name is determined by how many times that name appears in the provided "people" list.
    If a name appears in the list the same number of times as another name, then sort those people by their names
     alphabetically.

    See more examples provided in '__main__' of how this function should work.

    :param people: Input list of people (Objects of the Person class).
    :return: Sorted list of people.
    """
    # Sort the people list using built-in sorted function and anonymous lambda function:
    # first create a list of person names from object list people by using map function,
    # then count the names in that list,
    # then sort the object list people by the name count descending (for this "-" in front of the
    # first sorting condition is used).
    # Then, sort the object list people by person names ascending (alphabetically).
    sorted_list =\
        sorted(people, key=lambda person: (-list(map(lambda person: person.name.lower(),
                                                     people)).count(person.name.lower()), person.name.casefold()))
    return sorted_list


if __name__ == '__main__':
    numbers = [7, 19, 27, 389, 1, 6007, 49, 94, 904, 2, 1001, 1213, 0, 444, 723, 724, 0, 899, 667, 5, 8]
    sort_numbers_using_sort(numbers)
    print(sort_numbers_using_sorted(numbers))
    print(sort_numbers_reversed(numbers))
    print(sort_tuples_by_length([(1, 1), (1, 1, 1)]))  # -> [(1, 1, 1), (1, 1)]
    print(sort_tuples_by_length([(1, 1), (20000,), (10, 1), (4, 2, 1)]))  # -> [(4, 2, 1), (1, 1), (10, 1), (20000,)]
    print(sort_tuples_by_length([([], [1, 2, 3]), ("Hello", 1000, 1, -60)]))
    # -> [("Hello", 1000, 1, -60), ([], [1, 2, 3])]

    ellie = Person("Ellie", 20, 1.74)
    sebastian = Person("Sebastian", 15, 1.7)
    lukas = Person("Lukas", 19, 1.82)
    lukas2 = Person("Lukas", 19, 1.81)
    alex = Person("Alex", 19, 1.8)

    people = [ellie, sebastian, lukas, lukas2, alex]

    print(sort_people_by_name(people))  # -> [alex, ellie, lukas, lukas2, sebastian]
    print(sort_people_by_age_name_height(people))  # -> [sebastian, alex, lukas2, lukas, ellie]
    print(sort_people_by_popularity_of_name(people))  # -> [lukas, lukas2, alex, ellie, sebastian]
