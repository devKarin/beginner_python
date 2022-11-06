"""
EX08.1 - Test hobbies.

This program conducts tests on first 3 functions of EX05 Hobbies:
create_dictionary, sort_dictionary and create_dictionary_with_hobbies.

Available tests:
test__create_dictionary__data_type_result_is_dictionary_input_empty_string()
    -> Tests whether the result is dictionary.
test__create_dictionary__data_type_result_is_dictionary_input_typical_string()
    -> Tests whether the result is dictionary.
test__create_dictionary__data_type_values_no_hobbies()
    -> Tests whether the dictionary values are lists.
test__create_dictionary__data_type_values_one_hobby()
    -> Tests whether the dictionary values are lists.
test__create_dictionary__data_type_values_hobbies_is_list_of_strings()
    -> Tests whether the hobbies are strings in lists.
test__create_dictionary__no_duplicate_hobbies()
    -> Tests whether hobbies for a person occur once in dictionary values.
test__sort_dictionary__data_type_result_empty_dict()
    -> Tests whether the result is dictionary when the input is an empty dictionary.
test__sort_dictionary__data_type_result()
    -> Tests whether the result is dictionary.
test__sort_dictionary__data_type_keys_empty_dict()
    -> Tests whether the keys of the output dictionary are strings.
test__sort_dictionary__data_type_keys_typical_input()
    -> Tests whether the keys of the output dictionary are strings.
test__sort_dictionary__data_type_values_empty_lists()
    -> Tests whether the values of the output dictionary are lists.
test__sort_dictionary__data_type_values()
    -> Tests whether the values of the output dictionary are lists.
test__sort_dictionary__data_type_values_consist_strings()
    -> Tests whether the values of the output dictionary are lists containing strings.
test__sort_dictionary__data_type_values_consist_strings_empty_string()
    -> Tests whether the values of the output dictionary are lists containing strings
test__sort_dictionary__hobbies_sorted_alphabetically()
    -> Tests whether the strings within value list of the output dictionary are sorted alphabetically.
test__sort_dictionary__hobbies_sorted_alphabetically_keys_not_sorted()
    -> Tests whether the strings within value list of the output dictionary are sorted alphabetically,
    but keys of the output dictionary are not sorted.
test__create_dictionary_with_hobbies__data_type_result_empty_string()
    -> Tests whether the result is dictionary.
test__create_dictionary_with_hobbies__data_type_result()
    -> Tests whether the result is dictionary.
test__create_dictionary_with_hobbies__data_type_keys_empty_string()
    -> Tests whether the keys of the output are strings.
test__create_dictionary_with_hobbies__data_type_keys()
    -> Tests whether the keys of the output are strings.
test__create_dictionary_with_hobbies__data_type_keys_empty_hobbies()
    -> Tests whether the keys of the output dictionary are strings.
test__create_dictionary_with_hobbies__data_type_values_empty_names()
    -> Tests whether the output dictionary values are lists of strings.
test__create_dictionary_with_hobbies__data_type_values()
    -> Tests whether the output dictionary values are lists of strings.
test__create_dictionary_with_hobbies__names_sorted_alphabetically()
    -> Tests whether the persons' names within value lists of the output dictionary are sorted alphabetically.

"""


import pytest
import hobbies


