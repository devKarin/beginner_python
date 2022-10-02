"""
EX04 Lists.

1. Car inventory.
This program creates a list of cars from a given string.

"""


def list_of_cars(all_cars: str) -> list:
    """
    Return list of cars.

    The input string contains of car makes and models, separated by comma.
    Both the make and the model do not contain spaces (both are one word).

    "Audi A4,Skoda Superb,Audi A4" => ["Audi A4", "Skoda Superb", "Audi A4"]

    :param all_cars: string
    :return: list
    """
    # If the empty string is entered, return empty list.
    if not all_cars:
        return []
    # Split the string at comma and turn it into a list.
    cars_list = all_cars.split(",")
    return cars_list


def car_makes(all_cars: str) -> list:
    """
    Return list of unique car makes.

    The order of the elements should be the same as in the input string (first appearance).

    "Audi A4,Skoda Superb,Audi A4" => ["Audi", "Skoda"]

    :param all_cars: string
    :return: list
    """
    # Remove possible redundant spaces from edges of the string.
    all_cars = all_cars.strip()
    # Create the car list containing models and makes.
    list_with_models = list_of_cars(all_cars)
    # It the list is empty, return the empty list.
    # The empty list in Python is considered False.
    if not list_with_models:
        return list_with_models
    # Initiate a list for car makes.
    list_of_makes = []
    # Loop through the car list and find the indices of spaces within its items.
    for make in list_with_models:
        space_index = make.find(" ")
        # Slice the model-make list item at the space and use the part before space (car make).
        # The space index is not included into the slice.
        car_make = make[:space_index]
        # Check whether the make is already in the car_make list and if not, add it.
        if car_make not in list_of_makes:
            list_of_makes.append(car_make)
    # Return the list of car makes.
    return list_of_makes


def car_models(all_cars: str) -> list:
    """
    Return list of unique car models.

    The order of the elements should be the same as in the input string (first appearance).

    "Audi A4,Skoda Superb,Audi A4,Audi A6" => ["A4", "Superb", "A6"]

    :param all_cars: string
    :return: list
    """
    # The following part of the code is largely the same as in the car_makes function.
    all_cars = all_cars.strip()
    list_with_models = list_of_cars(all_cars)
    if not list_with_models:
        return list_with_models
    # Initiate models list.
    models_list = []
    for model in list_with_models:
        space_index = model.find(" ")
        # Slice the model-make list item at the space and use the part after the space (car model).
        # In order to start slicing right after the space, 1 needs to be added to the space index,
        # because the letter at the index, which marks the start of the slice will be included.
        # find() is used instead of split because model can consist of multiple spaces and find()
        # finds only the first one.
        model = model[space_index + 1:]
        if model not in models_list:
            models_list.append(model)
    return models_list


def create_cars_list(all_cars: str) -> list:
    """
    Return a two-dimensional list of car makes and models.

    Returns a list of car makes and models based on comma-separated string as an argument.
    This is a helper function for search_by_make, search_by_model and car_make_and_models functions.

    :param all_cars: string
    :return: list
    """
    # Clean the input.
    all_cars = all_cars.strip()
    # Create cars list.
    car_list_with_models_and_makes = list_of_cars(all_cars)
    # Initiate cars_list.
    cars_list = []
    # Loop through the cars list with makes and models and create a list.
    for item in car_list_with_models_and_makes:
        # Separate car makes into one-element list.
        make = car_makes(item)
        # Separate model into one-element list.
        model = car_models(item)
        # Create a two-dimensional list from car make and model.
        make.append(model)
        # Collect makes and models into one parent list.
        cars_list.append(make)
    return cars_list


def create_car_dictionary(cars_list: list) -> dict:
    """
    Return a list of car makes and models as dictionary.

    Returns the dictionary of car makes and models based on a two-dimensional cars_list as an argument.
    This is a helper function for search_by_model and car_make_and_models functions.

    :param cars_list: list
    :return: dictionary
    """
    # Initiate cars dictionary.
    cars_dictionary = {}
    # Loop through the helper list.
    for item in range(len(cars_list)):
        # If the car make (in case fold) is not present in the car's dictionary, add it there.
        if cars_list[item][0].casefold() not in str(cars_dictionary.keys()).casefold():
            cars_dictionary.update({cars_list[item][0]: cars_list[item][1]})
        # If the car make as a key is present in the dictionary, update only the models list.
        else:
            # Find the right model where the key is case fold equal with the model to be checked.
            for key, value in cars_dictionary.items():
                if cars_list[item][0].casefold() == key.casefold():
                    # Add the model into the models list and update the dictionary.
                    cars_dictionary.update({key: value + cars_list[item][1]})
    # Return the finished dictionary.
    return cars_dictionary


