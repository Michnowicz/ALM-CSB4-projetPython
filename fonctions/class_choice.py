from fonctions.personnage import Warrior, Mage, Ranger


def class_choice(name):
    print("\nChoisissez parmis une des 3 classes: (Insérez un nombre)\n1 - Guerrier\n2 - Mage\n3 - Archer")
    try:
        choice = int(input("> "))
        if choice == 1:
            chosen_class = Warrior(name)
            return chosen_class
        elif choice == 2:
            chosen_class = Mage(name)
            return chosen_class
        elif choice == 3:
            chosen_class = Ranger(name)
            return chosen_class
        else:
            print("Commande erronée. Choisissez parmis une des 3 classes en insérant un nombre entre 1 et 3 dans le terminal.\n")
            return class_choice()
    
    except ValueError:
        print("Commande erronée. Merci d'entrer un nombre.\n")
        return class_choice()