sample_data = """Jack:crafting\nPeter:hiking\nWendy:gaming\nMonica:tennis\nChris:origami\nSophie:sport\nMonica:design\nCarmen:sport\nChris:sport\nMonica:skateboarding\nCarmen:cooking\nWendy:photography\nMonica:tennis\nCooper:yoga\nWendy:sport\nCooper:movies\nMonica:theatre\nCooper:yoga\nChris:gaming\nMolly:fishing\nJack:skateboarding\nWendy:fishing\nJack:drawing\nMonica:baking\nSophie:baking\nAlfred:driving\nAlfred:shopping\nAlfred:crafting\nJack:drawing\nCarmen:shopping\nCarmen:driving\nPeter:drawing\nCarmen:shopping\nWendy:fitness\nAlfred:travel\nJack:origami\nSophie:design\nJack:pets\nCarmen:dance\nAlfred:baking\nSophie:sport\nPeter:gaming\nJack:skateboarding\nCooper:football\nAlfred:sport\nCooper:fitness\nChris:yoga\nWendy:football\nMolly:design\nJack:hiking\nMonica:pets\nCarmen:photography\nJack:baking\nPeter:driving\nChris:driving\nCarmen:driving\nPeter:theatre\nMolly:hiking\nWendy:puzzles\nJack:crafting\nPeter:photography\nCarmen:theatre\nSophie:crafting\nCarmen:cooking\nAlfred:gaming\nPeter:theatre\nCooper:hiking\nChris:football\nChris:pets\nJack:football\nMonica:skateboarding\nChris:driving\nCarmen:pets\nCooper:gaming\nChris:hiking\nJack:cooking\nPeter:fishing\nJack:gaming\nPeter:origami\nCarmen:movies\nSophie:driving\nJack:sport\nCarmen:theatre\nWendy:shopping\nCarmen:pets\nWendy:gaming\nSophie:football\nWendy:theatre\nCarmen:football\nMolly:theatre\nPeter:theatre\nMonica:flowers\nMolly:skateboarding\nPeter:driving\nSophie:travel\nMonica:photography\nCooper:cooking\nJack:fitness\nPeter:cooking\nChris:gaming"""


def test__create_dictionary__data_type_result_is_dictionary_input_empty_string():
    """
    Test whether the result is in correct data structure (dictionary).

    Test case:
    input is an empty string
    result is dictionary
    Expected True

    :return:
    """
    result = hobbies.create_dictionary("")
    assert isinstance(result, dict) is True
    assert isinstance(result, set or list or tuple or str) is False


def test__create_dictionary__data_type_result_is_dictionary_input_typical_string():
    """
    Test whether the result is in correct data structure (dictionary).

    Test case:
    input is a string
    result is dictionary
    Expected True

    :return:
    """
    result = hobbies.create_dictionary("""Cooper:cooking\nJack:fitness\nPeter:cooking\nChris:gaming""")
    assert isinstance(result, dict) is True
    assert isinstance(result, set or list or tuple or str) is False


def test__create_dictionary__data_type_values_no_hobbies():
    """
    Test whether the dictionary values are in correct data structure (list).

    Test case:
    input is a string
    persons hobbies are a list in dictionary
    :return:
    """
    # Test empty hobbies
    input_string = """Cooper: \nJack: \nPeter: \nChris: """
    result = hobbies.create_dictionary(input_string)
    assert isinstance(result["Peter"], list) is True
    assert isinstance(result["Peter"], set or dict or tuple or str or int or float) is False
    # Provide feedback
    assert result == {"Cooper": [" "], "Jack": [" "], "Peter": [" "], "Chris": [" "]}


def test__create_dictionary__data_type_values_one_hobby():
    """
    Test whether the dictionary values are in correct data structure (list).

    Test case:
    input is a string
    persons hobbies are a list in dictionary
    :return:
    """
    # Test typical string
    input_string = """Cooper:cooking\nJack:fitness\nPeter:cooking\nChris:gaming"""
    result = hobbies.create_dictionary(input_string)
    assert isinstance(result["Cooper"], list) is True
    assert isinstance(result["Cooper"], set or dict or tuple or str or int or float) is False
    # Provide feedback
    assert result == {"Cooper": ["cooking"], "Jack": ["fitness"], "Peter": ["cooking"], "Chris": ["gaming"]}


def test__create_dictionary__data_type_values_hobbies_is_list_of_strings():
    """
    Test whether the dictionary values are in correct data structure (list of strings).

    Test case:
    input is a string
    persons hobbies are a list of strings in dictionary
    :return:
    """
    # Test string with one hobby per person
    input_string = """Cooper:cooking\nJack:fitness\nPeter:cooking\nChris:gaming"""
    result = hobbies.create_dictionary(input_string)
    assert isinstance(result["Cooper"][0], str) is True
    assert isinstance(result["Cooper"][0], set or dict or tuple or list or int or float) is False
    assert result == {"Cooper": ["cooking"], "Jack": ["fitness"], "Peter": ["cooking"], "Chris": ["gaming"]}
    # Test multiple hobbies per person
    result = hobbies.create_dictionary(sample_data)
    assert isinstance(result["Jack"][2], str) is True
    assert isinstance(result["Jack"][2], set or dict or tuple or list or int or float) is False