def search_by_make(all_cars: str, search_parameter: str) -> list:
    """
    Return a list of cars based on the comma-separated cars string and a search-string to search for a car make.

    The function searches for cars where the make is the same as the search string, the search is case-insensitive.

    :param all_cars: string
    :param search_parameter: string
    :return: list
    """
    cars = create_cars_list(all_cars)
    # Initiate search result list.
    search_results = []
    # Loop through the cars list and match the search parameter.
    for car in cars:
        if search_parameter.casefold() == car[0].casefold():
            for element in car[1]:
                search_results.append(f"{car[0]} {element}")
    return search_results


def search_by_model(all_cars: str, search_parameter: str) -> list:
    """
    Return a list of cars based on the comma-separated cars string and a search-string to search for a car model.

    The function searches for cars where the search string is one of the car models, the search is case-insensitive.

    :param all_cars: string
    :param search_parameter: string
    :return: list
    """
    # Use helper functions.
    cars_list = create_cars_list(all_cars)
    cars = create_car_dictionary(cars_list)
    # Initiate search result list.
    search_results = []
    # Loop through the cars list and match the search parameter. model is a list of models here.
    for make, model in cars.items():
        # Loop through models. element represents one model in models list for one make.
        for element in model:
            model_partitions = list(element.split(" "))
            # Loop through the strings in model name. part represents one string in the model name.
            for part in model_partitions:
                if search_parameter.casefold() == part.casefold():
                    search_results.append(f"{make} {element}")
    return search_results


def car_make_and_models(all_cars: str) -> list:
    """
    Create a list of structured information about makes and models.

    For each different car make in the input string an element is created in the output list.
    The element itself is a list, where the first position is the name of the make (string),
    the second element is a list of models for the given make (list of strings).

    No duplicate makes or models should be in the output.

    The order of the makes and models should be the same os in the input list (first appearance).

    "Audi A4,Skoda Super,Skoda Octavia,BMW 530,Seat Leon Lux,Skoda Superb,Skoda Superb,BMW x5" =>
    [['Audi', ['A4']], ['Skoda', ['Super', 'Octavia', 'Superb']], ['BMW', ['530', 'x5']], ['Seat', ['Leon Lux']]]

    :param all_cars: string
    :return: list
    """
    # Use helper functions.
    cars_list = create_cars_list(all_cars)
    car_dictionary = create_car_dictionary(cars_list)
    # Initiate a list for the final result.
    car_list_with_make_and_models = []
    # Loop through car makes and model in dictionary.
    for make, models in car_dictionary.items():
        # Initiate a make sublist for every make.
        make_list_with_models_sublist = []
        # Initiate a models sublist for every car make.
        models_list = []
        for model in models:
            # If the model already exists in models list, continue with the next iteration.
            if model in models_list:
                continue
            # If the model is not in the models list yet, add it.
            else:
                models_list.append(model)
        # Combine lists together.
        # Add make into an empty make sublist.
        make_list_with_models_sublist.append(make)
        # Add models list into the make list.
        make_list_with_models_sublist.append(models_list)
        # Add the make-model list into final results list.
        car_list_with_make_and_models.append(make_list_with_models_sublist)
    return car_list_with_make_and_models


