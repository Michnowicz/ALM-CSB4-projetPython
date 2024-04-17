

class Player:
    def __init__(self, name):
        self.name = name
        self.place = "maison"
        self.lvl = 1
        self.exp = 0
        self.gold = 0
        self.inventory = []

    def player_attack(self, ennemy):
            print(f"\nVous attaquez {ennemy.name}.")
            if self.atk > ennemy.armor:
                damage = self.atk - ennemy.armor
            else:
                damage = 0
            if ennemy.hp < damage:
                ennemy.hp = 0
            else:
                ennemy.hp -= damage
            print(f"Vous infligez {damage} points de dégats à {ennemy.name}.")

class Warrior(Player):
    def __init__(self, name):
        super().__init__(name)
        self.role = "guerrier"
        self.maxhp = 300
        self.hp = 300
        self.atk = 20
        self.armor = 5


class Mage(Player):
    def __init__(self, name):
        super().__init__(name)
        self.role = "mage"
        self.maxhp = 200
        self.hp = 200
        self.atk = 25
        self.armor = 2



class Ranger(Player):
    def __init__(self, name):
        super().__init__(name)
        self.role = "archer"
        self.maxhp = 250
        self.hp = 250
        self.atk = 30
        self.armor = 3