def test__create_dictionary__no_duplicate_hobbies():
    """
    Test whether a hobby of a person reflected multiple times in input string
    is represented once in dictionary values list for that person.

    Test case:
    input is a string consisting duplicate hobbies for one person
    dictionary values represent every value once
    :return:
    """
    input_string = """Cooper:cooking\nJack:fitness\nCooper:cooking\nCooper:gaming"""
    result = hobbies.create_dictionary(input_string)
    assert len(result["Cooper"]) == 2


def test__sort_dictionary__data_type_result_empty_dict():
    """
    Test whether the result is in correct data structure (dictionary).

    Test case:
    input is an empty dictionary
    result is a dictionary
    Expected True

    :return:
    """
    input_dictionary = {}
    result = hobbies.sort_dictionary(input_dictionary)
    assert isinstance(result, dict) is True
    assert isinstance(result, set or tuple or list or str or None) is False
    input_dictionary = {"": []}
    result = hobbies.sort_dictionary(input_dictionary)
    assert isinstance(result, dict) is True
    assert isinstance(result, set or tuple or list or str or None) is False


def test__sort_dictionary__data_type_result():
    """
    Test whether the result is in correct data structure (dictionary).

    Test case:
    input is a dictionary
    result is a dictionary
    Expected True

    :return:
    """
    input_dictionary = {"Jack": ["swimming", "hiking"], "Charlie": ["games", "yoga"]}
    result = hobbies.sort_dictionary(input_dictionary)
    assert isinstance(result, dict) is True
    assert isinstance(result, set or tuple or list or None) is False


def test__sort_dictionary__data_type_keys_empty_dict():
    """
    Test whether the keys of the output are in correct data structure (strings).

    Test case:
    input is an empty dictionary
    result is an empty dictionary with the empty string as a key and empty list as a value

    :return:
    """
    input_dictionary = {}
    result = hobbies.sort_dictionary(input_dictionary)
    assert isinstance(list(result.keys())[0], str) is True
    assert result == {"": []}
    input_dictionary = {"": []}
    result = hobbies.sort_dictionary(input_dictionary)
    assert isinstance(list(result.keys())[0], str) is True
    assert result == {"": []}


def test__sort_dictionary__data_type_keys_typical_input():
    """
    Test whether the keys of the output are in correct data structure (strings).

    Test case:
    input is a dictionary
    result is a dictionary with strings as keys

    :return:
    """
    input_dictionary = {"Jack": ["swimming", "hiking"], "Charlie": ["games", "yoga"]}
    result = hobbies.sort_dictionary(input_dictionary)
    assert isinstance(list(result.keys())[0], str) is True
    assert isinstance(list(result.keys())[0], tuple or int or float) is False


def test__sort_dictionary__data_type_values_empty_lists():
    """
    Test whether the values of the output are in correct data structure (lists).

    Test case:
    input is a dictionary with empty lists as a values
    result is a dictionary with lists as values

    :return:
    """
    # Test dictionary with empty lists as values
    input_dictionary = {"Cooper": [" "], "Jack": [" "], "Peter": [" "], "Chris": [" "]}
    result = hobbies.sort_dictionary(input_dictionary)
    assert isinstance(result["Peter"], list) is True
    assert isinstance(result["Peter"], set or dict or tuple or str or int or float) is False


def test__sort_dictionary__data_type_values():
    """
    Test whether the values of the output are in correct data structure (lists).

    Test case:
    input is a typical dictionary with lists as values
    result is a dictionary with lists as values

    :return:
    """
    input_dictionary = {"Jack": ["swimming", "hiking"], "Charlie": ["games", "yoga"]}
    result = hobbies.sort_dictionary(input_dictionary)
    assert isinstance(result["Jack"], list) is True
    assert isinstance(result["Jack"], set or dict or tuple or str or int or float) is False