def add_cars(car_list: list, all_cars: str) -> list:
    """
    Add cars from the list into the existing car list.

    The first parameter is in the same format as the output of the previous function.
    The second parameter is a string of comma separated cars (as in all the previous functions).
    The task is to add cars from the string into the list.

    Hint: This and car_make_and_models are very similar functions. Try to use one inside another.

    [['Audi', ['A4']], ['Skoda', ['Superb']]]
    and
    "Audi A6,BMW A B C,Audi A4"

    =>

    [['Audi', ['A4', 'A6']], ['Skoda', ['Superb']], ['BMW', ['A B C']]]

    :param car_list: list
    :param all_cars: string
    :return: list
    """
    # Convert the string of additional cars into a list.
    additional_cars_list = car_make_and_models(all_cars)
    # If the cars list is empty, use another function to create it from a string and return it.
    if not car_list:
        return car_make_and_models(all_cars)

    # Loop through every car make in car_list.
    for item in range(len(car_list)):
        # For every car in car_list loop through car makes in the additional_cars_list.
        for element in additional_cars_list:
            # If the car make in car_list is (case fold) equal
            # to the car make in additional_cars_list,
            # start checking the models.
            if car_list[item][0].casefold() == element[0].casefold():
                # Loop through all models for the make in question.
                for model in element[1]:
                    # If the model is not in the list of models for that car make in car_list, add it.
                    if model not in car_list[item][1]:
                        car_list[item][1].append(model)
            # If the car makes which we compare are not (case fold) equal,
            # convert car list into a string and check whether it's located somewhere else
            # and will be considered in another round of that loop.
            # If the make (case fold) can't be found in the list,
            # add it with all it's models into the car_list.
            elif element[0].casefold() not in str(car_list).casefold():
                car_list.append(element)
    return car_list


def number_of_cars(all_cars: str) -> list:
    """
    Create a list of tuples with make quantities.
    The result is a list of tuples.
    Each tuple is in the form: (make_name: str, quantity: int).
    The order of the tuples (makes) is the same as the first appearance in the list.

    :param all_cars: string
    :return: list
    """
    # If the input string is empty, return an empty list.
    if all_cars.strip() == "":
        return []

    # Create a car list with makes (non-unique) and models.
    car_list = create_cars_list(all_cars)
    # Create a case fold copy of the input-string.
    makes = all_cars.casefold()
    # Initiate an empty dictionary
    makes_dictionary = {}
    # Initiate an empty list for the number of cars.
    number_of_makes = []

    # Loop through all makes and count them case fold.
    for car_make in car_list:
        count = makes.count(car_make[0].casefold())
        # No need to check, whether the key already exists - just rewrite the count:
        # for example replace 4 with 4.
        makes_dictionary.update({car_make[0]: count})

    for key, value in makes_dictionary.items():
        number_of_makes.append((key, value))
    return number_of_makes


def car_list_as_string(cars: list) -> str:
    """
    Create a list of cars.

    The input list is in the same format as the result of car_make_and_models function.
    The order of the elements in the string is the same as in the list.
    [['Audi', ['A4']], ['Skoda', ['Superb']]] =>
    "Audi A4,Skoda Superb"

    :param cars: list
    :return: string
    """
    # Initiate an empty string.
    cars_as_string = ""

    # Loop through all car makes in list.
    for make in cars:
        # Loop through models sublist for a car make.
        for model in make[1]:
            # For every model, append a make and model as a string to the cars_as_string.
            cars_as_string += f"{make[0]} {model},"
    # Finally, remove the redundant comma from the right end of the string.
    cars_as_string = cars_as_string.rstrip(",")
    return cars_as_string


