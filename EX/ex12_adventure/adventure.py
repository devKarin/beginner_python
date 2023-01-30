"""
EX12 - Adventure.

This program creates a game simulator.

Available classes:
Adventurer; Adventurer class
Monster; Monster class. Describes the opponents (enemies) of adventurers.
World; The World class. Holds the game logic.

Methods in Adventurer class:
__init__(self, name: str, class_type: str, power: int, experience: int = 0));
    -> Adventurer class constructor. Every adventurer has a name, a class type,
    power and experience, which is initially 0.
    -> Uses base class (AlchemicalStorage) constructor and extends it with recipes from AlchemicalRecipes class.
__repr__(self) -> str; Representation of Adventurer. Returns adventurer data as a formatted string.
add_power(self, power: int); Adds given amount of power to adventurer.
add_experience(self, exp: int); Add experience or power to adventurer.

Methods in Monster class:
__init__(self, name: str, type: str, power: int); Monster class constructor. Every monster has a name, a type and power.
@property def name(self); Returns the name of the monster.
__repr__(self) -> str; Representation of Monster. Returns monster data as a formatted string.

Methods in World class:
__init__(self, python_master: str = "Sõber");
    -> Initialize the class 'World'. Every world instance must have a name which is a name of the Python Master.
    Every object has a Python Master, adventurer list, list of active adventurers, monster list, list of active
    monsters, graveyard and sometimes necromancers.
@property def python_master(self); Returns the Python Master.
get_python_master(self); Returns the Python Master.
get_adventurer_list(self) -> list; Returns the list of adventurers in this world.
get_monster_list(self) -> list; Returns the list of monsters in this world.
get_graveyard(self) -> list; Returns list of all characters (adventurers and monsters) fallen during the game.
add_adventurer(self, character: Adventurer); Adds an adventurer into the world.
add_monster(self, character: Monster); Adds a monster into the world.
remove_character(self, name: str); Remove character from the world by name using graveyard.
necromancers_active(self, is_necromancers_active: bool); Sets necromancers activity in the world.
revive_graveyard(self); Revives all characters in graveyard.
get_active_adventurers(self) -> list; Returns active adventurers sorted by experience descending.
add_strongest_adventurer(self, class_type: str); Activates the strongest adventurer.
add_weakest_adventurer(self, class_type: str); Activate the weakest adventurer.
add_most_experienced_adventurer(self, class_type: str); Activates the most experienced adventurer.
add_least_experienced_adventurer(self, class_type: str); Activates the least experienced adventurer.
add_adventurer_by_name(self, name: str); Activates adventurer by name.
add_all_adventurers_of_class_type(self, class_type: str); Activates all adventurers with given class type.
add_all_adventurers(self); Activates all non-active adventurers.
get_active_monsters(self) -> list; Returns active monsters sorted by power descending.
add_monster_by_name(self, name: str); Activates monster by name.
add_strongest_monster(self); Activates the strongest monster.
add_weakest_monster(self); Activates the weakest monster.
add_all_monsters_of_type(self, type: str); Activates all monsters with given type.
add_all_monsters(self); Adds all non-active monsters.

"""


import math


class Adventurer:
    """
    Adventurer class.

    The Adventurer class describes the adventurers.
    """

    def __init__(self, name: str, class_type: str, power: int, experience: int = 0):
        """
        Initialize the Adventurer class.

        Every object has a name, class type, power and experience.

        self.name = name
        :param name: name of the adventurer
        :param class_type: type of the adventurer
        :param power: power of the adventurer
        :param experience: experience of the adventurer
        """
        self.name = name
        self.class_type = class_type
        self.power = int(power)
        self.experience = experience
        if class_type not in {"Druid", "Wizard", "Paladin"}:
            self.class_type = "Fighter"
        if power > 99:
            self.power = 10

    def __repr__(self) -> str:
        """
        Representation of Adventurer.

        Returns adventurer data as a formatted string.
        :return: string representation of adventurer data
        """
        return f"{self.name}, the {self.class_type}, Power: {self.power}, Experience: {self.experience}."

    def add_power(self, power: int):
        """
        Add power to adventurer.

        Adds given amount of power to adventurer.
        :param power: power points to add to adventurer
        :return:
        """
        self.power += int(power)

    def add_experience(self, exp: int):
        """
        Add experience to adventurer.

        Adds given amount of experience to the adventurer. If the adventurer has more than 99 experience points,
        the adventurer gains one tenth of experience (rounded down) worth power and the experience drops to 0.

        :param exp: experience points to add to the adventurer
        :return:
        """
        if exp < 0:
            return
        self.experience += exp
        if self.experience > 99:
            self.power += math.floor(self.experience / 10)
            self.experience = 0