def test__sort_dictionary__data_type_values_consist_strings():
    """
    Test whether the values of the output are in correct data structure (lists consisting strings).

    Test case:
    input is a dictionary with lists of strings as values
    result is a dictionary with lists consisting strings as values

    :return:
    """
    input_dictionary = {"Jack": ["swimming", "hiking"], "Charlie": ["games", "yoga"]}
    result = hobbies.sort_dictionary(input_dictionary)
    assert isinstance(result["Charlie"][0], str) is True
    assert isinstance(result["Charlie"][0], set or dict or tuple or list or int or float) is False


def test__sort_dictionary__data_type_values_consist_strings_empty_string():
    """
    Test whether the values of the output are in correct data structure (lists consisting strings).

    Test case:
    input is a dictionary with lists of empty strings as values
    result is a dictionary with lists consisting empty strings as values

    :return:
    """
    input_dictionary = {"Cooper": ["", ""], "Charlie": ["games", "yoga"]}
    result = hobbies.sort_dictionary(input_dictionary)
    assert isinstance(result["Cooper"][0], str) is True
    assert isinstance(result["Cooper"][0], set or dict or tuple or list or int or float) is False


def test__sort_dictionary__hobbies_sorted_alphabetically():
    """
    Test whether the value instances within value lists are sorted alphabetically.

    Test case:
    input is a dictionary with values as lists of strings
    value elements within lists are sorted alphabetically

    :return:
    """
    input_dictionary = {"": ["m", "s", "i", "q", "a", "f", "e", "x", "n", "y", "h", "u", "a", "g", "t", "i", "n", "r",
                             "u", "a", "g", "a", "o", "t", "h", "u"]}
    result = hobbies.sort_dictionary(input_dictionary)
    assert result == {"": ['a', 'a', 'a', 'a', 'e', 'f', 'g', 'g', 'h', 'h', 'i', 'i', 'm', 'n', 'n', 'o', 'q', 'r',
                           's', 't', 't', 'u', 'u', 'u', 'x', 'y']}
    input_dictionary = {"": ["v", "o", "s", "a", "t", "j", "l", "c", "h", "u", "w", "b", "p", "k", "r", "e", "g", "i",
                             "f", "n", "y", "x", "z", "m", "q", "d"]}
    result = hobbies.sort_dictionary(input_dictionary)
    assert result == {"": ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
                           "s", "t", "u", "v", "w", "x", "y", "z"]}


def test__sort_dictionary__hobbies_sorted_alphabetically_keys_not_sorted():
    """
    Test whether the value instances within value lists are sorted alphabetically, but keys are left as they are.

    Test case:
    input is a dictionary with values as lists of strings
    value elements within lists are sorted alphabetically
    keys are in order as they were in input dictionary

    :return:
    """
    input_dictionary = {"b": ["d", "a"], "a": ["c", "f"]}
    result = hobbies.sort_dictionary(input_dictionary)
    assert result == {"b": ["a", "d"], "a": ["c", "f"]}


def test__create_dictionary_with_hobbies__data_type_result_empty_string():
    """
    Test whether the result is in correct data structure (dictionary).

    Test case:
    input is an empty string
    result is a dictionary
    Expected True

    :return:
    """
    result = hobbies.create_dictionary_with_hobbies("")
    assert isinstance(result, dict) is True
    assert isinstance(result, set or list or tuple or str or None) is False


def test__create_dictionary_with_hobbies__data_type_result():
    """
    Test whether the result is in correct data structure (dictionary).

    Test case:
    input is a string
    result is a dictionary
    Expected True

    :return:
    """
    result = hobbies.create_dictionary_with_hobbies(sample_data)
    assert isinstance(result, dict) is True
    assert isinstance(result, set or list or tuple or str or None) is False


def test__create_dictionary_with_hobbies__data_type_keys_empty_string():
    """
    Test whether the keys of the output are in correct data structure (strings).

    Test case:
    input is an empty string
    result is an empty dictionary with the empty string as a key and empty list as a value

    :return:
    """
    input_dictionary = ""
    result = hobbies.create_dictionary_with_hobbies(input_dictionary)
    assert isinstance(list(result.keys())[0], str) is True
    assert result == {"": []}


