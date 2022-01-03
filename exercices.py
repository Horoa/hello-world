from math import pi

#1. Écrire un programme qui, à partir de la saisie d'un rayon et d'une hauteur, calcule le volume d'un cône droit.

def findVolume(radius,height):
    return pi*radius*radius*height/3.0
  
#2. Une boucle while : entrez un prix HT (entrez o pour terminer) et affichez sa valeur TTC.

def findPriceTTC():
    priceWT = float(input("Price without taxe (0 tp end) ?"))
    while priceWT > 0:
        print("Price with taxes : { :.2f}\n".format(priceWT * 1.2))
        priceWT = float(input("Price without taxe (0 tp end) ?"))

#3  Une autre boucle while : calculez la somme d'une suite de nombres positifs ou nuls. Comptez combien il y avait de données et combien étaient supérieures à 100.
#   Entrer un nombre inférieur ou égal à 0 indique la fin de la suite.
