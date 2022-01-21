from math import pi
from random import randint

# https://python.developpez.com/cours/apprendre-python-3/?page=exercices-corriges
#1. Écrire un programme qui, à partir de la saisie d'un rayon et d'une hauteur, calcule le volume d'un cône droit.

def findVolume(radius,height):
    return pi*radius*radius*height/3.0

def exercice1():
    print("radius = " + str(findVolume(float(input("radius?")),float(input("height?")))))
  
#2. Une boucle while : entrez un prix HT (entrez o pour terminer) et affichez sa valeur TTC.

def findPriceTTC():
    prixHT = float(input("Prix HT (0 pour terminer) ?"))
    while prixHT > 0:
        print("Prix TTC : " + str(prixHT * 1.2) + "€\n")
        prixHT = float(input("Prix HT (0 pour terminer) ?"))

def exercice2():
    findPriceTTC()
        
        
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

def exercice3():
    sumOfASerie()
    
#4 L'utilisateur donne un entier positif n et le programme affiche PAIR s'il est divisible par 2, IMPAIR sinon

def isOddOrEven():
    numberInput = int(input("Take a number"))
    if numberInput%2 == 0 :
        print( str(numberInput) + " is even")
    else :
        print( str(numberInput) + " is odd")

def exercice4():
    isOddOrEven()
    
#5 L'utilisateur donne un entier positif et le programme annonce combien de fois de suite cet entier est divisible par 2.

def numberOfPossibleHalves():
    numberInput = int(input("Take a number"))
    numberOfHalves = 0
    while numberInput != 0 and numberInput%2==0 :
        numberInput/=2
        numberOfHalves+=1
    print("You can divide your number " + str(numberOfHalves) + " times\n")

def exercice5():
    numberOfPossibleHalves()
    
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
            
def exercice6():
    findCommonDivisor()
            
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

def exercice7():
    findE()

#8  Un gardien de phare va aux toilettes cinq fois par jour. Or les WC sont au rez-de-chaussée…
#   Écrire une procédure (donc sans return) hauteurParcourue qui reçoit deux paramètres, le nombre de marches du phare et la hauteur de chaque marche (en cm), et qui affiche :
#   Pour x marches de y cm, il parcourt z.zz m par semaine.

def hauteurParcourue(nombreMarche, hauteurMarche):
    print("For " + str(nombreMarche) + " steps of " + str(hauteurMarche) + "cm, he walks " + str(nombreMarche*hauteurMarche*2*7*5/100) + "m per week")

def exercice8():
    hauteurParcourue(int(input("number of step?")),float(input("height of the step?")))
   
#9  Un permis de chasse à points remplace désormais le permis de chasse traditionnel. Chaque chasseur possède au départ un capital de 100 points. S'il tue une poule, il perd 1 point, 3 points pour un chien, 5 points pour une vache et 10 points pour un ami. Le permis coûte 200 euros.
#   Écrire une fonction amende qui reçoit le nombre de victimes du chasseur et qui renvoie la somme due.
#   Utilisez cette fonction dans un programme principal qui saisit le nombre de victimes et qui affiche la somme que le chasseur doit débourser.

