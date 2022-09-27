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


def create_car_dictionary(all_cars: str) -> dict:
    """
    Return a list of car makes and models as dictionary.

    Returns the dictionary of car makes and models based on comma-separated string as an argument.
    This is a helper function for search_by_make and search_by_model functions.

    :param all_cars: string
    :return: dictionary
    """
    # Clean the input.
    all_cars = all_cars.strip()
    # Create cars list.
    car_list_with_models_and_makes = list_of_cars(all_cars)
    # Initiate cars dictionary.
    cars = {}
    # Loop through the cars list and make a dictionary of it.
    for item in car_list_with_models_and_makes:
        # Create a key for the dictionary out of one-element car_makes list.
        make = str(car_makes(item)[0])
        # Create a value for the dictionary out of one-element car_models list.
        model = car_models(item)
        # If the key already exists, check, whether the value is also present.
        if make in cars.keys():
            """
            Comment out the removal of duplicated values, because the test doesn't like it.
            
            if model[0] in cars[make]:
                # If the model already exists at car make key in the dictionary, head to the next iteration.
                continue
            # If there is no such model yet, append the content of the one-element model list to the
            # models list at dictionary's key.
            else:
            """
            cars[make].append(model[0])
        # If there is no such key-value pairs as make and model, add it to the dictionary.
        else:
            cars.update({make: model})
    return cars


def search_by_make(all_cars: str, search_parameter: str) -> list:
    """
    Return a list of cars based on the comma-separated cars string and a search-string to search for a car make.

    The function searches for cars where the make is the same as the search string, the search is case-insensitive.

    :param all_cars: string
    :param search_parameter: string
    :return: list
    """
    # Use the helper function.
    cars = create_car_dictionary(all_cars)
    # Initiate search result list.
    search_results = []
    # Loop through the cars list and match the search parameter.
    for car_make, car_model in cars.items():
        if search_parameter.casefold() == car_make.casefold():
            for element in car_model:
                search_results.append(f"{car_make} {element}")
    return search_results


def search_by_model(all_cars: str, search_parameter: str) -> list:
    """
    Return a list of cars based on the comma-separated cars string and a search-string to search for a car model.

    The function searches for cars where the search string is one of the car models, the search is case-insensitive.

    :param all_cars: string
    :param search_parameter: string
    :return: list
    """
    # Use the helper function.
    cars = create_car_dictionary(all_cars)
    # Initiate search result list.
    search_results = []
    # Loop through the cars list and match the search parameter.
    for make, model in cars.items():
        for element in model:
            model_partitions = list(element.split(" "))
            for part in model_partitions:
                if search_parameter.casefold() == part.casefold():
                    search_results.append(f"{make} {element}")
    return search_results


if __name__ == '__main__':
    print(list_of_cars("Audi A4,Skoda Superb,Audi A4"))  # ["Audi A4", "Skoda Superb", "Audi A4"]
    print(list_of_cars("Audi A4 Skoda Superb Audi A4"))  # ["Audi A4 Skoda Superb Audi A4"]
    print(list_of_cars(""))  # []
    print("*****")

    print(car_makes("Audi A4,Skoda Super,Skoda Octavia,BMW 530,Seat Leon,Skoda Superb,Skoda Superb,BMW x5"))
    # ['Audi', 'Skoda', 'BMW', 'Seat']

    print(car_makes("Mazda 6,Mazda 6,Mazda 6,Mazda 6"))  # ['Mazda']
    print(car_makes(""))  # []
    print("*****")

    print(car_models("Audi A4,Skoda Superb,Audi A4,Audi A6"))  # ["A4", "Superb", "A6"]
    print(car_models(""))  # []
    print("*****")

    print(search_by_make("Audi A4 2021,Skoda Superb,Seat Leon,Skoda Superb,Audi A4 2022 sept", "Audi"))
    # ['Audi A4 2021', 'Audi A4 2022 sept']

    print(search_by_make("Audi A4", "A4"))  # []
    print(search_by_make("Audi A4,audi A5,AUDI a6 A7", "Audi"))  # ['Audi A4', 'audi A5', 'AUDI a6 A7']
    print(search_by_make("Audi A4,audi A5,AUDI a6 A7", "AUDI"))  # ['Audi A4', 'audi A5', 'AUDI a6 A7']
    print(search_by_make("Audi A4,Skoda Superb,Seat Leon,Audi A4,Seat Leon,Audi A4,Audi A6,Audi A4 2022", "Audi"))
    # ['Audi A4', 'Audi A4', 'Audi A4', 'Audi A6', 'Audi A4 2022']
    print("*****")

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
    print("*****")
