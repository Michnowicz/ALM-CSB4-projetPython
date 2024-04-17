

class Ennemy:
    def __init__(self,name,maxhp, hp, atk, armor, gold, exp):
        self.name = name
        self.maxhp = maxhp
        self.hp = hp
        self.atk = atk
        self.armor = armor
        self.gold = gold
        self.exp = exp

    def use_attack(self, player):
        print(f"{self.name} lance un attaque.")
        if player.armor - self.atk >= 0:
            dmg = 0
        else:
            dmg = self.atk - player.armor
        player.hp = player.hp - dmg
        print(f"{player.name} perd {dmg} points de vie.")


class Boss(Ennemy):
    def __init__(self, name, maxhp, hp, atk, armor, gold, exp):
        super().__init__(name, maxhp, hp, atk, armor, gold, exp)