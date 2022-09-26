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
    # Split the string at comma and turn it into a list.
    cars_list = all_cars.split(",")
    if not cars_list:
        return []
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
        return []
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
        return []
    # Initiate models list.
    models_list = []
    for model in list_with_models:
        space_index = model.find(" ")
        # Slice the model-make list item at the space and use the part after the space (car model).
        # In order to start slicing right after the space, 1 needs to be added to the space index,
        # because the letter at the index, which marks the start of the slice will be included.
        model = model[space_index + 1:]
        if model not in models_list:
            models_list.append(model)
    return models_list


if __name__ == '__main__':
    print(list_of_cars("Audi A4,Skoda Superb,Audi A4"))  # ["Audi A4", "Skoda Superb", "Audi A4"]

    print(car_makes("Audi A4,Skoda Super,Skoda Octavia,BMW 530,Seat Leon,Skoda Superb,Skoda Superb,BMW x5"))
    # ['Audi', 'Skoda', 'BMW', 'Seat']

    print(car_makes("Mazda 6,Mazda 6,Mazda 6,Mazda 6"))  # ['Mazda']
    print(car_makes(""))  # []

    print(car_models("Audi A4,Skoda Superb,Audi A4,Audi A6"))  # ["A4", "Superb", "A6"]
    print(car_models(""))  # []
