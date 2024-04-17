import random
from methodes.fight import fight

def random_encounter(player, place):
    roll = random.randint(1, 20)
    #print(f"resultat : {roll}")
    if len(place.ennemies) != 0:
        if roll == 1:
            if len(place.bosses) > 0:
                ennemy = place.bosses[0]
                print(f"\n{player.name} rencontre {ennemy.name}.")
                fight(player, ennemy)
            else:
                ennemy = place.ennemies[random.randint(0, len(place.ennemies) - 1)]
                print(f"\n{player.name} rencontre un {ennemy.name}.")
                fight(player, ennemy)
        elif roll > 1 and roll <= 6:
            if len(place.bosses) == 2:
                print(f"\n{player.name} rencontre {ennemy.name}.")
                ennemy = place.bosses[1]
                fight(player, ennemy)
            else:
                ennemy = place.ennemies[random.randint(0, len(place.ennemies) - 1)]
                print(f"\n{player.name} rencontre un {ennemy.name}.")
                fight(player, ennemy)
        elif roll > 6 and roll < 15:
            ennemy = place.ennemies[random.randint(0, len(place.ennemies) - 1)]
            print(f"\n{player.name} rencontre un {ennemy.name}.")
            fight(player, ennemy)
