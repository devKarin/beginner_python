"""
EX10 - Hobbies.

This program organises people and their hobbies.

Available classes:
Person; Person class

Functions in Person class:
__init__; Person constructor.
__repr__; Tweet representation. Returns the tweeting user, tweet content, tweet time and retweets as an f-string.
@property full_name(self) -> str; Property decorator which defines full name for person object.

Available functions:
filter_by_hobby(people_list: list, hobby: str) -> list;
    -> Returns list of people who have the given hobby in their list of hobbies.
sort_by_most_hobbies(people_list: list) -> list;
    -> Returns a list of people sorted by amount of hobbies in descending order.
sort_by_least_hobbies(people_list: list) -> list;
    -> Returns a list of people sorted by amount of hobbies in ascending order.
sort_people_and_hobbies(people_list: list) -> list;
    -> Returns a list of people sorted alphabetically by their full name,
     and with their hobbies list sorted alphabetically.

"""


class Person:
    """
    Class for people.

    Every person has
    a first name,
    last name and
    list of hobbies.
    """

    def __init__(self, first_name: str, last_name: str, hobbies: list):
        """
        Person constructor.

        :param first_name: first name of the person
        :param last_name: last name of the person
        :param hobbies: list of hobbies
        """
        self.first_name = first_name
        self.last_name = last_name
        self.hobbies = hobbies

    @property
    def full_name(self) -> str:
        """Get person's full name. Combination of first and last name."""
        return str(self.first_name) + str(self.last_name)

    def __repr__(self) -> str:
        """
        Person representation.

        :return: person's full name
        """
        return self.full_name


def filter_by_hobby(people_list: list, hobby: str) -> list:
    """
    Return list of people who have the given hobby in their list of hobbies.

    :param people_list: input list of people.
    :param hobby: hobby to filter by.
    :return: filtered list of people.
    """
    # If the hobby is in persons hobbies list, add the person in filtered list.
    return list(filter(lambda person: hobby in person.hobbies, people_list))


def sort_by_most_hobbies(people_list: list) -> list:
    """
    Return a list of people sorted by amount of hobbies in descending order.

    Highest amount of hobbies first.
    If they have the same amount of hobbies, then by full name alphabetically.

    :param people_list: list of people to sort.
    :return: sorted list of people.
    """
    # Sort the people list by using built-in function sorted and anonymous lambda function.
    # First sort people by the length of their hobbies list descending and then by full name alphabetically.
    # In order to reverse the numerical sorting condition "-" is used.
    sorted_list = sorted(people_list, key=lambda person: (-len(person.hobbies), person.full_name))
    return sorted_list


def sort_by_least_hobbies(people_list: list) -> list:
    """
    Return a list of people sorted by amount of hobbies in ascending order.

    Least amount of hobbies first.
    If they have the same amount of hobbies, then by full name alphabetically.

    :param people_list: list of people to sort.
    :return: sorted list of people.
    """
    # This is basically the same function as previous except the first sorting condition direction.
    sorted_list = sorted(people_list, key=lambda person: (len(person.hobbies), person.full_name))
    return sorted_list


def sort_people_and_hobbies(people_list: list) -> list:
    """
    Return a list of people sorted alphabetically by their full name and with their hobbies list sorted alphabetically.

    :param people_list: list of people to sort.
    :return: sorted list of people.
    """
    # First sort persons hobbies with built-in function sort which does not have to return anything
    # and then sort by persons full name alphabetically.
    sorted_list = sorted(people_list, key=lambda person: (person.hobbies.sort(), person.full_name))
    return sorted_list


if __name__ == '__main__':
    person1 = Person("Mari", "Kukk", ["dancing", "biking", "programming"])
    person2 = Person("Jeff", "Bezos", ["money", "hair", "late_capitalism", "space", "unions"])
    person3 = Person("Elon", "Musk", ["late_capitalism", "space", "cars"])
    people = [person1, person2, person3]

    print(filter_by_hobby(people, "space"))  # -> [JeffBezos, ElonMusk]

    print(sort_by_most_hobbies(people))  # -> [JeffBezos, ElonMusk, MariKukk]

    print(sort_by_least_hobbies(people))   # -> [ElonMusk, MariKukk, JeffBezos]

    print(sort_people_and_hobbies(people))  # -> [ElonMusk, JeffBezos, MariKukk]
    print(person1.hobbies)  # -> ['biking', 'dancing', 'programming']
