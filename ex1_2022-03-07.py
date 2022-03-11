#Exercice 1:
#Créez un programme demandant à un utilisateur d'entrer un entier et retournez-lui le carré. Si le 
#nombre est positif, retournez-lui aussi la racine carrée.

from math import sqrt

def modification_s(nombre):
    if nombre > 0:
        return nombre**2, float(f"{sqrt(nombre):.3f}")
    else:
        return nombre**2 


rep = int(input("Entrez un nombre entier: "))

print(modification_s(rep))



        
