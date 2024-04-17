import random
from classes.place import Place
from methodes.class_choice import class_choice
from methodes.main_action import main_action 
from classes.ennemies import Ennemy, Boss



# creation d'ennemis
slime = Ennemy("gluant", 50, 50, 20, 0, random.randint(0, 10), 10)
gobelin = Ennemy("gobelin", 60, 60, 20, 3, random.randint(3, 15), 15)
wolf = Ennemy("loup sauvage", 70, 70, 25, 1, random.randint(3, 15), 15)
zombie = Ennemy("zombie", 80, 80, 20, 5, random.randint(5, 25), 20)
skeleton = Ennemy("squelette", 75, 75, 23, 4, random.randint(5, 25), 20)

# création de boss
troll = Boss("troll", 230, 230, 25, 7, 100, 100)
tiamat = Boss("Tiamat", 9999, 9999, 500, 100, 10000, 10000)

# création des lieux
maison = Place("maison", [], [], [])
village = Place("village", ["bouclier en fer", "potion"], [], [])
foret = Place("forêt", ["fleur", "bâton en fer"], [slime, gobelin, wolf], [tiamat])
grotte = Place("grotte", ["vieille clé", "minerai d'or"], [gobelin, skeleton], [tiamat])
donjon = Place("donjon", ["rubis"], [skeleton, zombie, slime], [tiamat, troll])
places = [maison, village, foret, grotte, donjon]





# création du personnage
print("Comment vous appelez-vous?")
name = input("> ")
player = class_choice(name)

# actions
main_action(player, places)
