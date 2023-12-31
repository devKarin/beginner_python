"""KT3 - 05.11.2022 14:00"""


def last_to_first(s: str) -> str:
    """
    Move last symbol to the beginning of the string.

    last_to_first("ab") => "ba"
    last_to_first("") => ""
    last_to_first("hello") => "ohell"
    """
    # If the string is empty, return empty string
    if not s.strip():
        return ""
    # Otherwise return a string where the first letter is the last of the original and
    # the rest of it is a slice from original string without the last letter
    else:
        return s[-1] + s[:-1]


def only_one_pair(numbers: list) -> bool:
    """
    Whether the list only has one pair.

    Function returns True, if the list only has one pair (two elements have the same value).
    In other cases:
     there are no elements with the same value
     there are more than 2 elements with the same value
     there are several pairs
    returns False.

    only_one_pair([1, 2, 3]) => False
    only_one_pair([1]) => False
    only_one_pair([1, 2, 3, 1]) => True
    only_one_pair([1, 2, 1, 3, 1]) => False
    only_one_pair([1, 2, 1, 3, 1, 2]) => False
    """
    # Check whether the unique set of the list is exatly one element shorter
    # (i.e there is exactly one pair)
    return len(numbers) - len(set(numbers)) == 1


def pentabonacci(n: int) -> int:
    """
    Find the total number of odd values in the sequence up to the f(n) [included].

    The sequence is defined like this:
    f(0) = 0
    f(1) = 1
    f(2) = 1
    f(3) = 2
    f(4) = 4
    f(n) = f(n - 1) + f(n - 2) + f(n - 3) + f(n - 4) + f(n - 5)

    Keep in mind that 1 is the only value that is duplicated in the sequence
    and must be counted only once.

    pentabonacci(5) -> 1
    pentabonacci(10) -> 3
    pentabonacci(15) -> 5

    :param n: The last term to take into account.
    :return: Total number of odd values.
    """
    # Initiate the counter
    counter = 0
    element = 0
    # Since there is no need to save all the elements, do not use recursion
    for i in range(n + 1):
        if i == 0:
            element = 0
        elif i == 1:
            element = 1
        elif i == 2:
            element = 2
        else:
            element += (n - i)
        if element % 2 != 0:
            counter += 1
    return counter - 2


def swap_dict_keys_and_value_lists(d: dict) -> dict:
    """
    Swap keys and values in dict.

    Values are lists.
    Every element in this list should be a key,
    and current key will be a value for the new key.
    Values in the result are lists.

    Every list in input dict has at least 1 element.
    The order of the values in the result dict is not important.

    swap_dict_keys_and_value_lists({"a": ["b", "c"]}) => {"b": ["a"], "c": ["a"]}
    swap_dict_keys_and_value_lists({1: [2, 3], 4: [2, 5]}) => {2: [1, 4], 3: [1], 5: [4]}
    swap_dict_keys_and_value_lists({}) => {}
    swap_dict_keys_and_value_lists({1: [2]}) => {2: [1]}
    """
    # Initiate new final dictionary
    reversed_dictionary = {}
    if not d:
        return reversed_dictionary
    # Loop the key-value pairs
    for key, values in d.items():
        # Loop for every value in values list
        for value in values:
            # Set the value to be new key in dict (if it's not already in dictionary) and the key to be value of it
            if value not in reversed_dictionary:
                reversed_dictionary[value] = [key]
            # If the key exists, add new value into the values list
            else:
                reversed_dictionary[value].append(key)
    return reversed_dictionary


if __name__ == '__main__':
    assert last_to_first("ab") == "ba"
    assert last_to_first("") == ""
    assert last_to_first("hello") == "ohell"

    assert only_one_pair([1, 2, 3]) is False
    assert only_one_pair([1]) is False
    assert only_one_pair([1, 2, 3, 1]) is True
    assert only_one_pair([1, 2, 1, 3, 1]) is False
    assert only_one_pair([1, 2, 1, 3, 1, 2]) is False

    assert pentabonacci(5) == 1
    assert pentabonacci(10) == 3
    assert pentabonacci(15) == 5

    assert swap_dict_keys_and_value_lists({"a": ["b", "c"]}) == {"b": ["a"], "c": ["a"]}
    assert swap_dict_keys_and_value_lists({1: [2, 3], 4: [2, 5]}) == {2: [1, 4], 3: [1], 5: [4]}
    # or {2: [4, 1], 3: [1], 5: [4]}

    assert swap_dict_keys_and_value_lists({}) == {}
    assert swap_dict_keys_and_value_lists({1: [2]}) == {2: [1]}

    print(last_to_first("ab"))  # => "ba"
    print(last_to_first(""))  # => ""
    print(last_to_first("hello"))  # => "ohell"

    print(only_one_pair([1, 2, 3]))  # = > False
    print(only_one_pair([1]))  # = > False
    print(only_one_pair([1, 2, 3, 1]))  # = > True
    print(only_one_pair([1, 2, 1, 3, 1]))  # = > False
    print(only_one_pair([1, 2, 1, 3, 1, 2]))  # = > False

    print(swap_dict_keys_and_value_lists({"a": ["b", "c"]}))  # = > {"b": ["a"], "c": ["a"]}
    print(swap_dict_keys_and_value_lists({1: [2, 3], 4: [2, 5]}))  # = > {2: [1, 4], 3: [1], 5: [4]}
    print(swap_dict_keys_and_value_lists({}))  # = > {}
    print(swap_dict_keys_and_value_lists({1: [2]}))  # = > {2: [1]}

    print(pentabonacci(5))  # -> 1
    print(pentabonacci(10))  # -> 3
    print(pentabonacci(15))  # -> 5
