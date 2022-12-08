"""
EX07 - File handling.

This program makes different reading and writing operations with files.

When files to be read are missing, a notification is printed and an empty data structure is returned.
Module uses utf-8 encoding.

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

read_csv_file_into_list_of_dicts_using_datatypes(filename: str | Path) -> list;
Reads data from file and casts values into different datatypes.

add_missing_keys_to_subdict(dictionary: dict, keys_to_be_checked: list, given_value=None) -> dict;
Normalises data structure by adding missing keys present in other sub-dictionaries to sub-dictionaries of a dictionary.

read_people_data(directory: str) -> dict; Reads people data from csv-files of the given directory.
custom_sort_birth(dict_items: dict[int, dict]) -> any; Sorts dictionary items by birthdate.
custom_sort_age(dict_items: dict[int, dict]) -> any; Sorts dictionary items by name.
generate_people_report(person_data_directory: str, report_filename: str) -> None;
Generates report about people data which is read from csv-files of given directory by
using function read_people_data().

"""

import csv
import datetime
from pathlib import Path


def read_file_contents(filename: str) -> str:
    """
    Read file contents into string.

    In this particular case it is safe to assume that the file exists.

    :param filename: File to read.
    :return: File contents as string.
    """
    try:
        with open(filename, "r", encoding="utf-8") as some_file:
            contents = some_file.read()
        return contents
    except FileNotFoundError:
        print("The file was not found. Please check the filename.")
        return ""


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
    try:
        file_lines = []
        with open(filename, "r", encoding="utf-8") as some_file:
            for line in some_file:
                file_lines.append(line.strip())
        return file_lines
    except FileNotFoundError:
        print("The file was not found. Please check the filename.")
        return []


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
    try:
        file_lines = []
        with open(filename, encoding="utf-8") as csv_file:
            # Saves the file as a csv.reader object
            # and separates the lines in file to lists of strings
            # which were separated by the delimiter.
            csv_reader = csv.reader(csv_file, delimiter=",")

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
    except FileNotFoundError:
        print("The file was not found. Please check the filename.")
        return []


def write_contents_to_file(filename: str, contents: str) -> None:
    """
    Write contents to file.

    If the file does not exist, create it.

    :param filename: File to write to.
    :param contents: Content to write to.
    :return: None
    """
    with open(filename, "w", encoding="utf-8") as some_file:
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
    with open(filename, "w", encoding="utf-8") as some_file:
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
    # According to documentation: "If csvfile (here: filename is a file object, it should be opened with newline=""."
    with open(filename, "w", newline="", encoding="utf-8") as csv_file:
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
    final_list = [["name", "town", "date"]]
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
    for name, visit_date in names_dictionary.items():
        # If the name is present in towns dictionary, add it straight into final list
        # in order to append it later to the final list and preserve name appearance order.
        if name in towns_dictionary:
            final_list.append([name, towns_dictionary[name], visit_date])
        # If the name is not in towns dictionary, there cannot be a town record either.
        else:
            helper_list.append([name, "-", names_dictionary[name]])
    # For the names not present in names_dictionary, but present in towns_dictionary, because they
    # were left unhandled within the previous loop.
    for name, town in towns_dictionary.items():
        if name not in names_dictionary:
            helper_list.append([name, town, "-"])
    final_list.extend(helper_list)
    # Write the final list into file using predefined function write_csv_file.
    write_csv_file(csv_output_filename, final_list)


