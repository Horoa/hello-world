def main():
    print("My compilator")
    text=input("The chain you want to enter in your compilator")
    compilateur(text)

def compilateur(text):
    #first step, separate, everything in list (i guess ?)
    listCompil = list(text.split(" "))
    print(listCompil)
    #second step, reduce the list (with some flex effect)
    #last step, execute the list (wtf does that mean ?)


compilateur("Bonjour je m'appelle Horoan")
