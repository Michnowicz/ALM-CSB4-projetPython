from methodes.move import move

def main_action(player, places):
    try:
        if player.hp > 0:
            print(f"\n{player.name} se trouve dans le lieu suivant: {player.place}.")
            print("Choisissez une action:\n1 - fouiller les lieux\n2 - se deplacer\n3 - se reposer\n4 - voir les stats\n5 - voir l'inventaire\n6 - quitter le jeu")
            choice = int(input("> "))
            if choice != 6:
                if choice == 1:
                    player.search(places)
                elif choice == 2:
                    move(player, places)
                elif choice == 3:
                    player.rest()
                elif choice == 4:
                    player.stats()
                elif choice == 5:
                    player.look_inventory()
                else:
                    print("\nCommande erronée. Merci d'entrer un nombre entre 1 et 6.")
                return main_action(player, places)
            else:
                print("Bonne journée.\n")
        else:
            print("Game Over.")
    except ValueError:
        print("\nCommande erronée. Merci d'entrer un nombre.")
        return main_action(player, places)
    except KeyboardInterrupt:
        print("\nBonne journée.\n")