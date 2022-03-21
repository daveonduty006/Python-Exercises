#Exercice 2:
#Créer une liste de 5 éléments : [1, 2, 5, 3, 4]. Ensuite, créer deux copies de cette liste, une copie en surface et une copie profonde 
#intitulée respectivement surface et profonde. Finalement, demander à l'utilisateur d'entrer un mot, modifier le 3e élément de la liste 
#«surface» et «profonde» et imprimer les trois listes à la console.

import copy 

def mod_liste():
    LISTE_1 = [1, 2, 5, 3, 4]
    copie_surface_liste = LISTE_1[:]
    copie_profonde_liste = copy.deepcopy(LISTE_1)
    mot_user = input("Entrez un mot: ")
    copie_surface_liste[2] = mot_user
    copie_profonde_liste[2] = mot_user 
    return print(LISTE_1, copie_surface_liste, copie_profonde_liste)


mod_liste()