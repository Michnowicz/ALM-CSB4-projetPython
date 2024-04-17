import random

def search(player, places):
    print(f"\n{player.name} fouille la zone de fond en comble.")
    for place in places:
        if place.name == player.place:
            if len(place.objects) > 0:
                random_index = random.randint(0, len(place.objects)-1)
                object = place.objects[random_index]
                player.inventory.append(object)
                del place.objects[random_index]
                print(f"{player.name} trouve {object}.")
            else:
                print(f"La zone semble vide.")



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

    except ValueError:
        print("\nCommande Inconnue. Veuillez saisir un nombre.")
        return move(player, places)



def look_inventory(player):
    print(f"\n{player.name} ({player.role})")
    print(f"  or : {player.gold}")
    print(f"  inventaire : {player.inventory}\n")