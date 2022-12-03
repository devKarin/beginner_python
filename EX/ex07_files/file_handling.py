"""
EX07 - File handling.

This program makes different reading and writing operations with files.

Available functions:
read_file_contents(filename: str) -> str; Reads file contents into string.
read_file_contents_to_list(filename: str) -> list; Reads file contents into list of lines.
read_csv_file(filename: str) -> list; Reads CSV file into list of rows.
write_contents_to_file(filename: str, contents: str) -> None; Writes contents to file.
write_lines_to_file(filename: str, lines: list) -> None; Writes lines to file.
write_csv_file(filename: str, data: list) -> None; Writes data into CSV file.
merge_dates_and_towns_into_csv(dates_filename: str, towns_filename: str, csv_output_filename: str) -> None;
Merge information from two files into one CSV file.

"""

import csv


def read_file_contents(filename: str) -> str:
    """
    Read file contents into string.

    In this particular case it is safe to assume that the file exists.

    :param filename: File to read.
    :return: File contents as string.
    """
    with open(filename, "r") as some_file:
        contents = some_file.read()
    return contents


def read_file_contents_to_list(filename: str) -> list:
    r"""
    Read file contents into list of lines.

    Assuming that the file exists is safe in this particular case.
    Each line from the file is a separate element.
    The order of the list is the same as in the file.

    List elements do not contain new line (\n).

    :param filename: File to read.
    :return: List of lines.
    """
    file_lines = []
    with open(filename, "r") as some_file:
        for line in some_file:
            file_lines.append(line.strip())
    return file_lines


def read_csv_file(filename: str) -> list:
    """
    Read CSV file into list of rows.

    Each row is also a list of "columns" or fields.

    CSV (Comma-separated values) example:
    name,age
    john,12
    mary,14

    Becomes:
    [
      ["name", "age"],
      ["john", "12"],
      ["mary", "14"]
    ]

    Uses csv module.

    :param filename: File to read.
    :return: List of lists.
    """
    file_lines = []
    with open(filename) as csv_file:
        # Saves the file as a csv.reader object
        # and separates the lines in file to lists of strings
        # which were separated by the delimiter.
        csv_reader = csv.reader(csv_file, delimiter=',')

        # Iterate over rows read from file.
        for row in csv_reader:
            row_as_list = []
            # Iterate over elements in row separated by comma.
            for element in row:
                # Create a list from elements in row.
                row_as_list.append(element)
            # Create a list from rows in file.
            file_lines.append(row_as_list)
    return file_lines


def write_contents_to_file(filename: str, contents: str) -> None:
    """
    Write contents to file.

    If the file does not exist, create it.

    :param filename: File to write to.
    :param contents: Content to write to.
    :return: None
    """
    with open(filename, "w") as some_file:
        some_file.write(contents)


def write_lines_to_file(filename: str, lines: list) -> None:
    """
    Write lines to file.

    Lines is a list of strings, each represents a separate line in the file.

    There is no new line in the end of the file.
    Unless the last element itself ends with the new line.

    :param filename: File to write to.
    :param lines: List of string to write to the file.
    :return: None
    """
    # Note: not appending, but overwriting.
    with open(filename, "w") as some_file:
        # It is easier to concatenate list elements into one string with newline and then write it into file.
        final_string = ""
        for line in lines:
            final_string += line + "\n"
        # Remove last newline. Not using strip here, because it would remove original newlines also.
        final_string = final_string[:-1]
        some_file.write(final_string)


def write_csv_file(filename: str, data: list) -> None:
    """
    Write data into CSV file.

    Data is a list of lists.
    List represents lines.
    Each element (which is list itself) represents columns in a line.

    [["name", "age"], ["john", "11"], ["mary", "15"]]
    Will result in csv file:

    name,age
    john,11
    mary,15

    Uses csv module.

    :param filename: Name of the file.
    :param data: List of lists to write to the file.
    :return: None
    """
    # According to documentation: "If csvfile (here: filename is a file object, it should be opened with newline=''."
    with open(filename, "w", newline='') as csv_file:
        # Create csv writer, where the elements are separated with commas.
        csv_writer = csv.writer(csv_file, delimiter=",")
        # Iterate over list of lists id est write into file row by row.
        for row in data:
            csv_writer.writerow(row)


