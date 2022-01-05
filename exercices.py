from math import pi

# https://python.developpez.com/cours/apprendre-python-3/?page=exercices-corriges
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
    print("You can divide your number " + str(numberOfHalves) + " times\n")
        
    
#6 L'utilisateur donne un entier supérieur à 1 et le programme affiche, s'il y en a, tous ses diviseurs propres sans répétition ainsi que leur nombre. S'il n'y en a pas, il indique qu'il est premier.

def findCommonDivisor():
    numberInput = int(input("Take a number"))
    if numberInput == 0 :
        print("0 has all integers other than 0 as a common divisor.\n")
    elif numberInput == 1 :
        print("1 has no common divisor but it isn't a prime number.\n")
    else :
        while numberInput < 2 : 
            numberInput=int(input("please choose a number greater than 1"))
        listOfCommonDivisor = []
        for i in range(2, numberInput) :
            if numberInput%i == 0 :
                listOfCommonDivisor.append(i)
        if len(listOfCommonDivisor) == 0 :
            print( str(numberInput) + " has no common divisor, it's a prime number")
        else :
            print ( str(numberInput) + " has " + str(len(listOfCommonDivisor)) + " common divisor : " + str(listOfCommonDivisor))
            
#7 Écrire un programme qui approxime par défaut la valeur de la constante mathématique e, pour n assez grand(56)

def findE():
    numberInput = 0
    while numberInput < 1 :
        numberInput = int(input("Number for the sum"))
    sum = 0
    for i in range(numberInput+1) : 
        sum += 1.0/factoriel(i)
    print("The value e is approximatively equals to " + str(sum))
    
def factoriel(number) :
    if number == 0 : 
        return 1
    return number*factoriel(number-1)


#8  Un gardien de phare va aux toilettes cinq fois par jour. Or les WC sont au rez-de-chaussée…
#   Écrire une procédure (donc sans return) hauteurParcourue qui reçoit deux paramètres, le nombre de marches du phare et la hauteur de chaque marche (en cm), et qui affiche :
#   Pour x marches de y cm, il parcourt z.zz m par semaine.

def hauteurParcourue(nombreMarche, hauteurMarche):
    print("For " + str(nombreMarche) + " steps of " + str(hauteurMarche) + "cm, he walks " + str(nombreMarche*hauteurMarche*2*7*5/100) + "m per week")

   

