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
        self.power = power
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
        self.power += power

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
        self. power = power
        self.type = type
        self.initial_name = name

    @property
    def name(self):
        """
        Return the name of the monster.

        If the monster type is 'Zombie', adds prefix 'Undead' to the name.

        :return: name of the monster
        """
        if self.type == "Zombie":
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

        Return sthe list of adventurers in this world.

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
        character_to_remove = list(filter(lambda character: character.name == name, self.adventurer_list))[0]
        if character_to_remove:
            self.graveyard.append(character_to_remove)
            self.adventurer_list.remove(character_to_remove)
            return
        character_to_remove = list(filter(lambda character: character.name == name, self.monster_list))[0]
        if character_to_remove:
            self.graveyard.append(character_to_remove)
            self.monster_list.remove(character_to_remove)
            return
        character_to_remove = list(filter(lambda character: character.name == name, self.graveyard))[0]
        if character_to_remove:
            self.graveyard.remove(character_to_remove)

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
        self.adventurer_list.clear()


if __name__ == "__main__":
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
    print(world.get_adventurer_list())  # -> Sander, Peep ja Toots

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
    print(world.get_active_adventurers())  # -> Peep
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
