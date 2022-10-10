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
sort_names_and_hobbies(data: str) -> tuple; Creates a tuple of sorted names and their hobbies.
find_people_with_hobbies(data: str, hobbies: list) -> set; Finds all different people with certain hobbies.

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


def sort_names_and_hobbies(data: str) -> tuple:
    """
    Create a tuple of sorted names and their hobbies.

    The structure of the tuple is as follows:
    (
        (name1, (hobby1, hobby2)),
        (name2, (hobby1, hobby2)),
         ...
    )

    For each person, there is a tuple, where the first element is the name (string)
    and the second element is an ordered tuple of hobbies (ordered alphabetically).
    All those person-tuples are ordered by the name of the person and are inside a tuple.

    :param data: given string from database
    :return: tuple of persons and their hobbies. Sorted alphabetically.
    """
    # Create a dictionary of people and their hobbies.
    dictionary = create_dictionary(data)
    # Sort the hobbies in dictionary values list.
    dictionary = sort_dictionary(dictionary)
    # Create a list of tuples
    list_of_tuples = []
    # Convert the dictionary into a sorted list.
    for name in sorted(dictionary.keys()):
        # Initiate a list for one person, add name and hobbies as a tuple in it.
        person_and_its_hobbies = [name, tuple(dictionary[name])]
        # Add this list as a tuple in the final list.
        list_of_tuples.append(tuple(person_and_its_hobbies))
    # Convert the whole list into a tuple and return it.
    return tuple(list_of_tuples)


def find_people_with_hobbies(data: str, hobbies: list) -> set:
    r"""
    Find all the different people with certain hobbies.

    It is recommended to use set here.

    Example:
        data="John:running\nMary:running\nJohn:dancing\nJack:dancing\nJack:painting\nSmith:painting"
        hobbies=["running", "dancing"]
    Result:
        {"John", "Mary", "Jack"}
    """
    # Create a dictionary of people and their hobbies.
    dictionary = create_dictionary(data)
    # Initiate a list for people names matching the search result
    people_with_matching_hobbies = []
    # Create a set from hobbies to be searched.
    hobbies_set = set(hobbies)
    for name, hobbies_of_name in dictionary.items():
        hobbies_set_for_name = set(hobbies_of_name)
        if hobbies_set_for_name.intersection(hobbies_set):
            people_with_matching_hobbies.append(name)

    return set(people_with_matching_hobbies)


def find_two_people_with_most_common_hobbies(data: str) -> dict:
    """
    Find a pair of people who have the highest ratio of common to different hobbies.

    Common hobbies are the ones that both people have.
    Different hobbies are the ones that only one person has.

    Example:
    John has:
        running
        walking
    Mary has:
        dancing
        running
    Nora has:
        running
        singing
        dancing

    Pairs and corresponding common and different hobbies; ratio
    John and Mary; common: running; diff: walking, dancing; ratio: 1/2
    John and Nora; common: running; diff: walking, singing, dancing; ratio: 1/3
    Mary and Nora; common: running, dancing; diff: singing; ratio: 2/1

    So the best result is Mary and Nora. It doesn't matter in which order the names are returned.

    If multiple pairs have the same best ratio, it doesn't matter which pair is returned.

    The exception is when multiple pairs share all of their hobbies, in which case the pair with
    the most shared hobbies is returned.

    A pair with only common hobbies is better than any other pair with at least 1 different hobby.

    Example:
    John has:
        running
        walking
    Mary has:
        running
        walking
    Nora has:
        running
    Oprah has:
        running
    Albert has:
        tennis
        basketball
        football
    Xena has:
        tennis
        basketball
        football
        dancing

    John and Mary have 2 common, 0 different. Ratio 2/0
    Nora and Mary (also Nora and John, Oprah and John, Oprah and Mary) have 1 common, 1 different. Ratio 1/1
    Nora and Oprah have 1 common, 0 different. Ratio 1/0
    Albert and Xena have 3 common, 1 different. Ratio 3/1

    In that case the best pair is John and Mary. If the number of different hobbies is 0,
    then this is better than any pair with at least 1 different hobby.
    Out of the pairs with 0 different hobbies, the one with the highest number
    of common hobbies is the best.
    If there are multiple pairs with the highest number of common hobbies,
    any pair (and in any order) is accepted.

    If there are less than 2 people in the input, return None.
    """
    # Create a dictionary with people and their hobbies.
    people_and_hobbies = create_dictionary(data)
    # Initiate a list to collect tuples of names and ratios
    dict_of_ratios = {}
    # Loop through people and their hobbies.
    for name_1, hobby_1 in people_and_hobbies.items():
        # Run the second loop in order to get combinations.
        for name_2, hobby_2 in people_and_hobbies.items():
            # Don't compare a name with itself, but continue to the next iteration.
            if name_1 is name_2:
                continue
            # Convert two peoples hobbies into sets and find the length of the intersection set.
            common_hobbies = len(set(hobby_1).intersection(set(hobby_2)))
            # # Convert two peoples hobbies into sets and find the length of the symmetric difference set.
            different_hobbies = len(set(hobby_1).symmetric_difference(set(hobby_2)))
            # Collect the result into a dictionary, where the key is a tuple of names.
            dict_of_ratios.update({(name_1, name_2): [common_hobbies, different_hobbies]})
    # Sort the dictionary first by common interests descending and then by different interests ascending.
    # Comment out some code - sorting only by common interests.
    # sorted_dict_by_common = sorted(dict_of_ratios.items(), key=lambda element: element[1][0], reverse=True)
    sorted_dict_by_common = sorted(
        dict_of_ratios.items(), key=lambda element: (
            sorted(
                dict_of_ratios.items(), key=lambda item: item[1][0], reverse=True
            ), element[1][1]
        )
    )
    # Return the pair with most common hobbies.
    return sorted_dict_by_common[0][0]


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
    print(sort_names_and_hobbies(sample_data))

    sort_result = sort_names_and_hobbies(sample_data)
    # if the condition after assert is False, error will be thrown
    assert isinstance(sort_result, tuple)
    assert len(sort_result) == 10
    assert sort_result[0][0] == 'Alfred'
    assert len(sort_result[0][1]) == 7
    assert sort_result[-1] == (
        'Wendy', ('fishing', 'fitness', 'football', 'gaming', 'photography', 'puzzles', 'shopping', 'sport', 'theatre')
    )
    # if you see this line below, then everything seems to be ok!
    print("sorting works!")

    sample_data = """Jack:painting\nPeter:painting\nJack:running\nMary:running\nSmith:walking"""
    print(find_people_with_hobbies(sample_data, ["running", "painting"]))
    print(find_people_with_hobbies(
        "John:running\nMary:running\nJohn:dancing\nJack:dancing\nJack:painting\nSmith:painting",
        ["running", "dancing"]
    ))  # {"John", "Mary", "Jack"}

    sample_data = """John:running\nJohn:walking\nMary:dancing\nMary:running\nNora:running\nNora:singing\nNora:dancing"""
    print(find_two_people_with_most_common_hobbies(sample_data))  # ('Mary', 'Nora')