def merge_dates_and_towns_into_csv(dates_filename: str, towns_filename: str, csv_output_filename: str) -> None:
    """
    Merge information from two files into one CSV file.

    Dates file contains names and dates. Separated by colon.
    john:01.01.2001
    mary:06.03.2016

    In this particular case it is safe to assume that the date does not need to be validated.
    Every line contains name, colon and date.

    Towns file contains names and towns. Separated by colon.
    john:london
    mary:new york

    Every line contains name, colon and town name.
    There are no headers in the input files.

    Those two files should be merged by names.
    The result should be a csv file:

    name,town,date
    john,london,01.01.2001
    mary,new york,06.03.2016

    Applies for the third part:
    If information about a person is missing, it should be "-" in the output file.

    The order of the lines should follow the order in dates input file.
    Names which are missing in dates input file, will follow the order
    in towns input file.
    The order of the fields is: name,town,date

    name,town,date
    john,-,01.01.2001
    mary,new york,-

    Hint: try to reuse csv reading and writing functions.
    When reading csv, delimiter can be specified.

    :param dates_filename: Input file with names and dates.
    :param towns_filename: Input file with names and towns.
    :param csv_output_filename: Output CSV-file with names, towns and dates.
    :return: None
    """
    # Create header.
    final_list = [['name', 'town', 'date']]
    # For collecting the names absent in dates file but present in towns file.
    helper_list = []
    names_dictionary = {}
    towns_dictionary = {}
    # Create names and dates list.
    names_and_dates_list = read_file_contents_to_list(dates_filename)
    # Create names and towns list.
    names_and_towns_list = read_file_contents_to_list(towns_filename)

    # Add names and dates into names dictionary.
    for row in names_and_dates_list:
        name_and_date = row.split(":")
        names_dictionary.update({name_and_date[0]: name_and_date[1] or "-"})

    # Add names and towns into towns dictionary.
    for row in names_and_towns_list:
        name_and_town = row.split(":")
        towns_dictionary.update({name_and_town[0]: name_and_town[1] or "-"})

    # Merge names and towns dictionaries into final list.
    for name, date in names_dictionary.items():
        # If the name is present in towns dictionary, add it straight into final list
        # in order to append it later to the final list and preserve name appearance order.
        if name in towns_dictionary:
            # If the name is not in names dictionary, there cannot be a date either.
            final_list.append([name, towns_dictionary[name], date])
        else:
            helper_list.append([name, "-", names_dictionary[name]])
    final_list.extend(helper_list)
    # Write the final list into file using predefined function write_csv_file.
    write_csv_file(csv_output_filename, final_list)


def read_csv_file_into_list_of_dicts(filename: str) -> list:
    """
    Read csv file into list of dictionaries.

    Header line will be used for dict keys.
    Each line after header line will result in a dict inside the result list.
    Every line contains the same number of fields.

    Example:
    name,age,sex
    John,12,M
    Mary,13,F

    Header line will be used as keys for each content line.
    The result:
    [
      {"name": "John", "age": "12", "sex": "M"},
      {"name": "Mary", "age": "13", "sex": "F"},
    ]

    If there are only header or no rows in the CSV-file,
    the result is an empty list.

    The order of the elements in the list should be the same
    as the lines in the file (the first line becomes the first element etc.)

    :param filename: CSV-file to read.
    :return: List of dictionaries where keys are taken from the header.
    """
    pass


def write_list_of_dicts_to_csv_file(filename: str, data: list) -> None:
    """
    Write list of dicts into csv file.

    Data contains a list of dictionaries.
    Dictionary key represents the field.

    Example data:
    [
      {"name": "john", "age": "23"}
      {"name": "mary", "age": "44"}
    ]
    Will become:
    name,age
    john,23
    mary,44

    The order of fields/headers is not important.
    The order of lines is important (the same as in the list).

    Example:
    [
      {"name": "john", "age": "12"},
      {"name": "mary", "town": "London"}
    ]
    Will become:
    name,age,town
    john,12,
    mary,,London

    Fields which are not present in one line will be empty.

    The order of the lines in the file should be the same
    as the order of elements in the list.

    :param filename: File to write to.
    :param data: List of dictionaries to write to the file.
    :return: None
    """


if __name__ == '__main__':
    write_lines_to_file("file.txt", ["hello", "world"])
    # file.txt:
    # hello
    # world

    print(read_csv_file("data.csv"))
    # [
    #     ["id", "name", "town", "birthday"],
    #     ["1", "ago", "tallinn", "01.01.2021"],
    #     ["2", "mari", "kuressaare", "02.02.2021"],
    # ]

    write_csv_file("output.csv", [
        ["id", "name", "town", "birthday"],
        ["1", "ago", "tallinn", "01.01.2021"],
        ["2", "mari", "kuressaare", "02.02.2021"],
    ])
    # output.csv:
    # id, name, town, birthday
    # 1, ago, tallinn, 01.01.2021
    # 2, mari, kuressaare, 02.02.2021

    merge_dates_and_towns_into_csv("dates.txt", "towns.txt", "dates_and_towns.csv")
    # name,town,date
    # ago,tartu,01.01.2021
    # mati,narva,06.08.2020
    # mari,tallinn,-

    print(read_csv_file("Example.csv"))
    # [
    #   ["name", "age"],
    #   ["john", "12"],
    #   ["mary", "14"]
    # ]
