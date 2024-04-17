import random
from fonctions.place import Place
from fonctions.character import Warrior
from fonctions.class_choice import class_choice
from fonctions.main_action import main_action 
from fonctions.ennemies import Ennemy, Boss
from fonctions.random_encounter import random_encounter

# creation d'ennemis
slime = Ennemy("gluant", 100, 100, 20, 0, random.randint(0, 10), 10)
gobelin = Ennemy("gobelin", 120, 120, 20, 3, random.randint(3, 15), 15)
wolf = Ennemy("loup sauvage", 130, 130, 25, 1, random.randint(3, 15), 15)
zombie = Ennemy("zombie", 150, 150, 20, 5, random.randint(5, 25), 20)
skeleton = Ennemy("squelette", 140, 140, 23, 4, random.randint(5, 25), 20)

# création de boss
troll = Boss("troll", 230, 230, 25, 7, 100, 100)
tiamat = Boss("Tiamat", 9999, 9999, 500, 100, 10000, 10000)

# création des lieux
maison = Place("maison", [], [], [])
village = Place("village", ["bouclier en fer", "potion"], [slime, gobelin], [])
foret = Place("forêt", ["fleur", "bâton en fer"], [slime, gobelin, wolf], [tiamat])
grotte = Place("grotte", ["vieille clé", "minerai d'or"], [gobelin, skeleton], [tiamat])
donjon = Place("donjon", ["rubis"], [skeleton, zombie, slime], [troll, tiamat])
places = [maison, village, foret, grotte, donjon]


#perso 
player = Warrior("Julio")





#test
random_encounter(player, grotte)
