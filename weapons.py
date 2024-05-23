from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def attack(self, enemy) -> int:
        pass

class Armor(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_class(self) -> str:
        pass

    def get_strength(self) -> int:
        pass

class Bare_hands(Weapon):
    def get_name(self) -> str:
        return "Bare hands"

    def attack(self, enemy) -> int:
        armor = enemy.get_armor()
        if armor.get_class() == "close":
            return -5
        else:
            return 0
    
class Bare_skin(Armor):
    def get_name(self) -> str:
        return "Bare skin"

    def get_class(self) -> str:
        return "close"

    def get_strength(self) -> int:
        return 0
    
class Sword(Weapon):
    def get_name(self) -> str:
        return "Sword"

    def attack(self, enemy) -> int:
        armor = enemy.get_armor()
        if armor.get_class() == "close":
            return 10
        elif armor.get_class() == "magic":
            return 40
        else:
            return 20
        
class Large_shield(Armor):
    def get_name(self) -> str:
        return "Large shield"

    def get_class(self) -> str:
        return "close"

    def get_strength(self) -> int:
        return 5
    
class Bow(Weapon):
    def get_name(self) -> str:
        return "Bow"

    def attack(self, enemy) -> int:
        armor = enemy.get_armor()
        if armor.get_class() == "close":
            return 20
        elif armor.get_class() == "magic":
            return 30
        else:
            return 10
        
class Small_shield(Armor):
    def get_name(self) -> str:
        return "Small shield"

    def get_class(self) -> str:
        return "distant"

    def get_strength(self) -> int:
        return 5
    
class Lightning(Weapon):
    def get_name(self) -> str:
        return "Lightning"

    def attack(self, enemy) -> int:
        armor = enemy.get_armor()
        if armor.get_class() == "magic":
            return 0
        else:
            return 30
        
class Magic_dome(Armor):
    def get_name(self) -> str:
        return "Magic dome"

    def get_class(self) -> str:
        return "magic"

    def get_strength(self) -> int:
        return 10