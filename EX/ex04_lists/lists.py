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
    cars_list = all_cars.split(",")
    return cars_list


def car_makes(all_cars: str) -> list:
    """
    Return list of unique car makes.

    The order of the elements should be the same as in the input string (first appearance).

    "Audi A4,Skoda Superb,Audi A4" => ["Audi", "Skoda"]
    """
    all_cars = all_cars.strip()
    if not all_cars:
        return []
    list_with_models = list_of_cars(all_cars)
    list_of_makes = []
    for make in list_with_models:
        space_index = make.find(" ")
        car_make = make[:space_index]
        if car_make not in list_of_makes:
            list_of_makes.append(car_make)
    return list_of_makes


def car_models(all_cars: str) -> list:
    """
    Return list of unique car models.

    The order of the elements should be the same as in the input string (first appearance).

    "Audi A4,Skoda Superb,Audi A4,Audi A6" => ["A4", "Superb", "A6"]
    """
    all_cars = all_cars.strip()
    if not all_cars:
        return []
    list_with_models = list_of_cars(all_cars)
    models_list = []
    for model in list_with_models:
        space_index = model.find(" ")
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