if __name__ == '__main__':
    print('List on cars:')
    print(list_of_cars("Audi A4,Skoda Superb,Audi A4"))  # ["Audi A4", "Skoda Superb", "Audi A4"]
    print(list_of_cars("Audi A4 Skoda Superb Audi A4"))  # ["Audi A4 Skoda Superb Audi A4"]
    print(list_of_cars(""))  # []
    print("*****")

    print('Car makes:')
    print(car_makes("Audi A4,Skoda Super,Skoda Octavia,BMW 530,Seat Leon,Skoda Superb,Skoda Superb,BMW x5"))
    # ['Audi', 'Skoda', 'BMW', 'Seat']

    print(car_makes("Mazda 6,Mazda 6,Mazda 6,Mazda 6"))  # ['Mazda']
    print(car_makes(""))  # []
    print("*****")

    print('Car models:')
    print(car_models("Audi A4,Skoda Superb,Audi A4,Audi A6"))  # ["A4", "Superb", "A6"]
    print(car_models(""))  # []
    print("*****")

    print('Search by make:')
    print(search_by_make("Audi A4 2021,Skoda Superb,Seat Leon,Skoda Superb,Audi A4 2022 sept", "Audi"))
    # ['Audi A4 2021', 'Audi A4 2022 sept']

    print(search_by_make("Audi A4", "A4"))  # []
    print(search_by_make("Audi A4,audi A5,AUDI a6 A7", "Audi"))  # ['Audi A4', 'audi A5', 'AUDI a6 A7']
    print(search_by_make("Audi A4,audi A5,AUDI a6 A7", "AUDI"))  # ['Audi A4', 'audi A5', 'AUDI a6 A7']
    print(search_by_make("Audi A4,Skoda Superb,Seat Leon,Audi A4,Seat Leon,Audi A4,Audi A6,Audi A4 2022", "Audi"))
    # ['Audi A4', 'Audi A4', 'Audi A4', 'Audi A6', 'Audi A4 2022']
    print(search_by_make("Audi A4,Skoda Superb,Seat Leon,audi A4,SEAT Leon,AUDI A4,AudI A6,Audi A4 2022", "audi"))
    # ['Audi A4', 'audi A4', 'AUDI A4', 'AudI A6', 'Audi A4 2022']

    print("*****")

    print('Search by model:')
    print(search_by_model("Audi A4,Audi a4 2021,Audi A40", "A4"))  # ["Audi A4", "Audi a4 2021"]
    print(search_by_model("Audi A4,Audi a4 2021,Audi A40", "a4"))  # ["Audi A4", "Audi a4 2021"]
    print(search_by_model("Audi A4 2021,Skoda Superb,Seat Leon,Skoda Superb,Audi A4 2022 sept", "sept"))
    # ['Audi A4 2022 sept']

    print(search_by_model("Audi A4 2021,Skoda Superb,Seat Leon,Skoda Superb,Audi A4 2022 sept", "sep"))  # []
    print(search_by_model("Audi A4 2021,Skoda Superb,Seat Leon,Skoda Superb,Audi A4 2022 sept", "2021"))
    # ['Audi A4 2021']

    print(search_by_model("Audi A4,Audi a4 2021,Audi A40", "A40"))  # ['Audi A40']
    print(search_by_model("Audi A4,Audi a4 2021,Audi A40", "202"))  # []
    print(search_by_model("Audi A4,Audi a4 2021,Audi A40", "a4 2021"))  # []
    print(search_by_model("Audi A4,Audi a4 2021,Audi A40", "a"))  # []
    print(search_by_model("Audi A4,Audi a4 2021,Audi A40", "Audi"))  # []
    print(search_by_model("Audi A4,Audi a4 2021,Audi A40,Audi A4", "a4"))  # ['Audi A4', 'Audi a4 2021', 'Audi A4']
    print(search_by_model("Audi A4 2021,Skoda Superb,Seat Leon,Skoda Superb,Audi A4 2022 sept", "suPerB"))
    # ['Skoda Superb', 'Skoda Superb']

    print(search_by_model("Audi A4,Audi a4 2021,Audi A40", "x l a u 2"))  # []
    print(search_by_model("Audi A4 2021,Skoda Superb,Seat Leon,Skoda Superb,Audi A4 2022 sept", "SUPERB"))
    # ['Skoda Superb', 'Skoda Superb']

    print(search_by_model("Audi A4 2021,Skoda Superb,Seat Leon,Skoda Superb,Audi A4 2022 sept", "Skoda"))
    # []

    print("*****")

    print('Car makes and models:')
    print(car_make_and_models(
        "Audi A4,Skoda Super,Skoda Octavia,BMW 530,Seat Leon Lux,Skoda Superb,Skoda Superb,BMW x5"
    ))
    # [['Audi', ['A4']], ['Skoda', ['Super', 'Octavia', 'Superb']], ['BMW', ['530', 'x5']], ['Seat', ['Leon Lux']]]

    print("*****")

    print("add cars:")
    print(add_cars([['Audi', ['A4']], ['Skoda', ['Superb']]], "Audi A6,BMW A B C,Audi A4"))
    # [['Audi', ['A4', 'A6']], ['Skoda', ['Superb']], ['BMW', ['A B C']]]
    print(add_cars([], "Audi A6,BMW A B C,Audi A4"))
    # [['Audi', ['A6', 'A4]], ['BMW', ['A B C']]]

    print("*****")

    print("Number of cars:")
    print(number_of_cars("Audi A4,Skoda Super,Skoda Octavia,BMW 530,Seat Leon Lux,Skoda Superb,Skoda Superb,BMW x5"))

    print("*****")

    print("Car list as a string:")
    print(car_list_as_string(
        [['Audi', ['A4']], ['Skoda', ['Super', 'Octavia', 'Superb']], ['BMW', ['530', 'x5']], ['Seat', ['Leon Lux']]]
    ))
    # "Audi A4,Skoda Super,Skoda Octavia,Skoda Superb,BMW 530,BMW x5,Seat Leon Lux"
