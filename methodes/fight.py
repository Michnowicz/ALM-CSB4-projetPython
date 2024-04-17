
def fight(player, ennemy):
    print(f"\n{player.name} -> pv: {player.hp}/{player.maxhp}")
    print(f"Que voulez-vous faire?")
    print("1 - attaquer\n2 - fuir")
    try:
        choice = int(input("> "))
        flee_flag = False

        if choice == 1:
            player.player_attack(ennemy)
            if ennemy.hp > 0:
                ennemy.use_attack(player)
        elif choice == 2:
            flee_flag = player.flee()
            if flee_flag == False:
                ennemy.use_attack(player)
        else:
            print("\nCommande erronée. Merci d'entrer un nombre entre 1 et 2")

        if flee_flag == True:
            print(f"\n{player.name} réussi à fuir.")
        else:
            if player.hp > 0 and ennemy.hp > 0:
                return fight(player, ennemy)
            else:
                if ennemy.hp == 0:
                    print(f"\n{player.name} a vaincu {ennemy.name}. {player.name} recoit {ennemy.gold} pièces d'or et {ennemy.exp} points d'expériences.")
                    player.gold += ennemy.gold
                    player.exp += ennemy.exp
                    ennemy.hp = ennemy.maxhp
                    if player.exp >= player.nextlvl:
                        player.level_up()
                        player.exp -= player.nextlvl
                        player.nextlvl += 30
                elif player.hp == 0:
                    print(f"\n{player.name} n'a plus de points de vie.")

    except ValueError:
        print("\nCommande erronée. Merci d'entrer un nombre.")
        return fight(player, ennemy)