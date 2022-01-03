from math import pi

#1. Écrire un programme qui, à partir de la saisie d'un rayon et d'une hauteur, calcule le volume d'un cône droit.

def findVolume(radius,height):
    return pi*radius*radius*height/3.0
  
#2. Une boucle while : entrez un prix HT (entrez o pour terminer) et affichez sa valeur TTC.

def findPriceTTC():
    priceWT = float(input("Price without taxe (0 to end) ?"))
    while priceWT > 0:
        print("Price with taxes : { :.2f}\n".format(priceWT * 1.2))
        priceWT = float(input("Price without taxe (0 to end) ?"))

#3  Une autre boucle while : calculez la somme d'une suite de nombres positifs ou nuls. Comptez combien il y avait de données et combien étaient supérieures à 100.
#   Entrer un nombre inférieur ou égal à 0 indique la fin de la suite.

def sumOfASerie():
    numberInput = float(input("Number of the serie (0 to end) ?"))
    totalOfNumberHigherThanOneHundred = 0
    totalOfNumber = 0
    sumTotal = 0
       
    while numberInput > 0 :
        if numberInput >= 100 :
            totalOfNumberHigherThanOneHundred +=1
        totalOfNumber +=1
        sumTotal += numberInput
        numberInput = float(input("Number of the serie (0 to end) ?"))
        
    print("The sum total of the serie is " + str(sumTotal) + " there was " + str(totalOfNumber) + " numbers and " + str(totalOfNumberHigherThanOneHundred) + " numbers higher than 100")

    
#4 L'utilisateur donne un entier positif n et le programme affiche PAIR s'il est divisible par 2, IMPAIR sinon

def isOddOrEven():
    numberInput = int(input("Take a number"))
    if numberInput%2 == 0 :
        print( str(numberInput) + " is even")
    else :
        print( str(numberInput) + " is odd")
    
    
#5 L'utilisateur donne un entier positif et le programme annonce combien de fois de suite cet entier est divisible par 2.

def numberOfPossibleHalves():
    numberInput = int(input("Take a number"))
    numberOfHalves = 0
    while numberInput != 0 and numberInput%2==0 :
        numberInput/=2
        numberOfHalves+=1
    print("You can divide your number " + str(numberOfHalves) + " times")
        
    
