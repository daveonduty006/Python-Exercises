#Exercice 6:
#Écrire un programme demandant un entier à un utilisateur et lui retournant sa parité. Ex.: Le nombre «4» 
#est paire.

def parite():
    nombre = int(input("Entrez un nombre entier: "))
    if nombre % 2 == 0: 
        pair = "Nombre pair"
    else:
        pair = "Nombre impair"
    return pair 


print(parite()) 