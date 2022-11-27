"""
EX05 - Regex.

3. Schedule.
This program Creates schedule from the given file.

Available functions:
create_schedule_file(input_filename: str, output_filename: str) -> None;
Creates a textfile with schedule string displayed as table from the given input file.

create_schedule_string(input_string: str) -> str;
Creates schedule string from the given input string. Alternative tot the create_schedule_file function.

find_matches_from_text(input_string: str) -> collections;
Finds times and activities from the given input string according to the pattern.

create_schedule_dictionary(matches: collections) -> dict;
Creates sorted and validated schedule dictionary where keys are times and values are lists of
unique activities for the given time. Uses function format_time.

format_time(schedule: dict) -> dict;
Converts schedule dictionary time string keys from 24-hour format into 12-hour format.

create_schedule(input_string: str) -> str;
Creates a schedule string using find_matches_from_text function and create_schedule_dictionary function.

measure_table_content(schedule_string: str) -> tuple;
Measures the maximum length of time-string and activities in characters in schedule string.

create_table(schedule_string: str) -> str;
Creates a schedule table as a string from schedule data string. Uses measure_table_content function.

"""


import collections
import re


def create_schedule_file(input_filename: str, output_filename: str) -> None:
    """
    Create schedule file from the given input file.

    :param input_filename: file name to read input string from
    :param output_filename: file name to write the output string
    :return:
    """
    # Open the input file, read the contents, save it into variable and close the file.
    with open(input_filename, "r") as some_file:
        contents = some_file.read()
    # Create schedule as a string using the text from input file.
    final_string = create_schedule(contents)
    # Transform the schedule string into schedule table string.
    schedule_table = create_table(final_string)
    # Create an output file, write the schedule table there and close the file.
    with open(output_filename, "w") as some_file:
        some_file.write(schedule_table)


def create_schedule_string(input_string: str) -> str:
    """
    Create schedule string from the given input string.

    This is an alternative to the create_schedule_file function, but without reading input from and writing
    output to a file.
    Creates a schedule string using create_schedule function and create_table function.
    :param input_string: string where from extract schedule data
    :return: schedule table as a string
    """
    final_string = create_schedule(input_string)
    schedule_table = create_table(final_string)
    return schedule_table


def find_matches_from_text(input_string: str) -> collections:
    """
    Find matches from the given input string according to the pattern.

    :param input_string: string to find schedule data from
    :return: collections of match object
    """
    # Time is always preceded by a new line or a space
    # The number of hours can be 2- or 1-digit. In first case the first number is between 0 and 2.
    # The second number or in case 1-digit hours the number is between 0 and 9.
    # Separator between hours and minutes can be any character except a digit.
    # The number of minutes can be 2- or 1-digit. In first case the first number is between 0 and 5.
    # The second number or in case 1-digit minutes the number is between 0 and 9.
    # The time and activity are separated by one or more empty spaces.
    # Activity contains only latin letters and is at least on character long.
    # The word for activity ends when any other character is encountered.
    pattern = r"(?:\s)(((?:[0-2])?(?:[0-9]))[^\d]([0-5]?[0-9])) +([A-Za-z]+)"
    # Find matches.
    matches = re.finditer(pattern, input_string)
    return matches


def create_schedule_dictionary(matches: collections) -> dict:
    """
    Create a schedule dictionary from matches collection.

    Creates a validated and sorted schedule dictionary where keys are times and values are lists of
    unique activities for the given time.
    :param matches: matches collection consisting times and activities
    :return: sorted and validated schedule dictionary
    """
    schedule_dictionary = {}
    # Fill missing numbers in time with zeros for easier sorting.
    # Group 1 the whole time-string
    # Group 2 hours
    # Group 3 minutes
    # Group 4 activities
    for match in matches:
        if len(match.group(2)) == 1:
            formatted_time = f"0{match.group(2)}"
        else:
            formatted_time = f"{match.group(2)}"
        if len(match.group(3)) == 1:
            formatted_time = f"{formatted_time}:0{match.group(3)}"
        else:
            formatted_time = f"{formatted_time}:{match.group(3)}"

        # If the activity for the iven time already exists, do not duplicate, but continue with the cycle.
        if formatted_time in schedule_dictionary:
            if match.group(4).lower() in schedule_dictionary[formatted_time]:
                continue
            # Also, convert activities into lowercase.
            schedule_dictionary[formatted_time].append((match.group(4).lower()))
        else:
            schedule_dictionary[formatted_time] = [match.group(4).lower()]
    # Sort and format dictionary
    # Following commented-out line fires a warning. Thereby using alternative.
    # sorted_dictionary = dict(sorted(schedule_dictionary.items(), key=lambda item: item[0]))
    sorted_dictionary = {key: value for key, value in sorted(schedule_dictionary.items())}
    formatted_dictionary = format_time(sorted_dictionary)
    return formatted_dictionary


