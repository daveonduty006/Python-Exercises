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
    prog, math, os = liste_lignes[0], liste_lignes[2], liste_lignes[4]  
    dico = {prog : liste_lignes[1], math : liste_lignes[3], os : liste_lignes[5]}
    return dico

# fonction de l'exercise 3 modifiée selon l'énoncé de l'exercise 5 
def menu_user(dico_entrant):
    #récupère toutes mes clés et valeurs d'association dans 2 listes différentes   
    liste_de_cles = list(dico_entrant.keys())
    liste_de_vals = list(dico_entrant.values())
    #
    selection_repo = int(input("Quel répertoire voulez-vous consulter? \n"
                               "1. Vos cours \n"
                               "2. Vos enseignants \n"
                               "Choisissez un répertoire: "))
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
            print("Votre sélection de cours est invalide")    
    elif selection_repo == 2:
        selection_prof = input("\nEntrez le nom complet de votre enseignant avec majuscules: ")
        #ajustement pour le \n présent dans la compilation du dictionnaire à partir du fichier .txt 
        selection_prof1 = selection_prof + "\n"
        #
        if selection_prof1 in liste_de_vals:
            print(f"\n{selection_prof} est l'un/une de vos enseignant(e)s")
        else:
            print(f"\n{selection_prof} n'est pas l'un/une de vos enseignant(e)s")
    else: 
        print("Choix de répertoire invalide")
    return


dico_cours = remplissage_dico()
menu_user(dico_cours)