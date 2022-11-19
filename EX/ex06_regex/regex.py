"""
EX05 - Regex.

1. Regex.
This program makes different operations based on regex.

Available functions:
find_words(text: str) -> list; Returns a list of all the words in the text string.
find_words_with_vowels(text: str) -> list; Returns a list of all words starting with a vowel.
find_sentences(text: str) -> list; Returns a list of all the sentences in the text string.
find_words_from_sentence(sentence: str) -> list;  Returns all the words found in the sentence.
find_words_from_sentences_only(text: str) -> list; Returns all words that are part of sentences.
find_years(text: str) -> list; Returns a list of all the years as integers.
find_phone_numbers(text: str) -> dict; Returns a dictionary of all the telephone numbers found.

"""


import re


def find_words(text: str) -> list:
    """
    Given string text, return all the words in that string.

    A word here is considered to be any combination letters that starts with
    a capital letter and contains of at least one more lowercase letter.
    Note that Estonian õ, ä, ö and ü should also be accepted here.

    Words must be found using regex.

    :param text: given string to find words from
    :return: list of words found in given string
    """
    # Find pattern which starts with single capital letter followed by one or more lowercase letters.
    pattern = r"([A-Z,Õ,Ä,Ö,Ü][a-z,ü,ä,ö,ü]+)"
    # Return a list for all non-overlapping matches found.
    match = re.findall(pattern, text)
    return match


def find_words_with_vowels(text: str) -> list:
    """
    Given string text, return all the words in that string that start with a vowel.

    A word here is considered to be any combination letters that starts with
    a capital letter and contains of at least one more lowercase letter.
    Note that Estonian õ, ä, ö and ü should also be accepted here.

    Words must be found using regex.

    :param text: given string to find words from
    :return: list of words that start with a vowel found in given string
    """
    # Find pattern which starts with a single capital vowel followed by one or more lowercase letters.
    pattern = r"([AEIOUÕÄÖÜ][a-züäöü]+)"
    # Return a list for all non-overlapping matches found.
    match = re.findall(pattern, text)
    return match


def find_sentences(text: str) -> list:
    """
    Given string text, return all sentences in that string.

    A sentence always starts with a capital letter and ends with punctuation (.!?).
    Note that a sentence may also contain all the typical symbols (like commas, colons, numbers, etc.).
    A sentence may also end in multiple punctuation (example: "Wait...").

    Sentences must be found using regex.

    :param text: given string to find sentences from
    :return: list of sentences found in given string
    """
    # In first non-capturing group find pattern which begins with one or more capital letters
    # followed by zero or more letters, numbers or dashes and zero or one whitespace character.
    # In the second non-capturing group find zero or many times pattern where there is
    # zero or more letters, zero or one comma, dash, colon, semicolon or whitespace.
    # In the third non-capturing group find pattern where there is one or more letters
    # and one or more dots, exclamation marks or question marks.
    # In the fourth non-capturing group find zero or more whitespace characters.
    # Bind those non-capturing groups into one capturing group which represents a sentence.
    pattern = r"((?:[A-ZÕÄÖÜ]+[\wõäöü]*\s?)(?:\"?\'?[\wÕÄÖÜõäöü]*\"?\'?\,?\-?\:?\;?\s?)*" \
              r"(?:[\wÕÄÖÜõäöü]+[\.\!\?]+))(?:\s?)"
    # Return a list for all non-overlapping matches found.
    match = re.findall(pattern, text)
    return match


def find_words_from_sentence(sentence: str) -> list:
    """
    Given a sentence, return all words in that sentence.

    Here, a word is considered to be a normal word in a sentence,
    that is separated from other words by a whitespace (or commas, etc.).
    Note that numbers are also considered as words here, but commas, etc. are not
    a part of a word.

    Words must be found using regex.

    :param sentence: given sentence to find words from
    :return: list of words found in given sentence
    """
    final_list = []
    # Find sentences using previous function.
    for item in find_sentences(sentence):
        # Split the sentence at any non-word character.
        # Add all elements from list returned from split method into the final list.
        final_list.extend(re.split(r"\W+", item))
        # Remove the empty string from list, which was added as the reminder of the initial string.
        final_list.remove("")
    return final_list


def find_words_from_sentences_only(text: str) -> list:
    """
    Given string text, return all words in that string that are a part of a sentence in that string.

    A sentence is defined in function find_sentences().
    A word is defined in function find_words_from_sentence().

    :param text: given string to find words from
    :return: list of words found in sentences from given string
    """
    return find_words_from_sentence(text)