class Monster:
    """
    Monster class.

    The Monster class describes monsters who are opponents (enemies) of adventurers.
    """

    def __init__(self, name: str, type: str, power: int):
        """
        Initialize the Monster class.

        Every monster has a name, type and power.

        :param name: monster name
        :param type: monster type
        :param power: monster power points
        """
        self.type = type
        self. power = int(power)
        self.type = type
        self.initial_name = name

    @property
    def name(self):
        """
        Return the name of the monster.

        If the monster type is 'Zombie', adds prefix 'Undead' to the name.

        :return: name of the monster
        """
        if self.type.startswith("Zombie"):
            return f"Undead {self.initial_name}"
        else:
            return self.initial_name

    def __repr__(self) -> str:
        """
        Representation of Monster.

        Returns monster data as a formatted string.

        :return: string representation of monster data
        """
        return f"{self.name} of type {self.type}, Power: {self.power}."


class World:
    """
    Class 'World'.

    Every world instance must have a name which is a name of the Python Master.
    """

    def __init__(self, python_master: str = "Sõber"):
        """
        Initialize the class 'World'.

        Every object has a Python Master, adventurer list, list of active adventurers, monster list,
        list of active monsters, graveyard and sometimes necromancers.
        """
        self.__master = python_master
        self.adventurer_list = []
        self.monster_list = []
        self.graveyard = []
        self.active_adventurers = []
        self.active_monsters = []
        self.is_necromancers_active = False

    # The name of the Python Master must not be changed.
    @property
    def python_master(self):
        """
        Return the Python Master.

        Returns the Python Master.

        :return: the python master
        """
        return self.__master

    def get_python_master(self):
        """
        Get the Python Master.

        Returns the Python Master.

        :return: the python master instance
        """
        return self.python_master

    def get_adventurer_list(self) -> list:
        """
        Get the list of adventurers in this world.

        Returns the list of adventurers in this world.

        :return: list of adventurers
        """
        return self.adventurer_list

    def get_monster_list(self) -> list:
        """
        Get the list of monsters in this world.

        Returns the list of monsters in this world.

        :return: list of monsters
        """
        return self.monster_list

    def get_graveyard(self) -> list:
        """
        Get the list of fallen characters in this world.

        Returns list of all characters (adventurers and monsters) fallen during the game.

        :return: list of fallen characters
        """
        return self.graveyard

    def add_adventurer(self, character: Adventurer):
        """
        Add an adventurer into the world.

        Adds an adventurer into the worlds adventurer list. Checks before adding in order to prevent listing monsters
        among adventurers.

        :param character: adventurer to add
        :return:
        """
        # Check whether the character to be added is a type of Adventurer.
        if isinstance(character, Adventurer):
            self.adventurer_list.append(character)

    def add_monster(self, character: Monster):
        """
        Add a monster into the world.

        Adds a monster into the world. Checks the type of the character to be added before adding in order to prevent
        listing adventurers among monsters.

        :param character: monster to add
        :return:
        """
        # Check whether the character to be added is a type of Monster.
        if isinstance(character, Monster):
            self.monster_list.append(character)

    def remove_character(self, name: str):
        """
        Remove character from the world by name using graveyard.

        Removes character from world and adds it into graveyard.
        If the character is already in the graveyard, deletes the character.

        :param name: character to remove
        :return:
        """
        character_to_remove = list(filter(lambda character: character.name == name, self.adventurer_list))
        if character_to_remove:
            self.graveyard.append(character_to_remove[0])
            self.adventurer_list.remove(character_to_remove[0])
            return
        character_to_remove = list(filter(lambda character: character.name == name, self.monster_list))
        if character_to_remove:
            self.graveyard.append(character_to_remove[0])
            self.monster_list.remove(character_to_remove[0])
            return
        character_to_remove = list(filter(lambda character: character.name == name, self.graveyard))
        if character_to_remove:
            self.graveyard.remove(character_to_remove[0])

    def necromancers_active(self, is_necromancers_active: bool):
        """
        Set necromancers activity.

        Sets necromancers activity in the world.

        :param is_necromancers_active: indicates whether the necromancers are activated
        :return:
        """
        self.is_necromancers_active = is_necromancers_active

    def revive_graveyard(self):
        """
        Revive all characters in graveyard.

        Turns all monsters in graveyard into zombies and moves them from graveyard into monster list,
        turns all adventurers in graveyard into zombies and moves them into monster list,
        inactivates necromancers.

        :return:
        """
        if not self.is_necromancers_active:
            return
        for character in self.graveyard:
            if isinstance(character, Monster):
                character.type = "Zombie"
                self.monster_list.append(character)
            elif isinstance(character, Adventurer):
                self.add_monster(Monster(character.name, f"Zombie {character.class_type}", character.power))
        self.graveyard.clear()
        self.is_necromancers_active = False

    def get_active_adventurers(self) -> list:
        """
        Return active adventurers sorted by experience descending.

        Returns a list where active adventurers are sorted descending by experience.

        :return: list of active adventurers
        """
        return sorted(self.active_adventurers, key=lambda adventurer: -adventurer.experience)

    def add_strongest_adventurer(self, class_type: str):
        """
        Activate the strongest adventurer.

        Adds the adventurer who has the most power with given class type into active adventurers list.

        :param class_type: type of adventurer
        :return:
        """
        filtered_list = list(filter(lambda adventurer: adventurer.class_type == class_type, self.adventurer_list))
        if filtered_list:
            strongest_adventurer = max(filtered_list, key=lambda adventurer: adventurer.power)
            self.active_adventurers.append(strongest_adventurer)
            self.adventurer_list.remove(strongest_adventurer)

    def add_weakest_adventurer(self, class_type: str):
        """
        Activate the weakest adventurer.

        Adds the adventurer who has the least power with given class type into active adventurers list.

        :param class_type: type of adventurer
        :return:
        """
        filtered_list = list(filter(lambda adventurer: adventurer.class_type == class_type, self.adventurer_list))
        if filtered_list:
            weakest_adventurer = min(filtered_list, key=lambda adventurer: adventurer.power)
            self.active_adventurers.append(weakest_adventurer)
            self.adventurer_list.remove(weakest_adventurer)

    def add_most_experienced_adventurer(self, class_type: str):
        """
        Activate the most experienced adventurer.

        Adds the adventurer who has the most experience with given class type into active adventurers list.

        :param class_type: type of adventurer
        :return:
        """
        filtered_list = list(filter(lambda adventurer: adventurer.class_type == class_type, self.adventurer_list))
        if filtered_list:
            most_experienced_adventurer = max(filtered_list, key=lambda adventurer: adventurer.experience)
            self.active_adventurers.append(most_experienced_adventurer)
            self.adventurer_list.remove(most_experienced_adventurer)

    def add_least_experienced_adventurer(self, class_type: str):
        """
        Activate the least experienced adventurer.

        Adds the adventurer who has the least experience with given class type into active adventurers list.

        :param class_type: type of adventurer
        :return:
        """
        filtered_list = list(filter(lambda adventurer: adventurer.class_type == class_type, self.adventurer_list))
        if filtered_list:
            least_experienced_adventurer = min(filtered_list, key=lambda adventurer: adventurer.experience)
            self.active_adventurers.append(least_experienced_adventurer)
            self.adventurer_list.remove(least_experienced_adventurer)

    def add_adventurer_by_name(self, name: str):
        """
        Activate adventurer by name.

        If an adventurer with such name exists, adds it into active adventurers list.

        :param name: adventurer name
        :return:
        """
        adventurers_to_activate = list(filter(lambda adventurer: adventurer.name == name, self.adventurer_list))
        self.active_adventurers.extend(adventurers_to_activate)
        self.adventurer_list = \
            list(filter(lambda adventurer: adventurer not in adventurers_to_activate, self.adventurer_list))

    def add_all_adventurers_of_class_type(self, class_type: str):
        """
        Activate all adventurers with given class type.

        Adds all adventurers with given class type into active adventurers list.

        :param class_type: type of adventurer
        :return:
        """
        filtered_list = list(filter(lambda adventurer: adventurer.class_type == class_type, self.adventurer_list))
        self.active_adventurers.extend(filtered_list)
        self.adventurer_list = list(filter(lambda adventurer: adventurer not in filtered_list, self.adventurer_list))

    def add_all_adventurers(self):
        """
        Activate all non-active adventurers.

        Adds all adventurers from adventurers list into active adventurers list.

        :return:
        """
        self.active_adventurers.extend(adventurer for adventurer in self.adventurer_list)
        self.adventurer_list.clear()

    def get_active_monsters(self) -> list:
        """
        Return active monsters sorted by power descending.

        Returns a list where active monsters are sorted descending by power.

        :return: list of active monsters
        """
        return sorted(self.active_monsters, key=lambda monster: -monster.power)

    def add_monster_by_name(self, name: str):
        """
        Activate monster by name.

        If a monster with such name exists, adds it into active monsters list.

        :param name: monster name
        :return:
        """
        monsters_to_activate = list(filter(lambda monster: monster.name == name, self.monster_list))
        self.active_monsters.extend(monsters_to_activate)
        self.monster_list = list(filter(lambda monster: monster not in monsters_to_activate, self.monster_list))

    def add_strongest_monster(self):
        """
        Activate the strongest monster.

        Adds the monster with the most power into active monsters list.

        :return:
        """
        if self.monster_list:
            strongest_monster = max(self.monster_list, key=lambda monster: monster.power)
            self.active_monsters.append(strongest_monster)
            self.monster_list.remove(strongest_monster)

    def add_weakest_monster(self):
        """
        Activate the weakest monster.

        Adds the monster with the least power into active monsters list.

        :return:
        """
        if self.monster_list:
            weakest_monster = min(self.monster_list, key=lambda monster: monster.power)
            self.active_monsters.append(weakest_monster)
            self.monster_list.remove(weakest_monster)

    def add_all_monsters_of_type(self, type: str):
        """
        Activate all monsters with given type.

        Adds all monsters with given type into active monsters list.

        :param type: monster type
        :return:
        """
        filtered_list = list(filter(lambda monster: monster.type == type, self.monster_list))
        self.active_monsters.extend(filtered_list)
        self.monster_list = list(filter(lambda monster: monster not in filtered_list, self.monster_list))

    def add_all_monsters(self):
        """
        Add all non-active monsters.

        Adds all monsters from monsters list into active monsters list.

        :return:
        """
        self.active_monsters.extend(monster for monster in self.monster_list)
        self.monster_list.clear()

    def remove_animals_and_ents(self):
        """
        Remove Animal and Ent type monsters from active monsters if Druid is present.

        Removes Animal or Ent type monsters from active monsters list and adds them into monsters list if
        among adventurers is an adventurer with a class type Druid.

        :return:
        """
        # Is there a Druid among adventurers.
        if list(filter(lambda adventurer: adventurer.class_type == "Druid", self.active_adventurers)):
            # If there are monsters with type Animal or Ent they return from active monsters into monsters list.
            animals_and_ents = list(filter(lambda monster: monster.type in ["Animal", "Ent"], self.active_monsters))
            for monster in animals_and_ents:
                self.active_monsters.remove(monster)
                self.monster_list.append(monster)

    def double_paladin_power(self):
        """
        Double Paladin class type active adventurers power.

        Doubles the power of all Paladin class type adventurers if there is an active monster of type "Zombie",
        "Zombie Fighter", "Zombie Druid", "Zombie Paladin" or "Zombie Wizard".

        :return:
        """
        if list(filter(lambda monster: monster.type in ["Zombie",
                                                        "Zombie Fighter",
                                                        "Zombie Druid",
                                                        "Zombie Paladin",
                                                        "Zombie Wizard"], self.active_monsters)):
            paladins = list(filter(lambda adventurer: adventurer.class_type == "Paladin", self.active_adventurers))
            for paladin in paladins:
                paladin.power *= 2

    def resume_paladin_power(self):
        """
        Resume the power of all Paladin class type active adventurers after the fight.

        Resumes the power level of all active adventurers of class type Paladin to the pre-fight level.

        :return:
        """
        paladins = list(filter(lambda adventurer: adventurer.class_type == "Paladin", self.active_adventurers))
        for paladin in paladins:
            paladin.power = math.floor(paladin.power / 2)

    def compare_powers(self):
        """
        Compare active adventurers and active monsters powers to decide the winners.

        Compares the sum power of active adventurers and active monsters and returns a tuple containing a character
        marking the winner ("A" - adventurers win, "M" - monsters win, T -tie),summed power of adventurers and
        summed power of monsters.

        :return: tuple containing character marking the winning team and teams summed powers
        """
        adventurers_power = 0
        monsters_power = 0
        for adventurer in self.active_adventurers:
            adventurers_power += adventurer.power
        for monster in self.active_monsters:
            monsters_power += monster.power
        if adventurers_power > monsters_power:
            return "A", adventurers_power, monsters_power
        if adventurers_power < monsters_power:
            return "M", adventurers_power, monsters_power
        if adventurers_power == monsters_power:
            return "T", adventurers_power, monsters_power

    def calculate_experience(self, result: tuple, deadly: bool):
        """
        Calculate new experience points after the adventure.

        Calculates the amount of gained experience and adds them to winners accordingly.

        :param result: the result of the adventure given as a tuple containing winner and power points
        :param deadly: was the adventure deadly or not
        :return:
        """
        if result[0] == "A":
            experience_gained = math.floor(result[2] / len(self.active_adventurers))
            for adventurer in self.active_adventurers:
                if deadly:
                    adventurer.add_experience(experience_gained * 2)
                else:
                    adventurer.add_experience(experience_gained)
        elif result[0] == "T":
            experience_gained = math.floor(result[2] / len(self.active_adventurers))
            for adventurer in self.active_adventurers:
                adventurer.add_experience(math.floor(experience_gained / 2))

    def go_adventure(self, deadly: bool = False):
        """
        Apply game logic.

        Applies game logic to the world.

        :param deadly:
        :return:
        """
        # Set power conditions prior adventure.
        self.remove_animals_and_ents()
        self.double_paladin_power()
        # Decide who is going to win.
        game_result = self.compare_powers()
        self.resume_paladin_power()
        # Add experience.
        self.calculate_experience(game_result, deadly)

        # Move fighters into proper list after the adventure.
        if not deadly:
            self.adventurer_list.extend(self.active_adventurers)
            self.active_adventurers.clear()
            self.monster_list.extend(self.active_monsters)
            self.active_monsters.clear()
        elif deadly:
            if game_result[0] == "A":
                self.adventurer_list.extend(self.active_adventurers)
                self.active_adventurers.clear()
                # Since the elements of active monsters list can not be deleted during looping the same list
                # use a helper list.
                monsters_to_remove = self.get_active_monsters()
                for monster in monsters_to_remove:
                    # Moves the monster into the graveyard.
                    self.graveyard.append(monster)
                    self.active_monsters.remove(monster)
                    # Removes the monster completely.
                    # self.remove_character(monster.name)
            elif game_result[0] == "M":
                self.monster_list.extend(self.active_monsters)
                self.active_monsters.clear()
                # Since the elements of active adventurers list can not be deleted during looping the same list
                # use a helper list.
                adventurers_to_remove = self.get_active_adventurers()
                for adventurer in adventurers_to_remove:
                    # Moves the adventurer into the graveyard.
                    self.graveyard.append(adventurer)
                    self.active_adventurers.remove(adventurer)
                    # Removes the adventurer completely.
                    # self.remove_character(adventurer.name)