def format_time(schedule: dict) -> dict:
    """
    Format schedule dictionary.

    Converts schedule dictionary time string keys from 24-hour format into 12-hour format.
    :param schedule: dictionary consisting time strings as keys and lists of activities as values.
    :return: formatted schedule dictionary
    """
    formatted_dictionary = {}
    # If the time begins with 00, replace it with 12. Also, add AM.
    for key, value in schedule.items():
        if key[0:2] == "00":
            formatted_dictionary.update({f"12{key[2:]} AM": value})
        # All other time strings beginning with zero are AM times.
        elif key[0] == "0":
            formatted_dictionary.update({f"{key[1:]} AM": value})
        # 10 and 11 are still AM.
        elif key[0:2] == "10" or key[0:2] == "11":
            formatted_dictionary.update({f"{key} AM": value})
        # 12 is PM.
        elif key[0:2] == "12":
            formatted_dictionary.update({f"{key} PM": value})
        # All other time strings are needed to convert into 12-hour strings and are PM.
        # Since there are no following conditions, 24 is conveniently excluded. Hence, the time is now validated also.
        elif key[0:2] in ["13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23"]:
            formatted_dictionary.update({f"{str(int(key[0:2]) - 12) + key[2:]} PM": value})
    return formatted_dictionary


def create_schedule(input_string: str) -> str:
    """
    Create schedule string from the given input string.

    Creates a schedule string using find_matches_from_text function and create_schedule_dictionary function.
    :param input_string: string where from extract schedule data
    :return: schedule data string
    """
    final_string = ""
    # Find times and activities using regex.
    matches = find_matches_from_text(input_string)
    # Create a dictionary for schedule.
    schedule_dictionary = create_schedule_dictionary(matches)
    # Create the schedule string from dictionary.
    for time, activities in schedule_dictionary.items():
        # Separate time and activities with a dash.
        final_string += f"{time}-"
        for activity in activities:
            final_string += f"{activity}, "
        # Remove the last comma and space.
        final_string = final_string[:-2]
        final_string += "\n"
    # Remove the last newline.
    final_string = final_string[:-1]
    return final_string


def measure_table_content(schedule_string: str) -> tuple:
    """
    Measure the length of time-string and activities in schedule string.

    Measures the maximum length of time and activities in characters in schedule string.
    :param schedule_string: string containing schedule information where different times are separated by newline
    :return: tuple containing number of characters of time-string and number of characters of activities string
    """
    if schedule_string == "":
        return 0, 0
    time_width = 0
    content_width = 0
    # Separate records.
    rows = schedule_string.split("\n")
    for row in rows:
        # Separate time-string from activities string.
        time_and_activities = row.split("-")
        # Find the maximum length for time and listed activities.
        if len(time_and_activities[0]) > time_width:
            time_width = len(time_and_activities[0])
        if len(time_and_activities[1]) > content_width:
            content_width = len(time_and_activities[1])
    return time_width, content_width


def create_table(schedule_string: str) -> str:
    """
    Create schedule table as a string from schedule string.

    Creates a schedule table as a string from schedule data string.
    :param schedule_string: string containing times and activities for them, records are separated with newline
    :return: string displaying as a schedule table
    """
    # Measure content length.
    content_width = measure_table_content(schedule_string)
    # Split the schedule string into rows.
    content_row = schedule_string.split("\n")
    # In case no entries return empty default table.
    if content_width[1] == 0:
        return (
            "--------------------\n"
            "|  time | entries  |\n"
            "--------------------\n"
            "| No entries found |\n"
            "--------------------"
        )
    else:
        # Dashes and spaces for table heading.
        # If content width is shorter than the word "entries".
        if content_width[1] <= 7:
            # Pipe + space + time column + space + pipe + space + "entries" length + space + pipe.
            dashes = "-" * (1 + 1 + content_width[0] + 1 + 1 + 1 + 7 + 1 + 1)
            spaces_for_heading = " "
        else:
            dashes = "-" * (1 + 1 + content_width[0] + 1 + 1 + 1 + content_width[1] + 1 + 1)
            spaces_for_heading = " " * (content_width[1] - 7 + 1)

        # Create table heading.
        # The length of time is received from content_width, the length of word "time" is 4.
        space_before_time = " " * (content_width[0] - 4 + 1)
        table = "{:}\n".format(dashes)
        table += "|{:}time{:}|{:}entries{:}|\n".format(space_before_time, " ", " ", spaces_for_heading)
        table += "{:}\n".format(dashes)
        # Create table body.
        for item in content_row:
            content_row_item = item.split("-")
            # Calculate the amount of spaces needed to add to the row.
            if content_width[1] <= 7:
                spaces = " " * (7 - len(content_row_item[1]) + 1)
            else:
                spaces = " " * (content_width[1] - len(content_row_item[1]) + 1)
            space_before_time = " " * (content_width[0] - len(content_row_item[0]) + 1)
            table += "|{:}{:}{:}|{:}{:}{:}|\n".format(space_before_time,
                                                      content_row_item[0], " ", " ", content_row_item[1], spaces)
        table += "{:}\n".format(dashes)
    return table


if __name__ == '__main__':
    print(create_schedule_string("wat 11:00 teine tekst 11:0 jah ei 10:00 pikktekst "))
    print(create_schedule_string("wat 11:00 t tekst 11:0 j ei 10:00 p "))
    create_schedule_file("schedule_input.txt", "schedule_output.txt")
    print(create_schedule_string(""))
    print(create_schedule_string("s asdf  15 03 correct asfd"))
    print(create_schedule_string("go 15:03 correct done"))
    print(create_schedule_string("tere tere siin pole uhtegi kellaaega, aga moned numbrid on nagu 12 h."))
