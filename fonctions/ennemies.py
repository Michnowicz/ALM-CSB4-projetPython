

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
        if self.atk > player.armor:
            damage = self.atk - player.armor
        else:
            damage = 0
        if player.hp < damage:
            player.hp = 0
        else:
            player.hp -= damage
        print(f"{player.name} perd {damage} points de vie.")


class Boss(Ennemy):
    def __init__(self, name, maxhp, hp, atk, armor, gold, exp):
        super().__init__(name, maxhp, hp, atk, armor, gold, exp)