def get_value_types(dictionary: dict, value_types: dict) -> dict:
    """
    Get common value types for dictionary values with the same key.

    Determines, based on value, whether the value type is integer, "datetime.date" or string.
    Values like "None", "-" and " " are ignored and will not change the data type for the rest of the values of a key.
    If there are different value types for the values with the same key,
    the value type is determined as a string.
    If the date format is not dd.mm.yyyy it is considered incorrect and the value is treated as a string,
    (and therefore all date values for the same key are strings).

    :param dictionary: Dictionary with values to be typed.
    :param value_types: Dictionary to update with value types.
    :return: Dictionary updated with value types.
    """
    for key, value in dictionary.items():
        # Check key-value pairs where the value is not missing, "None" or "-"
        if value == "-" or value == "None" or value == "":
            continue
        # If the value contains only digits, it can be cast into integer.
        # Update only if the key already does not have "int" type.
        if value.isdigit() and key not in value_types:
            value_types.update({key: "int"})
        # If the value is integer, but already has different value type it should be updated to string.
        elif value.isdigit() and value_types[key] == "int":
            continue
        elif not value.isdigit():
            try:
                # If the value type can be cast into datetime.date, do it only in case the type has not been
                # determined yet.
                # Otherwise, unless it already has "datetime.date" type,
                # it has different value types and should be string anyway.
                datetime.datetime.strptime(value, "%d.%m.%Y").date()
                if key not in value_types:
                    value_types.update({key: "datetime.date"})
                elif value_types[key] != "datetime.date":
                    value_types.update({key: "str"})
            except ValueError:
                value_types.update({key: "str"})
        else:
            value_types.update({key: "str"})
    return value_types


def read_csv_file_into_list_of_dicts(filename: str | Path, *typed: bool) -> list:
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
    try:
        list_of_dictionaries = []
        with open(filename, newline="", encoding="utf-8") as csv_file:
            # https://docs.python.org/3/library/csv.html#csv.DictReader
            # class csv.DictReader(f, fieldnames=None, restkey=None, restval=None, dialect="excel", *args, **kwds)
            # Saves the file as a csv.DictReader object
            csv_reader = csv.DictReader(csv_file)
            # Dictionary for holding value types is created only in case typed dictionary is expected to be returned.
            # Theoretically it saves memory space. It's not much but it's honest work. :)
            if typed:
                value_types = {}
            for row in csv_reader:
                if typed:
                    # Value types are updated with every row.
                    value_types = get_value_types(row, value_types)
                list_of_dictionaries.append(row)
            # In case typed dictionary is expected, apply types and replace "-", "" and "None" with None.
            if typed:
                for dictionary in list_of_dictionaries:
                    for key, value in dictionary.items():
                        if value == "-" or value == "None" or value == "":
                            dictionary.update({key: None})
                        elif value_types[key] == "int":
                            dictionary.update({key: int(value)})
                        elif value_types[key] == "datetime.date":
                            dictionary.update({key: datetime.datetime.strptime(value, "%d.%m.%Y").date()})
        return list_of_dictionaries
    except FileNotFoundError:
        print("The file was not found. Please check the filename or Path.")
        return []


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

    with open(filename, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, restval="")
        if fieldnames:
            writer.writeheader()
        for row in data:
            writer.writerow(row)


def read_csv_file_into_list_of_dicts_using_datatypes(filename: str | Path) -> list:
    """
    Read data from file and cast values into different datatypes.

    If a field contains only numbers, turn this into int.
    If a field contains only dates (in format dd.mm.yyyy), turn this into date.
    Otherwise, the datatype is string (default by csv reader).

    Example:
    name,age
    john,11
    mary,14

    Becomes ("age" is int):
    [
      {"name": "john", "age": 11},
      {"name": "mary", "age": 14}
    ]

    But if all the fields cannot be cast to int, the field is left to string.
    Example:
    name,age
    john,11
    mary,14
    ago,unknown

    Becomes ("age" cannot be cast to int because of "ago"):
    [
      {"name": "john", "age": "11"},
      {"name": "mary", "age": "14"},
      {"name": "ago", "age": "unknown"}
    ]

    Example:
    name,date
    john,01.01.2020
    mary,07.09.2021

    Becomes:
    [
      {"name": "john", "date": datetime.date(2020, 1, 1)},
      {"name": "mary", "date": datetime.date(2021, 9, 7)},
    ]

    Example:
    name,date
    john,01.01.2020
    mary,late 2021

    Becomes:
    [
      {"name": "john", "date": "01.01.2020"},
      {"name": "mary", "date": "late 2021"},
    ]

    Value "-" indicates missing value and should be None in the result
    Example:
    name,date
    john,-
    mary,07.09.2021

    Becomes:
    [
      {"name": "john", "date": None},
      {"name": "mary", "date": datetime.date(2021, 9, 7)},
    ]

    None value also doesn't affect the data type
    (the column will have the type based on the existing values).

    The order of the elements in the list should be the same
    as the lines in the file.

    For date, strptime can be used:
    https://docs.python.org/3/library/datetime.html#examples-of-usage-date
    """
    # For the typed version of the dictionary, second optional argument indicating typed option must be True.
    return read_csv_file_into_list_of_dicts(filename, True)