if __name__ == "__main__":
    world = World("Sõber")
    hero = Adventurer("Sander", "Paladin", 50)
    hero2 = Adventurer("Toomas", "Druid", 50)
    hero3 = Adventurer("Toots", "Druid", 1)
    hero3.add_experience(149)

    print(hero3.power == 15)

    monster = Monster("Giant Badger", "Animal", 39043)
    monster2 = Monster("Monsu", "Zombie", 149)
    monster3 = Monster("Tilluke asi", "suva", 1)

    world.add_monster(monster)
    world.add_monster(monster2)
    world.add_adventurer(hero)
    world.add_adventurer(hero2)

    print(world.get_adventurer_list())  # Sander, Toomas
    print(world.get_monster_list())  # Giant Badger, Monsu

    world.add_all_adventurers()

    print(world.get_adventurer_list())  # []
    print(world.get_active_adventurers())  # Sander, Toomas

    world.add_all_monsters()

    print(world.get_monster_list())  # []
    print(world.get_active_monsters())  # Giant Badger, Monsu

    world.go_adventure(True)

    world.add_monster(monster3)
    world.add_adventurer(hero3)
    world.add_adventurer_by_name("Toomas")
    world.add_monster_by_name("Tilluke asi")

    world.go_adventure(True)

    print(hero2)  # "Toomas, the Druid, Power: 64, Experience: 2."


