#Exercice 5:
#En se basant sur l'exercice 4, modifier le menu utilisateur en y ajoutant une 
#option lui permettant de faire une recherche d'enseignant. Vérifier si l'enseignant
#entré par l'utilisateur est présent dans votre liste de cours et indiquer le 
#résultat à la console.

# fonction de l'exercise 4 avec valeur de retour
def remplissage_dico():
    dico = {}
    fichier = open("bdd.txt", "r", encoding="utf8")
    liste_lignes = fichier.readlines()
    fichier.close()

    dico = {liste_lignes[0] : liste_lignes[1], liste_lignes[2] : liste_lignes[3], \
            liste_lignes[4] : liste_lignes[5]}

    return dico


# fonction navigation dans les menus 
def menu_user(dico_entrant):
    ##récupère toutes mes clés et valeurs d'association dans 2 listes différentes   
    liste_de_cles = list(dico_entrant.keys())
    liste_de_vals = list(dico_entrant.values())
    ##
    
    selection_repo = int(input("En quoi êtes-vous intéressé? \n"
                               "1. Vos cours \n"
                               "2. Vos enseignants \n"
                               "Choisissez une option: "))

    if selection_repo == 1:
        selection_cours = int(input("\nVoici le menu de vos cours: \n"
                                    "1. Concepts de Programmation 1 \n"
                                    "2. Logique Mathématique pour l'Informatique \n"
                                    "3. Systèmes d'Exploitation \n"
                                    "Choisissez un cours: "))
        if selection_cours == 1:
            print(f"\n{liste_de_cles[0]} - {dico_entrant[liste_de_cles[0]]}")
        elif selection_cours == 2:
            print(f"\n{liste_de_cles[1]} - {dico_entrant[liste_de_cles[1]]}")
        elif selection_cours == 3:
            print(f"\n{liste_de_cles[2]} - {dico_entrant[liste_de_cles[2]]}")
        else:
            print("\nVotre sélection de cours est invalide")   

    elif selection_repo == 2:
        selection_prof = input("\nEntrez le nom complet de votre enseignant avec majuscules: ")
        ##ajustement pour le \n présent dans les éléments du dictionnaire
        selection_prof1 = selection_prof + " \n"
        ##
        if selection_prof1 in liste_de_vals:
            index = liste_de_vals.index(selection_prof1)
            print(f"\n{selection_prof} est l'un/une de vos enseignant(e)s \n"
                  f"Son cours est {liste_de_cles[index]}")
        else:
            print(f"\n{selection_prof} n'est pas l'un/une de vos enseignant(e)s")

    else: 
        print("\nChoix invalide")

    return




dico_cours = remplissage_dico()
menu_user(dico_cours)