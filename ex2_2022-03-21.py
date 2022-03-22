#Exercice 2:
#Créer une liste de 5 éléments : [1, 2, 5, 3, 4]. Ensuite, créer deux copies de cette liste, une copie en surface et une copie profonde 
#intitulée respectivement surface et profonde. Finalement, demander à l'utilisateur d'entrer un mot, modifier le 3e élément de la liste 
#«surface» et «profonde» et imprimer les trois listes à la console.

import copy 

def mod_liste():
    LISTE_1 = [1, 2, 5, 3, 4]

    surface = LISTE_1[:]
    profonde = copy.deepcopy(LISTE_1)

    mot_user = input("Entrez un mot: ")

    surface[2] = mot_user
    profonde[2] = mot_user 

    return print(LISTE_1), print(surface), print(profonde)




mod_liste()