from fonctions.place import Place
from fonctions.class_choice import class_choice
from fonctions.main_action import main_action 



# lieux
maison = Place("maison", [])
village = Place("village", ["bouclier en fer", "potion"])
foret = Place("forêt", ["fleur", "bâton en fer"])
grotte = Place("grotte", ["vieille clé", "minerai d'or"])
donjon = Place("donjon", ["rubis"])

places = [maison, village, foret, grotte, donjon]


# création du personnage
print("Comment vous appelez-vous?")
name = input("> ")
player = class_choice(name)

# actions
main_action(player, places)
