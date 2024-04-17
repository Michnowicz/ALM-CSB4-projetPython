import random
from fonctions.random_encounter import random_encounter


def search(player, places):
    roll = random.randint(1, 20)
    for place in places:
        if place.name == player.place:
                if roll < 8:
                    random_encounter(player, place)
                else:
                    print(f"\n{player.name} fouille la zone de fond en comble.")
                    if len(place.objects) > 0:
                        random_index = random.randint(0, len(place.objects)-1)
                        object = place.objects[random_index]
                        player.inventory.append(object)
                        del place.objects[random_index]
                        print(f"{player.name} trouve {object}.")
                    else:
                        print(f"\nLa zone semble vide.")


def move(player, places):
    print("\nChoisissez un lieu où se deplacer:")
    index = 1
    try:
        for place in places:
            print(f"{index} - {place.name}")
            index += 1
        choice = int(input("> "))
        if places[choice-1].name == player.place:
            print("\nVous vous trouvez déjà dans le lieu sélectionné.")
            return move(player, places)
        else:
            player.place = places[choice-1].name
            print(f"\nVous vous déplacez vers le/la {places[choice-1].name}.")
            random_encounter(player, places[choice-1])

    except ValueError:
        print("\nCommande Inconnue. Veuillez saisir un nombre.")
        return move(player, places)



def rest(player):
    if player.place == "maison" or player.place == "village":
        player.hp == player.maxhp
        print(f"\n{player.name} passe la nuit dans les lieux. Ses pv remontent à son maximum.")
    else:
        print("\nVous devez vous trouver à la maison ou au village pour vous reposer.")

def stats(player):
    print(f"\n  nom : {player.name}")
    print(f"  rôle : {player.role}")
    print(f"  niveau : {player.lvl}")
    print(f"  vie : {player.hp} / {player.maxhp}")
    print(f"  attaque : {player.atk}")
    print(f"  armure : {player.armor}")

def look_inventory(player):
    print(f"\n{player.name} ({player.role})")
    print(f"  or : {player.gold}")
    print(f"  inventaire : {player.inventory}\n")