def test__create_dictionary_with_hobbies__data_type_keys():
    """
    Test whether the keys of the output are in correct data structure (strings).

    Test case:
    input is a string
    result is a dictionary with strings as keys

    :return:
    """
    result = hobbies.create_dictionary_with_hobbies(sample_data)
    assert isinstance(list(result.keys())[0], str) is True


def test__create_dictionary_with_hobbies__data_type_keys_empty_hobbies():
    """
    Test whether the keys of the output dictionary are in correct data structure (strings).

    Test case:
    input is a string with persons names without hobbies
    result is a dictionary with the empty string as a key and list of names as a value

    :return:
    """
    input_string = """Cooper:\nJack:\nPeter:\nChris:"""
    result = hobbies.create_dictionary_with_hobbies(input_string)
    assert isinstance(list(result.keys())[0], str) is True
    assert result == {"": ["Chris", "Cooper", "Jack", "Peter"]}


def test__create_dictionary_with_hobbies__data_type_values_empty_names():
    """
    Test whether the dictionary values are in correct data structure (list of strings).

    Test case:
    input is a string with no names and multiple hobbies
    result is a dictionary with hobbies as keys and lists of empty strings as values

    :return:
    """
    input_string = """:cooking\n:fitness\n:cooking\n:gaming"""
    result = hobbies.create_dictionary_with_hobbies(input_string)
    assert isinstance(result["cooking"][0], str) is True
    assert result == {"cooking": [""], "fitness": [""], "gaming": [""]}


def test__create_dictionary_with_hobbies__data_type_values():
    """
    Test whether the dictionary values are in correct data structure (list of strings).

    Test case:
    input is a string with persons and their hobbies
    result is a dictionary with hobbies as keys and lists of person names as values
    Expected True

    :return:
    """
    result = hobbies.create_dictionary_with_hobbies(sample_data)
    assert isinstance(result["gaming"][0], str) is True


def test__create_dictionary_with_hobbies__names_sorted_alphabetically():
    """
    Test whether the value instances within value lists are sorted alphabetically.

    Test case:
    input is a string with persons and their hobbies
    result is a dictionary with hobbies as keys and hobbyists as strings in lists, sorted alphabetically

    :return:
    """
    result = hobbies.create_dictionary_with_hobbies(sample_data)
    assert result == {'crafting': ['Alfred', 'Jack', 'Sophie'], 'skateboarding': ['Jack', 'Molly', 'Monica'], 'drawing': ['Jack', 'Peter'], 'origami': ['Chris', 'Jack', 'Peter'], 'pets': ['Carmen', 'Chris', 'Jack', 'Monica'], 'hiking': ['Chris', 'Cooper', 'Jack', 'Molly', 'Peter'], 'baking': ['Alfred', 'Jack', 'Monica', 'Sophie'], 'football': ['Carmen', 'Chris', 'Cooper', 'Jack', 'Sophie', 'Wendy'], 'cooking': ['Carmen', 'Cooper', 'Jack', 'Peter'], 'gaming': ['Alfred', 'Chris', 'Cooper', 'Jack', 'Peter', 'Wendy'], 'sport': ['Alfred', 'Carmen', 'Chris', 'Jack', 'Sophie', 'Wendy'], 'fitness': ['Cooper', 'Jack', 'Wendy'], 'driving': ['Alfred', 'Carmen', 'Chris', 'Peter', 'Sophie'], 'theatre': ['Carmen', 'Molly', 'Monica', 'Peter', 'Wendy'], 'photography': ['Carmen', 'Monica', 'Peter', 'Wendy'], 'fishing': ['Molly', 'Peter', 'Wendy'], 'puzzles': ['Wendy'], 'shopping': ['Alfred', 'Carmen', 'Wendy'], 'tennis': ['Monica'], 'design': ['Molly', 'Monica', 'Sophie'], 'flowers': ['Monica'], 'yoga': ['Chris', 'Cooper'], 'travel': ['Alfred', 'Sophie'], 'dance': ['Carmen'], 'movies': ['Carmen', 'Cooper']}