def add_missing_keys_to_subdict(dictionary: dict, keys_to_be_checked: list, given_value=None) -> dict:
    """
    Add missing keys to the sub-dictionary of a dictionary.

    Helps to normalise data structure by adding missing keys to its sub-dictionaries.

    :param dictionary: Dictionary, which sub-dictionary is needed to be supplemented.
    :param keys_to_be_checked: List of keys to be checked in dictionary. Can be a list of all the keys available.
    :param given_value: Value to give to the added key. Defaults to None.
    :return: Dictionary with supplemented keys.
    """
    for value in dictionary.values():
        for key in keys_to_be_checked:
            if key not in value:
                value[key] = given_value
    return dictionary


def read_people_data(directory: str) -> dict:
    """
    Read people data from files.

    Files are inside directory. Read all *.csv files.
    Each file has an int field "id" which should be used to merge information.

    The result should be one dict where the key is id (int) and value is
    a dict of all the different values across the files.
    Missing keys should be in every dictionary.
    Missing value is represented as None.

    File: a.csv
    id,name
    1,john
    2,mary
    3,john

    File: births.csv
    id,birth
    1,01.01.2001
    2,05.06.1990

    File: deaths.csv
    id,death
    2,01.02.2020
    1,-

    Becomes:
    {
        1: {"id": 1, "name": "john", "birth": datetime.date(2001, 1, 1), "death": None},
        2: {"id": 2, "name": "mary", "birth": datetime.date(1990, 6, 5),
            "death": datetime.date(2020, 2, 1)},
        3: {"id": 3, "name": "john", "birth": None, "death": None},
    }

    :param directory: Directory where the csv files are.
    :return: Dictionary with id as keys and data dictionaries as values.
    """
    # Yield csv-files in given directory. Returns a generator.
    files_in_directory = Path(directory).glob("*.csv")
    final_dictionary = {}
    all_keys = []
    # Loop through csv-files.
    for file in files_in_directory:
        # Create a list of dictionaries from file data.
        list_from_file = read_csv_file_into_list_of_dicts_using_datatypes(file)
        for dictionary in list_from_file:
            if dictionary["id"] not in final_dictionary:
                final_dictionary.update({dictionary["id"]: dictionary})
            else:
                final_dictionary[dictionary["id"]] = {**final_dictionary[dictionary["id"]], **dictionary}
    # Collect all keys.
    # Although it means looping the dictionary the second time, it is faster than
    # collecting keys while creating the final dictionary.
    for value in final_dictionary.values():
        all_keys.extend(list(value.keys()))
    # Not removing duplicates in order to preserve the keys order.
    # Add missing keys with None values to the dictionaries.
    final_dictionary = add_missing_keys_to_subdict(final_dictionary, all_keys, None)
    return final_dictionary


def custom_sort_birth(dict_items: dict[int, dict]) -> any:
    """
    Sort dictionary items by birthdate.

    Items without birthdate are ordered last.

    :param dict_items: Dictionary items to be sorted.
    :return: Value to use to sort items.
    """
    # Missing values are for people yet to be born?
    # At this point I can not remember why decided to order them last (if ascending)
    # but it seemed logical at one point.
    # Compare dates as integers, for that calculate weight from year, month and day.
    value_for_comparison = 0
    if dict_items[1]["birth"] == "-":
        return 999999
    else:
        list_from_date = dict_items[1]["birth"].split(".")
        value_for_comparison += int(list_from_date[2]) * 365 + int(list_from_date[1]) * 30 + int(list_from_date[0])
    return value_for_comparison


