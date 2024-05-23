from abc import ABC, abstractmethod
import weapons

class Hero_abstract(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_armor(self) -> weapons.Armor:
        pass

    @abstractmethod
    def get_weapon(self) -> weapons.Weapon:
        pass

    @abstractmethod
    def get_attack_power(self) -> int:
        pass

    @abstractmethod
    def get_health(self) -> int:
        pass

    @abstractmethod
    def change_weapon(self, weapon: weapons.Weapon):
        pass

    @abstractmethod
    def change_armor(self, armor: weapons.Armor):
        pass

    @abstractmethod
    def attack(self, enemy: "Hero_abstract") -> None:
        pass

    @abstractmethod
    def take_damage(self, damage: int):
        pass

    @abstractmethod
    def is_alive(self) -> bool:
        pass

    @abstractmethod
    def is_computer(self) -> bool:
        pass

    @abstractmethod
    def regenerate(self) -> None:
        pass

class Hero(Hero_abstract):
    def __init__(self, is_computer: bool) -> None:
        self.__is_computer = is_computer
        if is_computer:
            self.__name = "Godzilla"
        else:
            self.__name = input("Enter your name: ")
        self.regenerate()

    def regenerate(self) -> None:
        self.__health = 100
        self.__attack_power = 20
        self.__armor = weapons.Bare_skin()
        self.__weapon = weapons.Bare_hands()

    def get_name(self) -> str:
        return self.__name

    def get_health(self) -> int:
        return self.__health

    def get_attack_power(self) -> int: 
        return self.__attack_power

    def get_armor(self) -> weapons.Armor:
        return self.__armor

    def get_weapon(self) -> weapons.Weapon:
        return self.__weapon

    def change_armor(self, armor: weapons.Armor):
        print(f"{self.__name} changes armor to {armor.get_name()}")
        self.__armor = armor

    def change_weapon(self, weapon: weapons.Weapon):
        print(f"{self.__name} changes weapon to {weapon.get_name()}")
        self.__weapon = weapon

    def attack(self, enemy: "Hero_abstract") -> None:
        attack = self.__attack_power + self.__weapon.attack(enemy)
        if attack < 0:
            attack = 0
        print (f"{self.__name} attacks {enemy.get_name()} with {self.__weapon.get_name()} with strength {attack}...")
        damage = attack - enemy.get_armor().get_strength()
        if damage < 0:
            damage = 0
        print(f"...and deals {damage} damage to {enemy.get_name()}!\n")
        enemy.take_damage(damage)        

    def take_damage(self, damage: int):
        self.__health -= damage
        self.__attack_power = 20 * self.__health // 100

    def is_alive(self) -> bool:
        return self.__health > 0

    def is_computer(self) -> bool:
        return self.__is_computer