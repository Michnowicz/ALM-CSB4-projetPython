import random
from methodes.random_encounter import random_encounter

class Player:
    def __init__(self, name):
        self.name = name
        self.place = "maison"
        self.lvl = 1
        self.exp = 0
        self.nextlvl = 50
        self.gold = 0
        self.inventory = []

    def search(self, places):
        roll = random.randint(1, 20)
        for place in places:
            if place.name == self.place:
                    if roll < 8:
                        random_encounter(self, place)
                    else:
                        if len(place.objects) > 0:
                            random_index = random.randint(0, len(place.objects)-1)
                            object = place.objects[random_index]
                            self.inventory.append(object)
                            del place.objects[random_index]
                            print(f"\n{self.name} fouille la zone de fond en comble. {self.name} trouve {object}.")
                        else:
                            print(f"\n{self.name} fouille la zone de fond en comble, mais la zone semble vide.")

    def rest(self):
        if self.place == "maison" or self.place == "village":
            self.hp == self.maxhp
            print(f"\n{self.name} passe la nuit dans les lieux. Ses pv remontent à son maximum.")
        else:
            print(f"\n{self.name} doit se trouver à la maison ou au village pour se reposer.")

    def stats(self):
        print(f"\n  nom : {self.name}")
        print(f"  rôle : {self.role}")
        print(f"  niveau : {self.lvl}")
        print(f"  vie : {self.hp} / {self.maxhp}")
        print(f"  attaque : {self.atk}")
        print(f"  armure : {self.armor}")

    def look_inventory(self):
        print(f"\n{self.name} ({self.role})")
        print(f"  or : {self.gold}")
        print(f"  inventaire : {self.inventory}\n")

    def player_attack(self, ennemy):
            if self.atk > ennemy.armor:
                damage = self.atk - ennemy.armor
            else:
                damage = 0
            if ennemy.hp < damage:
                ennemy.hp = 0
            else:
                ennemy.hp -= damage
            print(f"{self.name} inflige {damage} points de dégats à {ennemy.name}.")

    def level_up(self):
        print(f"\nfélicitations, {self.name} passe de niveau. Les statistiques de {self.name} augmentent.")
        print(" max hp + 20\n atk + 5")
        self.lvl += 1
        self.maxhp += 20
        self.hp = self.maxhp
        self.atk += 5

    def flee(self):
        roll = random.randint(1, 20)
        if roll > 10:
            print(f"\n{self.name} réussi à fuir.")
            return True
        else:
            print(f"\n{self.name} tente de fuir mais en vain.")
            return False

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