def custom_sort_age(dict_items: dict[int, dict]) -> any:
    """
    Sort dictionary items by name.

    If the age cannot be calculated, i.e. the age value is -1, the item is ordered last.

    :param dict_items: Dictionary items to be sorted.
    :return: Value to use to sort items.
    """
    # If the age can not be calculated, order the record last.
    if dict_items[1]["age"] == -1:
        return 99999
    else:
        return dict_items[1]["age"]


def generate_people_report(person_data_directory: str, report_filename: str) -> None:
    """
    Generate report about people data.

    Data is read from csv-files of given directory by using read_people_data().

    The input files contain fields "birth" and "death" which are dates.
    Those can be in different files.
    It is expected that there are no duplicate headers in the files (except for the "id").

    The report is a CSV file where all the fields are written to (along with the headers).
    Additionally, two fields are added:
    - "status" this is either "dead" or "alive" depending on whether there is a death date
    - "age" - current age or the age when dying.
    The age is calculated as full years.
    Birth 01.01.1940, death 01.01.2020 - age: 80
    Birth 02.01.1940, death 01.01.2020 - age: 79

    If there is no birthdate, then the age is -1.

    When calculating age, dates can be compared.

    The lines in the output file are ordered as follows:
    - first by the age ascending (younger before older);
      if the age cannot be calculated, then those lines will come last
    - if the age is the same, then those lines are ordered by birthdate descending (newer birth before older birth)
    - if both the age and birthdate are the same,
      then by name ascending (a before b).
      If name is not available, "" is used
      (people with missing name are ordered before people with name)
    - if the names are the same or name field is missing,
      records are ordered by id ascending.

    Dates in the report are in the format: dd.mm.yyyy
    (2-digit day, 2-digit month, 4-digit year).

    :param person_data_directory: Directory of input data.
    :param report_filename: Output file.
    :return: None
    """
    dictionary_to_write = read_people_data(person_data_directory)
    # Initate a variable to collect keys for later conditionals.
    allkeys = []
    # Add status and age keys.
    for sub_dict in dictionary_to_write.values():
        # Collect keys.
        allkeys = sub_dict.keys()
        # As per assignment description "birth" key is available, "age" key will be created here.
        if sub_dict["birth"] is None:
            sub_dict["age"] = -1
        # As per assignment description "death" key is available.
        elif sub_dict["death"] is not None:
            # Calculate difference in years.
            delta_year = sub_dict["death"].year - sub_dict["birth"].year
            # If person died before birthday, subtract 1 year to from age.
            # Compare date difference by replacing the year.
            if sub_dict["death"] < sub_dict["birth"].replace(year=sub_dict["death"].year):
                delta_year -= 1
            # Assign the year difference to the age key.
            sub_dict["age"] = delta_year
        # If the death date is missing, use today's date to calculate age.
        elif sub_dict["death"] is None:
            today = datetime.datetime.today().date()
            delta_year = today.year - sub_dict["birth"].year
            # If persons birthday is yet to come, subtract 1 year from age.
            if today < sub_dict["birth"].replace(year=today.year):
                delta_year -= 1
            sub_dict["age"] = delta_year
        # If the person is dead, create status "dead" and convert death date into date string.
        if sub_dict["death"] is not None:
            sub_dict["status"] = "dead"
            sub_dict["death"] = datetime.datetime.strftime(sub_dict["death"], "%d.%m.%Y")
        # If the person is alive, create status "alive".
        else:
            sub_dict["status"] = "alive"
        # If there is a birthdate, convert it into date string.
        if sub_dict["birth"] is not None:
            sub_dict["birth"] = datetime.datetime.strftime(sub_dict["birth"], "%d.%m.%Y")
        # Replace None values with "-", but for the name field with "" as required in assignment.
        sub_dict.update({key: ("-" if value is None
                               else ("" if key == "name" and value == "-"
                                     else (datetime.datetime.strftime(sub_dict[key], "%d.%m.%Y")
                                           if isinstance(value, datetime.date) and value is not None else value)))
                         for key, value in sub_dict.items()})
    # In order to preserve readability, independent sorting steps are used instead of one complex sorting.
    # In order not to overwrite sort order by sorting in steps, start from the last step.
    dictionary_to_write = \
        {key: value for key, value in sorted(dictionary_to_write.items(), key=lambda item: item[1]["id"])}
    # Name is the only key the assignment that may be missing entirely, because id, birth and death are
    # guaranteed to exist as per description of the assignment and age was created in this function above.
    if "name" in allkeys:
        # For sorting firstly alphabetically, then by length.
        dictionary_to_write = \
            {key: value for key, value in sorted(dictionary_to_write.items(),

                                                 key=lambda item: (item[1]["name"], len(item[1]["name"])))}
    # Order descending by birthdate - newer birth before.
    dictionary_to_write = \
        {key: value for key, value in sorted(dictionary_to_write.items(), key=custom_sort_birth, reverse=True)}
    # Order ascending by age. People without ae are ordered last.
    dictionary_to_write = {key: value for key, value in sorted(dictionary_to_write.items(), key=custom_sort_age)}
    # Write report into file. Argument for that function needs to be list,
    # thereby cast parent dictionary values into list.
    write_list_of_dicts_to_csv_file(report_filename, list(dictionary_to_write.values()))