def calculateFine(countKillChicken, countKillDog, countKillCow, countKillHunter) :
    print(str(((countKillChicken+countKillDog*3+countKillCow*5+countKillHunter*10)//100)*200)+ "€")

def exercice9():
    calculateFine(int(input("Chicken killed?")),int(input("Dog killed?")),int(input("Cow killed?")),int(input("Hunter killed?")))
    
#10 Je suis ligoté sur les rails en gare d'Arras. Écrire un programme qui affiche un tableau me permettant de connaître l'heure à laquelle je serai déchiqueté par le train parti de la gare du Nord à 9 h (il y a 170 km entre la gare du Nord et Arras).
#   Le tableau prédira les différentes heures possibles pour toutes les vitesses de 100 km/h à 300 km/h, par pas de 10 km/h, les résultats étant arrondis à la minute inférieure.
#       Écrire une procédure tchacatchac qui reçoit la vitesse du train et qui affiche l'heure du drame ;
#       Écrire le programme principal qui affiche le tableau demandé.

def tchacatchac(trainSpeed):
    hour = 170//trainSpeed
    min = int(170%trainSpeed*60/trainSpeed)
    minTen = '0' if min<10 else ''
    print (str(trainSpeed) + "km/h => " + str(9+hour) + "h" + minTen + str(min))

def stationTab():
    for vitesse in range(100,310,10):
        tchacatchac(vitesse)
        
def exercice10():
    stationTab()
    
#11 Un programme principal saisit une chaîne d'ADN valide et une séquence d'ADN valide (valide signifie qu'elles ne sont pas vides et sont formées exclusivement d'une combinaison arbitraire de "a", "t", "g" ou "c").
#   Écrire une fonction valide qui renvoie vrai si la saisie est valide, faux sinon.
#   Écrire une fonction saisie qui effectue une saisie valide et renvoie la valeur saisie sous forme d'une chaîne de caractères.
#   Écrire une fonction proportion qui reçoit deux arguments, la chaîne et la séquence et qui retourne la proportion de séquence dans la chaîne (c'est-à-dire son nombre d'occurrences).
#   Le programme principal appelle la fonction saisie pour la chaîne et pour la séquence et affiche le résultat.

def valide(chaine):   
    if chaine == "":
        return False
    for letter in chaine :
        if letter != "a" and letter != "t" and letter != "g" and letter != "c" :
            return False
    return True

def proportion(sequence, chain):
    return 100*chain.count(sequence)/len(chain)
    
def exercice11():
    chain = str(input("your chain ?"))
    while not(valide(chain)):
        chain = str(input("your chain isn't valide "))
    sequence = str(input("your sequence ?"))
    while (not(valide(sequence)) and len(sequence) != 2) :
        sequence = str(input("your sequence isn't valide "))
    print ("There is " + str(proportion(sequence, chain)) + "% of " + sequence + " in your chain")

#12 Il s'agit d'écrire, d'une part, un programme principal et, d'autre part, une fonction utilisée dans le programme principal.
#   La fonction listAleaInt(n, a, b) retourne une liste de n entiers aléatoires dans [a .. b] en utilisant la fonction randint(a, b) du module random.
#   ns le programme principal :
#   construire la liste en appelant la fonction listAleaInt() ;
#   calculer l'index de la case qui contient le minimum ;
#   échangez le premier élément du tableau avec son minimum.

def listAleaInt(n, a, b):
    list = []
    for i in range(n):
        list.append(randint(a,b))
    return list

def posOfTheMin(list):
    min = list[0]
    minPos = 0
    for i in range(1,len(list)) :
        if (min>list[i]):
            minPos=i
            min = list[i]
    return minPos

def exercice12():
    n = int(input("size of your list ?"))
    while n<1:
        n = int(input("your number must be >1"))
    a = int(input("first number ?"))
    b = int(input("second number ?"))
    while b<a:
        b = int(input("your number must be >a"))
    list = listAleaInt(n,a,b)
    print(list)
    posMin = posOfTheMin(list)
    print(posMin)
    list[0],list[posMin]=list[posMin],list[0]
    print(list)
    
#13 Comme précédemment, il s'agit d'écrire, d'une part, un programme principal et, d'autre part, une fonction utilisée dans le programme principal.
#   La fonction listAleaFloat(n) retourne une liste de n flottants aléatoires en utilisant la fonction random() du module random.
#   Dans le programme principal :
#   saisir un entier n dans l'intervalle : [2 .. 100] ;
#   construire la liste en appelant la fonction listAleaFloat() ;
#   afficher l'amplitude du tableau (écart entre sa plus grande et sa plus petite valeur) ;
#   afficher la moyenne du tableau.
    
def exercice13():
    n = int(input("size of your list ?"))
    while n<2 or n>100:
        n = int(input("your number must be in [2,100]"))
    list = [random() for i in range(n)]
    print(list)
    sumTotal=0
    min = list[0]
    max = list[0]
    for number in list :
        sumTotal += number
        if number>max:
            max = number
        if number<min:
            min = number
    print("The min is " + str(min) + ", the max is " + str(max) + ", the amplitude is " + str(max-min) + ", and the mean is " + str(sumTotal/n))
    
#14 Fonction renvoyant plusieurs valeurs sous forme d'un tuple.
#   Écrire une fonction minMaxMoy() qui reçoit une liste d'entiers et qui renvoie le minimum, le maximum et la moyenne de cette liste. Le programme principal appellera cette fonction avec la liste : [10, 18, 14, 20, 12, 16].

def minMaxMoy(list):
    n = len(list)
    print(list)
    sumTotal=0
    min = list[0]
    max = list[0]
    for number in list :
        sumTotal += number
        if number>max:
            max = number
        if number<min:
            min = number
    print("The min is " + str(min) + ", the max is " + str(max) + ", and the mean is " + str(sumTotal/n))

def exercice14():
    minMaxMoy([10, 18, 14, 20, 12, 16])
    

    
#15 Saisir un entier entre 1 et 3999 (pourquoi cette limitation ?). L'afficher en nombre romain.

def romain(n):
    millier=["","M","MM","MMM"]
    centaine=["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
    dizaine=["","X","X","XXX","XL","L","LX","LXX","LXXX","XC"]
    unite=["","I","II","III","IV","V","VI","VII","VIII","IX"]

    number = str(n)
    if n<1000 :
        number = "0" + number
    if n<100 :
        number = "0" + number
    if n<10 :
        number = "0" + number
    print(str(n) + " = " , end = '')
    print(millier[int(number[0])], end = '')
    print(centaine[int(number[1])], end = '')
    print(dizaine[int(number[2])], end = '')
    print(unite[int(number[3])])
    
def exercice15():
    n = int(input("the number you want in roman ?"))
    while n<1 or n>4000:
        n = int(input("your number must be in [1,3999]"))
    romain(n)

def exercice15test():
    for i in range(4000) :
        romain(i)
        
#16 Améliorer le script précédent en utilisant la fonction zip().

def exercice17():
    n = int(input("size of your list ?"))
    while n<2 or n>100:
        n = int(input("your number must be in [2,100]"))
    list = listAleaInt(n,0,500)
    print(list)
    listTest = [False for i in range(500)]
    duplicate = False
    for i in range(n):
        if listTest[list[i]] == False :
            listTest[list[i]] = True
        else :
            duplicate = True
    print(duplicate)

def twoDice(n):
    list=[]
    for i in range(1,7):
        if 7>(n-i)>0 :
            list.append([i,n-i])
    return list
    
    
def exercice19():
    n = int(input("number to get with 2 dices ?"))
    while n<2 or n>12:
        n = int(input("your number must be in [2,12]"))
    list=twoDice(n)
    print(list)

def addFirstElementList(n,list):
    listWithFirst = []
    for i in list :
        listWithFirst.append([n,*i])
    return listWithFirst
            
def threeDice(n):
    list=[]
    for i in range(1,7):
        if  13>(n-i)>1:
            list=[*list,*addFirstElementList(i,twoDice(n-i))]
    print(list)
            
            
def exercice20():
    n = int(input("number to get with 3 dices ?"))
    while n<3 or n>18:
        n = int(input("your number must be in [3,18]"))
    threeDice(n)
    
    def exercice21():
    numberOfDice= int(input("number of dices ?"))
    while numberOfDice<0:
        somme = int(input("your number must be <0"))
    somme = int(input("number to get with " + str(numberOfDice) + " dices ?"))
    while somme<numberOfDice or somme>(6*numberOfDice):
        somme = int(input("your number must be in ["+ str(numberOfDice) + "," + str(6*numberOfDice)+ "]"))
    

def exercice21():
    numberOfDice= int(input("number of dices ?"))
    while numberOfDice<0:
        somme = int(input("your number must be <0"))
    somme = int(input("number to get with " + str(numberOfDice) + " dices ?"))
    while somme<numberOfDice or somme>(6*numberOfDice):
        somme = int(input("your number must be in ["+ str(numberOfDice) + "," + str(6*numberOfDice)+ "]"))
    print(numberDice(numberOfDice,somme))

def numberDice(numberOfDice,somme):
    if numberOfDice==1:
        return [7-somme]
    list=[]
    for valueDice in range(1,7):
        if  ((numberOfDice+1)*6)>(somme-valueDice)>numberOfDice:
            return [*list,*addFirstElementList(valueDice,numberDice(numberOfDice-1,somme-valueDice))]
        

            
