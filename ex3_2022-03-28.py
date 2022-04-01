#Exercice 3:
#Créer une fonction prenant une liste de nombres, d'une taille indéterminée, 
#et permettant de les trier en ordre croissant. 
#(Vous ne pouvez pas utiliser sort() ou sorted(), vous devez vous-même 
#implémenter l'algorithme)

def compil_list():
    l = []
    user_input = 1
    while user_input != 0:
        user_input = int(input("Entrez un nombre que vous voulez ajouter dans " \
                               "la liste (entrez 0 quand vous avez terminé): "))
        if user_input != 0:
            l.append(user_input)
    return l


def sort_list(l):
    new_l = []
    while l:
        minimum = l[0]
        for n in l:
            if n < minimum:
                minimum = n
        new_l.append(minimum)
        l.remove(minimum)
    return print(new_l)



list_of_numbers = compil_list()
sort_list(list_of_numbers)

