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
Merges information from two files into one CSV file.

read_csv_file_into_list_of_dicts(filename: str) -> list; Reads csv file into list of dictionaries.
write_list_of_dicts_to_csv_file(filename: str, data: list) -> None; Writes list of dicts into csv file.

"""

import csv
from datetime import datetime


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
            final_list.append([name, towns_dictionary[name], date])
        # If the name is not in towns dictionary, there cannot be a town record either.
        else:
            helper_list.append([name, "-", names_dictionary[name]])
    # For the names not present in names_dictionary, but present in towns_dictionary, because they
    # were left unhandled within the pevious loop.
    for name, town in towns_dictionary.items():
        if name not in names_dictionary:
            helper_list.append([name, town, "-"])
    final_list.extend(helper_list)
    # Write the final list into file using predefined function write_csv_file.
    write_csv_file(csv_output_filename, final_list)


def get_value_types(dictionary: dict, value_types: dict) -> dict:
    for key, value in dictionary.items():
        if (value != '-') and (key not in value_types or value_types[key] != 'str'):
            try:
                int(value)
                value_types.update({key: 'int'})
            except ValueError:
                try:
                    datetime.strptime(value, '%d.%m.%Y').date()
                    value_types.update({key: 'datetime.date'})
                except ValueError:
                    value_types.update({key: 'str'})
    return value_types


def read_csv_file_into_list_of_dicts(filename: str, *typed: bool) -> list:
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

    The order of the elements in the list is the same
    as the lines in the file (the first line becomes the first element etc.)

    :param filename: CSV-file to read.
    :return: List of dictionaries where keys are taken from the header.
    """
    list_of_dictionaries = []
    with open(filename, newline='') as csv_file:
        # https://docs.python.org/3/library/csv.html#csv.DictReader
        # class csv.DictReader(f, fieldnames=None, restkey=None, restval=None, dialect='excel', *args, **kwds)
        # Saves the file as a csv.DictReader object
        csv_reader = csv.DictReader(csv_file)
        value_types = {}
        for row in csv_reader:
            if typed:
                value_types = get_value_types(row, value_types)
            list_of_dictionaries.append(row)
        if typed:
            for dictionary in list_of_dictionaries:
                for key, value in dictionary.items():
                    if value == '-':
                        dictionary.update({key: None})
                    elif value_types[key] == 'int':
                        dictionary.update({key: int(value)})
                    elif value_types[key] == 'datetime.date':
                        dictionary.update({key: datetime.strptime(value, '%d.%m.%Y').date()})
    return list_of_dictionaries


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

    The order of the lines in the file is the same
    as the order of elements in the list.

    :param filename: File to write to.
    :param data: List of dictionaries to write to the file.
    :return: None
    """
    fieldnames = []
    # In case there are different keys in the input data dictionaries.
    # In case it is known to have dictionaries with same keys in data, fieldnames = data[0].keys() should be enough.
    for dictionary in data:
        keys = dictionary.keys()
        for key in keys:
            if key not in fieldnames:
                fieldnames.append(key)

    with open(filename, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, restval='')
        if fieldnames:
            writer.writeheader()
        for row in data:
            writer.writerow(row)


def read_csv_file_into_list_of_dicts_using_datatypes(filename: str) -> list:
    """
    Read data from file and cast values into different datatypes.

    If a field contains only numbers, turn this into int.
    If a field contains only dates (in format dd.mm.yyyy), turn this into date.
    Otherwise the datatype is string (default by csv reader).

    Example:
    name,age
    john,11
    mary,14

    Becomes ('age' is int):
    [
      {'name': 'john', 'age': 11},
      {'name': 'mary', 'age': 14}
    ]

    But if all the fields cannot be cast to int, the field is left to string.
    Example:
    name,age
    john,11
    mary,14
    ago,unknown

    Becomes ('age' cannot be cast to int because of "ago"):
    [
      {'name': 'john', 'age': '11'},
      {'name': 'mary', 'age': '14'},
      {'name': 'ago', 'age': 'unknown'}
    ]

    Example:
    name,date
    john,01.01.2020
    mary,07.09.2021

    Becomes:
    [
      {'name': 'john', 'date': datetime.date(2020, 1, 1)},
      {'name': 'mary', 'date': datetime.date(2021, 9, 7)},
    ]

    Example:
    name,date
    john,01.01.2020
    mary,late 2021

    Becomes:
    [
      {'name': 'john', 'date': "01.01.2020"},
      {'name': 'mary', 'date': "late 2021"},
    ]

    Value "-" indicates missing value and should be None in the result
    Example:
    name,date
    john,-
    mary,07.09.2021

    Becomes:
    [
      {'name': 'john', 'date': None},
      {'name': 'mary', 'date': datetime.date(2021, 9, 7)},
    ]

    None value also doesn't affect the data type
    (the column will have the type based on the existing values).

    The order of the elements in the list should be the same
    as the lines in the file.

    For date, strptime can be used:
    https://docs.python.org/3/library/datetime.html#examples-of-usage-date
    """
    list_of_dictionaries = read_csv_file_into_list_of_dicts(filename, True)
    return list_of_dictionaries


if __name__ == '__main__':
    write_lines_to_file("file.txt", ["hello", "world"])
    # file.txt:
    # hello
    # world

    print("read_csv_file", read_csv_file("data.csv"))
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

    print("read_csv_file", read_csv_file("Example.csv"))
    # [
    #   ["name", "age"],
    #   ["john", "12"],
    #   ["mary", "14"]
    # ]

    print("read_csv_file_into_list_of_dicts", read_csv_file_into_list_of_dicts("example2.csv"))
    # [
    #   {"name": "John", "age": "12", "sex": "M"},
    #   {"name": "Mary", "age": "13", "sex": "F"},
    # ]

    print("read_csv_file_into_list_of_dicts", read_csv_file_into_list_of_dicts("example3.csv"))
    # [
    #   {"name": "John", "age": "12", "sex": "M", "town": "tallinn"},
    #   {"name": "Mary", "age": "13", "sex": "F", "town": "london"},
    # ]

    write_list_of_dicts_to_csv_file("output2.csv", [
        {"name": "john", "age": "23"},
        {"name": "mary", "age": "44"}
    ])
    # name,age
    # john,23
    # mary,44

    write_list_of_dicts_to_csv_file("output3.csv", [
        {"name": "john", "age": "12"},
        {"name": "mary", "town": "London"}
    ])
    # name,age,town
    # john,12,
    # mary,,London

    write_list_of_dicts_to_csv_file("output4.csv", [
        {"name": "John"},
        {"name": "Mary", "age": "19", "town": "tallinn"}
    ])
    # name,age,town
    # John,,
    # Mary,19,tallinn

    write_list_of_dicts_to_csv_file("output5.csv", [])
    # ''

    print("read_csv_file_into_list_of_dicts_using_datatypes",
          read_csv_file_into_list_of_dicts_using_datatypes("example.csv"))
    # [
    #   {'name': 'john', 'age': 12},
    #   {'name': 'mary', 'age': 14}
    # ]

    print("read_csv_file_into_list_of_dicts_using_datatypes",
          read_csv_file_into_list_of_dicts_using_datatypes("example4.csv"))
    # [
    #   {'name': 'john', 'age': '11'},
    #   {'name': 'mary', 'age': '14'},
    #   {'name': 'ago', 'age': 'unknown'}
    # ]

    print("read_csv_file_into_list_of_dicts_using_datatypes",
          read_csv_file_into_list_of_dicts_using_datatypes("example5.csv"))
    # [
    #   {'name': 'john', 'date': datetime.date(2020, 1, 1)},
    #   {'name': 'mary', 'date': datetime.date(2021, 9, 7)},
    # ]

    print("read_csv_file_into_list_of_dicts_using_datatypes",
          read_csv_file_into_list_of_dicts_using_datatypes("example6.csv"))
    # [
    #   {'name': 'john', 'date': "01.01.2020"},
    #   {'name': 'mary', 'date': "late 2021"},
    # ]

    print("read_csv_file_into_list_of_dicts_using_datatypes",
          read_csv_file_into_list_of_dicts_using_datatypes("example7.csv"))
    # [
    #   {'name': 'john', 'date': None},
    #   {'name': 'mary', 'date': datetime.date(2021, 9, 7)},
    # ]
