"""
EX02 Math.

4. Caesar cipher.
This program codes and decodes strings using the Caesar cipher.

"""


def encode(message: str, shift: int) -> str:
    """
    Encode a message using a Caesar cipher.

    Presume the message is already lowercase.
    For each letter of the message, shift it forward in the alphabet by shift amount.
    If the character isn't a letter, keep it the same.

    For example, shift = 3 then a => d, b => e, z => c (see explanation below)

    Shift:    0 1 2 3
    Alphabet:       A B C D E F G H I J
    Result:   A B C D E F G H I J

    Examples:
    1. encode('i like turtles', 6) == 'o roqk zaxzrky'
    2. encode('example', 1) == 'fybnqmf'
    3. encode('the quick brown fox jumps over the lazy dog.', 7) == 'aol xbpjr iyvdu mve qbtwz vcly aol shgf kvn.'

    :param message: message to be encoded
    :param shift: shift for encoding
    :return: encoded message
    """
    # Just in case convert the message in arguments into lowercase.
    lowercase_message = message.lower()
    # Initiate a translation dictionary for later use in translation
    translation_dictionary = {}
    # Exclude shifting more than the alphabet length.
    # Modulo shows the "pure" shift
    shift = shift % 26
    """
    English (latin) alphabet lowercase letters numeric value
    starts with 97 (a) and ends with the letter 122 (z).
    Loop it through.
    """
    for letter in range(97, 123):
        """
        Calculate new letter value.
        If the new letter value exceeds alphabets last letter numeric value,
        start from the beginning of the alphabet i.e .
        """
        if (letter + shift) > 122:
            """
            This can be achieved at least two ways.
            Alternative:
            new_letter_index = letter + shift - 122 + 96
            - 1 is for compensation -> because due to the if-block
            the modulo is always greater than 0.
            """
            new_letter_index = (letter + shift) % 122 + 97 - 1
        else:
            new_letter_index = letter + shift
        # Update the dictionary with new key-value pais.
        translation_dictionary.update({letter: new_letter_index})
    # Translate the message using dictionary.
    translation = lowercase_message.translate(translation_dictionary)
    return translation


if __name__ == '__main__':
    print(encode("i like turtles", 6))  # -> o roqk zaxzrky
    print(encode("i like turtles", -20))  # -> o roqk zaxzrky
    print(encode("o roqk zaxzrky", 20))  # -> i like turtles
    print(encode("o roqk zaxzrky", 72))  # -> i like turtles
    print(encode("example", 1))  # -> fybnqmf
    print(encode("don't change", 0))  # -> don't change
    print(encode('the quick brown fox jumps over the lazy dog.', 7))  # -> aol xbpjr iyvdu mve qbtwz vcly aol shgf kvn.
    print(encode('aaa zzz ... ``.', -1))  # -> aaa zzz ... ``.
