def create_dictionary(data: str) -> dict:
    """
    Create dictionary about people and their hobbies ie. {name1: [hobby1, hobby2, ...], name2: [...]}.

    There should be no duplicate hobbies on 1 person.

    :param data: given string from database
    :return: dictionary where keys are people and values are lists of hobbies
    """
    dictionary = {}
    for i in data.split("\n"):
        name, hobby = i.split(":")
        if name not in dictionary:
            dictionary[name] = [hobby]
        elif hobby not in dictionary[name]:
            dictionary[name].append(hobby)
    return dictionary


def sort_dictionary(dictionary: dict) -> dict:
    """
    Sort dictionary values alphabetically.

    The order of keys is not important.

    sort_dictionary({"b":[], "a":[], "c": []})  => {"b":[], "a":[], "c": []}
    sort_dictionary({"": ["a", "f", "d"]})  => {"": ["a", "d", "f"]}
    sort_dictionary({"b":["d", "a"], "a":["c", "f"]})  => {"b":["a", "d"], "a":["c", "f"]}
    sort_dictionary({"Jack": ["swimming", "hiking"], "Charlie": ["games", "yoga"]})
        => {"Jack": ["hiking", "swimming"], "Charlie": ["games", "yoga"]}

    :param dictionary: dictionary to sort
    :return: sorted dictionary
    """
    for word in dictionary:
        dictionary[word].sort()
    return dictionary


def create_dictionary_with_hobbies(data: str) -> dict:
    """
    Create dictionary about hobbies and their hobbyists ie. {hobby1: [name1, name2, ...], hobby2: [...]}.

    :param data: given string from database
    :return: dictionary, where keys are hobbies and values are lists of people. Values are sorted alphabetically
    """
    dictionary = create_dictionary(data)
    new_dictionary = {}
    for i in dictionary:
        for j in dictionary[i]:
            if j not in new_dictionary:
                new_dictionary[j] = [i]
            else:
                new_dictionary[j].append(i)
    return sort_dictionary(new_dictionary)

