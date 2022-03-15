#Exercice 4:
#Écrire un programme avec une fonction prennant 2 floats et retournant leur addition, soustraction et 
#division. Les résultats des additions doivent avoir au plus 1 chiffre après la virgule, la soustraction 2 
#chiffres après la virgule et la division 3 chiffres après la virgule.

def operations(nb1, nb2):
    add = f"{nb1+nb2:.1f}"
    sous = f"{nb1-nb2:.2f}"
    div = f"{nb1/nb2:.3f}"
    return add, sous, div 


n1 = float(input("Entrez un premier nombre décimal: "))
n2 = float(input("Entrez un second nombre décimal: "))

print(operations(n1, n2))


