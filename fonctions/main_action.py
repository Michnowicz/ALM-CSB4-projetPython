from fonctions.actions import search, move, look_inventory


def main_action(player, places):
    try:
        print(f"\nVous vous trouvez dans le lieu suivant: {player.place}.")
        print("Choisissez une action:\n1 - fouiller les lieux\n2 - se deplacer\n3 - se reposer\n4 - voir l'inventaire\n5 - quitter le jeu")
        choice = int(input("> "))
        if choice != 5:
            if choice == 1:
                search(player, places)
            elif choice == 2:
                move(player, places)
            elif choice == 3:
                print('se repose\n')
            elif choice == 4:
                look_inventory(player)
            else:
                print("\nCommande erronée. Merci d'entrer un nombre entre 1 et 5")
            return main_action(player, places)
        else:
            print("Bonne journée.\n")
    except ValueError:
        print("\nCommande erronée. Merci d'entrer un nombre.")
        return main_action(player, places)
    except KeyboardInterrupt:
        print("\nBonne journée.\n")