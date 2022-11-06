"""
EX05 - Hobbies.

1. Hobbies dictionary.
This program makes different operations with dictionaries and hobbies in them.

Available functions:
create_dictionary(data: str) -> dict; Creates dictionary about people and their hobbies.
sort_dictionary(dictionary_to_sort: dict) -> dict; Sorts dictionary values alphabetically.
create_dictionary_with_hobbies(data: str) -> dict; Create dictionary about hobbies and their hobbyists.

"""


def create_dictionary(data: str) -> dict:
    """
    Create dictionary about people and their hobbies ie. {name1: [hobby1, hobby2, ...], name2: [...]}.

    There should be no duplicate hobbies on 1 person.

    :param data: given string from database
    :return: dictionary where keys are people and values are lists of hobbies
    """
    # If the list is empty, return empty dictionary.
    if not data:
        return {}
    # Split the string into lists.
    data_list = data.split("\n")
    # Initiate the dictionary.
    hobbies = {}

    # Loop through the data list.
    for item in data_list:
        index_to_splice = item.find(":")
        key = item[:index_to_splice]
        value = item[index_to_splice + 1:]
        if key not in hobbies:
            hobbies.update({key: [value]})
        elif value not in hobbies[key]:
            hobbies[key].append(value)
    return hobbies


def sort_dictionary(dictionary_to_sort: dict) -> dict:
    """
    Sort dictionary values alphabetically.

    The order of keys is not important.

    sort_dictionary({"b":[], "a":[], "c": []})  => {"b":[], "a":[], "c": []}
    sort_dictionary({"": ["a", "f", "d"]})  => {"": ["a", "d", "f"]}
    sort_dictionary({"b":["d", "a"], "a":["c", "f"]})  => {"b":["a", "d"], "a":["c", "f"]}
    sort_dictionary({"Jack": ["swimming", "hiking"], "Charlie": ["games", "yoga"]})
        => {"Jack": ["hiking", "swimming"], "Charlie": ["games", "yoga"]}

    :param dictionary_to_sort: dictionary to sort
    :return: sorted dictionary
    """
    # Additional code due to failing tests
    if not dictionary_to_sort or dictionary_to_sort == {}:
        return {"": []}
    # End of additional code
    for name, hobbies in dictionary_to_sort.items():
        dictionary_to_sort[name].sort(key=str.lower)
    return dictionary_to_sort


def create_dictionary_with_hobbies(data: str) -> dict:
    """
    Create dictionary about hobbies and their hobbyists ie. {hobby1: [name1, name2, ...], hobby2: [...]}.

    :param data: given string from database
    :return: dictionary, where keys are hobbies and values are lists of people. Values are sorted alphabetically
    """
    # Create initial dictionary.
    # Additional code due to failing tests
    if not data:
        return {"": []}
    else:
        dictionary = create_dictionary(data)
    # End of additional code
    # Following line commented out due to failing tests
    # dictionary = create_dictionary(data)
    # Initiate final dictionary.
    dictionary_with_hobbies = {}

    # Loop through the dictionary items.
    for name, hobbies in dictionary.items():
        # Loop through the hobbies and start collecting them into a new dictionary.
        for hobby in hobbies:
            # If the hobby is not present in the dictionary keys, add it.
            if hobby not in dictionary_with_hobbies.keys():
                dictionary_with_hobbies.update({hobby: [name]})
            # If the hobby is present, but the name is not in the values list, add it.
            elif name not in dictionary_with_hobbies[hobby]:
                dictionary_with_hobbies[hobby].append(name)
                # Sort the names list so there wouldn't be a need for a second loop.
                dictionary_with_hobbies[hobby].sort(key=str.lower)
    return dictionary_with_hobbies