def find_years(text: str) -> list:
    """
    Given string text, return a list of all 4-digit numbers (years) in that string.

    Only 4-digit numbers are considered years here.
    If there is a 5-digit number then that is not considered a year,
    nor will it give two years. So you can not split them up.

    Years must be found using regex.

    Hint: use lookbehind and lookahead to check what comes before and after the numbers.

    :param text: given string to find years from
    :return: list of years (integers) found in given string
    """
    final_list = []
    # Find the pattern where four-digit number is not leaded nor followed by a digit.
    # Iterate over iterator of Match object matching to the pattern.
    for number in re.finditer(r"(?<!\d)\d{4}(?!\d)", text):
        # Append the whole match converted into integer to the final list.
        final_list.append(int(number.group()))
    return final_list


def find_phone_numbers(text: str) -> dict:
    """
    Given string text, return a dictionary of all the phone numbers in that text.

    Phone number might be preceded by area code. Area code is a combination of plus sign and three numbers.
    The phone number itself is a combination of 7-8 numbers.
    The phone number might be separated from the area code with a whitespace, but not necessarily.

    The function must return a dictionary where keys are the area codes
    and values are lists of the phone numbers with the corresponding area number.
    If a phone number does not have an area code given, its area code would be empty string,
    so in dictionary it would be like that: {"": ["56332456"]}.

    Phone numbers must be found using regex.

    :param text: given string to find phone numbers from
    :return: dict containing the numbers
    """
    phone_book = {}
    # Find a pattern where the first group can exist one or zero times and consists of
    # plus-sign followed by three numbers and the second group consists 7-8 digits and
    # there is zero to multiple space characters between those two groups.
    # Iterate over iterator of Match object matching to the pattern.
    for phone_number in re.finditer(r"((\+\d{3})? *(\d{7,8}))", text):
        key = phone_number.group(2) or ""
        if key in phone_book:
            phone_book[key].append(phone_number.group(3))
        else:
            phone_book.update({key: [phone_number.group(3)]})
    return phone_book


if __name__ == '__main__':
    print(find_words('KanaMunaPelmeen!!ApelsinÕunMandariinKakaoHernesAhven'))
    # ['Kana', 'Muna', 'Pelmeen', 'Apelsin', 'Õun', 'Mandariin', 'Kakao', 'Hernes', 'Ahven']

    print(find_words_with_vowels('KanaMunaPelmeenApelsinÕunMandariinKakaoHernesAhven'))
    # ['Apelsin', 'Õun', 'Ahven']

    print(find_sentences('See on esimene - lause. See on ä teine lause! see ei ole lause. Aga kas see on? jah, oli.'))
    # ['See on esimene - lause.', 'See on ä teine lause!', 'Aga kas see on?']

    print(find_sentences('ei ole lause. See on!!! See ka...Ja see... See pole'))
    # ['See on!!!', 'See ka...', 'Ja see...']

    print(find_words_from_sentence("Super lause ää, sorry."))
    # ['Super', 'lause', 'ää', 'sorry']

    print(find_words_from_sentence("Täpitähed on: ä, ö, ü, õ."))
    # ['Täpitähed', 'on', 'ä', 'ö', 'ü', 'õ']

    print(find_words_from_sentence("Täpitähed on: Ä, Ö, Ü, Õ."))
    # ['Täpitähed', 'on', 'Ä', 'Ö', 'Ü', 'Õ']

    print(find_words_from_sentence("'Täpitähed' on: 'Ä', 'Ö', 'Ü', Õ, ä, ö, ü, õ."))
    # ['Täpitähed', 'on', 'Ä', 'Ö', 'Ü', 'Õ', 'ä', 'ö', 'ü', 'õ']

    print(find_words_from_sentences_only(
        'See on esimene - ä lause. See, on teine: lause! see ei ole lause. Aga kas see on? jah, oli.'))
    # ['See', 'on', 'esimene', 'ä', 'lause', 'See', 'on', 'teine', 'lause', 'Aga', 'kas', 'see', 'on']

    print(find_years("1998sef672387fh3f87fh83777f777f7777f73wfj893w8938434343"))
    # [1998, 7777]

    print(find_phone_numbers("+372 56887364  +37256887364  +33359835647  56887364 +11 1234567 +327 1 11111111"))
    # {'+372': ['56887364', '56887364'], '+333': ['59835647'], '': ['56887364', '1234567', '11111111']}
