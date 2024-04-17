from methodes.random_encounter import random_encounter


def move(player, places):
    print("\nChoisissez un lieu où se deplacer:")
    index = 1
    try:
        for place in places:
            print(f"{index} - {place.name}")
            index += 1
        choice = int(input("> "))
        if places[choice-1].name == player.place:
            print(f"\n{player.name} se trouve déjà dans le lieu sélectionné.")
            return move(player, places)
        else:
            player.place = places[choice-1].name
            print(f"\n{player.name} se déplace vers le/la {places[choice-1].name}.")
            random_encounter(player, places[choice-1])

    except ValueError:
        print("\nCommande Inconnue. Veuillez saisir un nombre.")
        return move(player, places)