if __name__ == "__main__":

    print("read_file_contents", read_file_contents("nasty.txt"))

    write_lines_to_file("file.txt", ["hello", "world", "jänes"])
    # file.txt:
    # hello
    # world
    # jänes

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
    # ""

    print("read_csv_file_into_list_of_dicts_using_datatypes",
          read_csv_file_into_list_of_dicts_using_datatypes("example.csv"))
    # [
    #   {"name": "john", "age": 12},
    #   {"name": "mary", "age": 14}
    # ]

    print("read_csv_file_into_list_of_dicts_using_datatypes",
          read_csv_file_into_list_of_dicts_using_datatypes("example4.csv"))
    # [
    #   {"name": "john", "age": "11"},
    #   {"name": "mary", "age": "14"},
    #   {"name": "ago", "age": "unknown"}
    # ]

    print("read_csv_file_into_list_of_dicts_using_datatypes",
          read_csv_file_into_list_of_dicts_using_datatypes("example5.csv"))
    # [
    #   {"name": "john", "date": datetime.date(2020, 1, 1)},
    #   {"name": "mary", "date": datetime.date(2021, 9, 7)},
    # ]

    print("read_csv_file_into_list_of_dicts_using_datatypes",
          read_csv_file_into_list_of_dicts_using_datatypes("example6.csv"))
    # [
    #   {"name": "john", "date": "01.01.2020"},
    #   {"name": "mary", "date": "late 2021"},
    # ]

    print("read_csv_file_into_list_of_dicts_using_datatypes",
          read_csv_file_into_list_of_dicts_using_datatypes("example7.csv"))
    # [
    #   {"name": "john", "date": None},
    #   {"name": "mary", "date": datetime.date(2021, 9, 7)},
    # ]

    print("read_csv_file_into_list_of_dicts_using_datatypes",
          read_csv_file_into_list_of_dicts_using_datatypes("example8.csv"))
    # [
    #    {"id": 1, "firstname": "ago", "blind date": datetime.date(2021, 2, 1)},
    #    {"id": 2, "firstname": "mary", "blind date": datetime.date(2020, 6, 5)},
    #    {"id": 3, "firstname": "max", "blind date": None},
    #    {"id": 4, "firstname": None, "blind date": None},
    # ]

    # print(read_people_data("../ex07_files"))
    # Relative path

    # print(read_people_data("C:\\Users\\karin\\PycharmProjects\\iti0102-2022\\EX\\ex07_files"))
    # Absolute path

    print(read_people_data("data"))
    # {
    #    1: {"id": 1, "name": "john", "birth": datetime.date(2001, 1, 1), "death": None},
    #    2: {"id": 2, "name": "mary", "birth": datetime.date(1990, 6, 5),
    #        "death": datetime.date(2020, 2, 1)},
    #    3: {"id": 3, "name": "john", "birth": None, "death": None},
    # }

    print(generate_people_report("data", "output6.csv"))
    print(generate_people_report("person_data", "output7.csv"))
