"""
EX05 - Hobbies.

1. Hobbies dictionary.
This program makes different operations with dictionaries and hobbies in them.

Available functions:
create_dictionary(data: str) -> dict; Creates dictionary about people and their hobbies.
sort_dictionary(dictionary_to_sort: dict) -> dict; Sorts dictionary values alphabetically.
create_dictionary_with_hobbies(data: str) -> dict; Create dictionary about hobbies and their hobbyists.
find_people_with_most_hobbies(data: str) -> list; Finds the people who have the most hobbies, sorted alphabetically.
find_least_popular_hobbies(data: str) -> list; Finds the least popular hobbies, sorted alphabetically.

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
    dictionary = create_dictionary(data)
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


def find_people_with_most_hobbies(data: str) -> list:
    """
    Find the people who have the most hobbies.

    :param data: given string from database
    :return: list of people with most hobbies. Sorted alphabetically.
    """
    # Create a dictionary with people and their hobbies.
    people_and_hobbies = create_dictionary(data)
    # Initiate a list for names of people with most hobbies.
    people_with_most_hobbies = []
    # Loop through the dictionary.
    for name, hobbies in people_and_hobbies.items():
        # Count the hobbies.
        people_and_hobbies[name] = len(people_and_hobbies[name])
    # Find the greatest number of hobbies within dictionary values.
    max_element = max(people_and_hobbies.values())
    # Loop through the dictionary and find the people who have the greatest amount of hobbies.
    for name, count in people_and_hobbies.items():
        if count == max_element:
            # Append their names into the final list.
            people_with_most_hobbies.append(name)
    # Finally, sort the list alphabetically.
    people_with_most_hobbies.sort(key=str.lower)
    return people_with_most_hobbies


def find_least_popular_hobbies(data: str) -> list:
    """
    Find the least popular hobbies.

    :param data: given string from database
    :return: list of the least popular hobbies. Sorted alphabetically.
    """
    # Create a dictionary with hobbies and hobbyists.
    people_and_hobbies = create_dictionary_with_hobbies(data)
    # Initiate a list for the least popular hobbies.
    least_popular_hobbies = []
    # Loop through the dictionary.
    for hobby, names in people_and_hobbies.items():
        # Count the names.
        people_and_hobbies[hobby] = len(people_and_hobbies[hobby])
    # Find the minimum number of hobbyists within dictionary values.
    min_element = min(people_and_hobbies.values())
    # Loop through the dictionary and find the hobbies with the least hobbyists.
    for hobby, count in people_and_hobbies.items():
        if count == min_element:
            # Append the hobby into the final list.
            least_popular_hobbies.append(hobby)
    # Finally, sort the list alphabetically.
    least_popular_hobbies.sort(key=str.lower)
    return least_popular_hobbies


if __name__ == '__main__':
    sample_data = """Jack:crafting\nPeter:hiking\nWendy:gaming\nMonica:tennis\nChris:origami\nSophie:sport\nMonica:design\nCarmen:sport\nChris:sport\nMonica:skateboarding\nCarmen:cooking\nWendy:photography\nMonica:tennis\nCooper:yoga\nWendy:sport\nCooper:movies\nMonica:theatre\nCooper:yoga\nChris:gaming\nMolly:fishing\nJack:skateboarding\nWendy:fishing\nJack:drawing\nMonica:baking\nSophie:baking\nAlfred:driving\nAlfred:shopping\nAlfred:crafting\nJack:drawing\nCarmen:shopping\nCarmen:driving\nPeter:drawing\nCarmen:shopping\nWendy:fitness\nAlfred:travel\nJack:origami\nSophie:design\nJack:pets\nCarmen:dance\nAlfred:baking\nSophie:sport\nPeter:gaming\nJack:skateboarding\nCooper:football\nAlfred:sport\nCooper:fitness\nChris:yoga\nWendy:football\nMolly:design\nJack:hiking\nMonica:pets\nCarmen:photography\nJack:baking\nPeter:driving\nChris:driving\nCarmen:driving\nPeter:theatre\nMolly:hiking\nWendy:puzzles\nJack:crafting\nPeter:photography\nCarmen:theatre\nSophie:crafting\nCarmen:cooking\nAlfred:gaming\nPeter:theatre\nCooper:hiking\nChris:football\nChris:pets\nJack:football\nMonica:skateboarding\nChris:driving\nCarmen:pets\nCooper:gaming\nChris:hiking\nJack:cooking\nPeter:fishing\nJack:gaming\nPeter:origami\nCarmen:movies\nSophie:driving\nJack:sport\nCarmen:theatre\nWendy:shopping\nCarmen:pets\nWendy:gaming\nSophie:football\nWendy:theatre\nCarmen:football\nMolly:theatre\nPeter:theatre\nMonica:flowers\nMolly:skateboarding\nPeter:driving\nSophie:travel\nMonica:photography\nCooper:cooking\nJack:fitness\nPeter:cooking\nChris:gaming"""
    dic = create_dictionary(sample_data)
    print("shopping" in dic["Wendy"])  # -> True
    print("fitness" in dic["Sophie"])  # -> False
    print("gaming" in dic["Peter"])  # -> True
    print(create_dictionary(""))  # -> {}
    print(len(dic["Jack"]))  # ->  12
    print(len(dic["Carmen"]))  # -> 10
    print(len(dic["Molly"]))  # -> 5
    print(len(dic["Sophie"]))  # -> 7
    print(sort_dictionary({"b": [], "a": [], "c": []}))  # => {"b": [], "a": [], "c": []}
    print(sort_dictionary({"": ["a", "f", "d"]}))  # => {"": ["a", "d", "f"]}
    print(sort_dictionary({"b": ["d", "a"], "a": ["c", "f"]}))  # => {"b":["a", "d"], "a":["c", "f"]}
    print(sort_dictionary({"Jack": ["swimming", "hiking"], "Charlie": ["games", "yoga"]}))
    # => {"Jack": ["hiking", "swimming"], "Charlie": ["games", "yoga"]}
    print(sort_dictionary({}))  # => {}
    print(create_dictionary_with_hobbies(sample_data))

    print(find_people_with_most_hobbies(sample_data))  # -> ['Jack']

    print("shopping" in dic["Wendy"])  # -> True
    print("fitness" in dic["Sophie"])  # -> False
    print("gaming" in dic["Peter"])  # -> True
    print(find_people_with_most_hobbies(sample_data))  # -> ['Jack']
    print(len(dic["Jack"]))  # ->  12
    print(len(dic["Carmen"]))  # -> 10
    print(len(dic["Molly"]))  # -> 5
    print(len(dic["Sophie"]))  # -> 7
    print(find_least_popular_hobbies(sample_data))  # -> ['dance', 'flowers', 'puzzles', 'tennis']
