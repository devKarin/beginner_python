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
__repr__(self) -> str; Representation of Monster. Returns monster data as a formatted string.

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
        if class_type not in ["Fighter", "Druid", "Wizard", "Paladin"]:
            self.class_type = "Fighter"
        if power > 99:
            self.power = 10
        if experience < 0:
            self.experience = 0

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
        self.experience += exp
        if self.experience > 99:
            self.power = math.floor(self.experience / 10)
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
        # Read about @property. Maybe create name using @property?
        self.name = name
        self.type = type
        self. power = power
        if self.type == "Zombie":
            self.name = f"Undead {name}"
        # Solve it later
        # Type can change during time because of necromancers. So if-clause in __init__ is not enough.

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

    Every world instance must have a name.
    """

    def __init__(self, python_master: str = "Sõber"):
        """
        Initialize the class 'World.

        Every object has a python master.
        """
        self.__python_master__ = python_master
        self.adventurer_list = []
        self.monster_list = []
        self.graveyard = []
        self.necromancers = False

    def __repr__(self) -> str:
        """
        Representation of AlchemicalElement.

        Returns element name as a formatted string.
        :return:
        """
        pass

    def get_python_master(self):
        """
        Get the name of the Python Master.

        :return: the name of the instance (python master)
        """
        return self.__python_master__

    def get_adventurer_list(self):
        """
        Get the list of adventurers in this world.

        :return: list of adventurers
        """
        return [adventurer.name for adventurer in self.adventurer_list]

    def get_monster_list(self):
        """
        Get the list of monsters in this world.

        :return: list of monsters
        """
        return [monster.name for monster in self.monster_list]

    def get_graveyard(self) -> list:
        """
        Get the list of fallen characters in this world.

        Gets the list of all characters (adventurers and monsters) fallen during the game.
        :return: list of fallen characters
        """
        # TODO: world.get_graveyard().append(monster)
        return [character.name for character in self.graveyard]

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
        Remove character from the world using graveyard.

        Removes character from world and add it into graveyard.
        If the character is already in the graveyard, deletes the character.

        :param name: character to remove
        :return:
        """
        if name in self.get_adventurer_list():
            removed_character = self.adventurer_list\
                .pop(self.adventurer_list.index(lambda character: character.name == name))
            self.graveyard.append(removed_character)
            return
        if name in self.get_monster_list():
            removed_character = self.monster_list.pop(self.monster_list.index(lambda character: character.name == name))
            self.graveyard.append(removed_character)
            return
        if name in self.graveyard:
            self.graveyard.pop(self.graveyard.index(lambda character: character.name == name))

    def necromancers_active(self, necromancers: bool):
        """
        Set nectomancers activity.

        Sets nectomancers activity in the world.
        :param necromancers:
        :return:
        """
        self.necromancers = necromancers

    def revive_graveyard(self):
        pass


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