if __name__ == "__main__2":
    hero = Adventurer("Mart", "Wizard", 50)
    hero2 = Adventurer("Sander", "Paladin", 50)
    monster = Monster("Goblin", "Goblin", 5)
    zombie = Monster("Goblin", "Zombie", 5)
    world = World("PM")

    world.get_graveyard().append(hero)
    world.get_graveyard().append(hero2)
    world.get_graveyard().append(monster)
    world.get_graveyard().append(zombie)

    world.revive_graveyard()
    print(len(world.get_graveyard()))  # 4


if __name__ == "__main__3":
    print("Kord oli maailm.")
    world = World("Sõber")
    print(world.get_python_master())  # -> "Sõber"
    print(world.get_graveyard())  # -> []
    print()
    print("Tutvustame tegelasi.")
    hero = Adventurer("Sander", "Paladin", 50)
    friend = Adventurer("Peep", "Druid", 25)
    another_friend = Adventurer("Toots", "Wizard", 40)
    annoying_friend = Adventurer("XxX_Eepiline_Sõdalane_XxX", "Tulevikurändaja ja ninja", 999999)
    print(hero)  # -> "Sander, the Paladin, Power: 50, Experience: 0."
    # Ei, tüütu sõber, sa ei saa olla tulevikurändaja ja ninja, nüüd sa pead fighter olema.
    # Ei maksa liiga tugevaks ka ennast alguses teha!
    print(annoying_friend)  # -> "XxX_Eepiline_Sõdalane_XxX, the Fighter, Power: 10, Experience: 0."
    print(friend)  # -> "Peep, the Druid, Power: 25, Experience: 0."
    print(another_friend)  # -> "Toots, the Wizard, Power: 40, Experience: 0."
    print()

    print("Peep, sa tundud kuidagi nõrk, ma lisasin sulle natukene tugevust.")
    friend.add_power(20)
    print(friend)  # -> "Peep, the Druid, Power: 45, Experience: 0."
    print()

    world.add_adventurer(hero)
    world.add_adventurer(friend)
    world.add_adventurer(another_friend)
    print(world.get_adventurer_list())
    # -> [Sander, the Paladin, Power: 50, Experience: 0.,
    # Peep, the Druid, Power: 45, Experience: 0., Toots, the Wizard, Power: 40, Experience: 0.]

    world.add_monster(annoying_friend)
    # Ei, tüütu sõber, sa ei saa olla vaenlane.
    print(world.get_monster_list())  # -> []
    world.add_adventurer(annoying_friend)
    print()

    print("Oodake veidikene, ma tekitan natukene kolle.")
    zombie = Monster("Rat", "Zombie", 10)
    goblin_spear = Monster("Goblin Spearman", "Goblin", 10)
    goblin_archer = Monster("Goblin Archer", "Goblin", 5)
    big_ogre = Monster("Big Ogre", "Ogre", 120)
    gargantuan_badger = Monster("Massive Badger", "Animal", 1590)

    print(big_ogre)  # -> "Big Ogre of type Ogre, Power: 120."
    print(zombie)  # -> "Undead Rat of type Zombie, Power: 10."

    world.add_monster(goblin_spear)

    print()
    print("Mängime esimese seikluse läbi!")
    world.add_strongest_adventurer("Druid")
    world.add_strongest_monster()
    print(world.get_active_adventurers())  # -> [Peep, the Druid, Power: 45, Experience: 0.]
    print(world.get_active_monsters())  # -> [Goblin Spearman of type Goblin, Power: 10.]
    print()

    world.go_adventure(True)

    world.add_strongest_adventurer("Druid")
    print(world.get_active_adventurers())  # -> [Peep, the Druid, Power: 45, Experience: 20.]
    print("Surnuaias peaks üks goblin olema.")
    print(world.get_graveyard())  # ->[Goblin Spearman of type Goblin, Power: 10.]
    print()

    world.add_monster(gargantuan_badger)
    world.add_strongest_monster()

    world.go_adventure(True)
    # Druid on loomade sõber ja ajab massiivse mägra ära.
    print(world.get_adventurer_list())  # -> Kõik 4 mängijat.
    print(world.get_monster_list())  # -> [Massive Badger of type Animal, Power: 1590.]

    world.remove_character("Massive Badger")
    print(world.get_monster_list())  # -> []
    print()

    print("Su sõber ütleb: \"Kui kõik need testid andsid sinu koodiga sama tulemuse "
          "mille ma siin ette kirjutasin, peaks kõik okei olema, proovi testerisse pushida! \" ")
