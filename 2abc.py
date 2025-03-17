from abc import ABC, abstractmethod

class Shinobi(ABC):
    def __init__(self, name, chakra):
        self.name = name
        self.chakra = chakra

    @abstractmethod
    def jutsu(self):
        pass

    @abstractmethod
    def special_ability(self):
        pass

class Uchiha(Shinobi):
    def jutsu(self):
        print(f"{self.name} uses Fireball Jutsu!")

    def special_ability(self):
        print(f"{self.name} activates Sharingan!")

class Uzumaki(Shinobi):
    def jutsu(self):
        print(f"{self.name} uses Rasengan!")

    def special_ability(self):
        print(f"{self.name} activates Sage Mode!")

sasuke = Uchiha("Sasuke", 300)
naruto = Uzumaki("Naruto", 500)

print("=== Shinobi Battle ===")
sasuke.jutsu()
sasuke.special_ability()
naruto.jutsu()
naruto.special_ability()
