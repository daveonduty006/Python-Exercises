#Exercice 6:
#Offrir à l'utilisateur une nouvelle option au menu lui permettant d'ajouter un cours et un nom 
#d'enseignant à la base de données de l'exercice 4. Une fois les données utilisateurs entrées, 
#ajouter les informations à la fin du document bdd.txt

# fonction remplissant un dictionnaire à partir d'une base de données
def remplissage_dico():
    dico = {}
    fichier = open("bdd.txt", "r", encoding="utf8")
    liste_lignes = fichier.readlines()
    fichier.close()
    dico = {liste_lignes[0] : liste_lignes[1], liste_lignes[2] : liste_lignes[3], \
            liste_lignes[4] : liste_lignes[5]}
    return dico

# fonction ajoutant de l'information dans la base de données
def mise_a_jour_dico(cours_entrant, enseignant_entrant):
    fichier = open("bdd.txt", "a", encoding="utf8")
    fichier.write(f"\n{cours_entrant}\n{enseignant_entrant}")
    fichier.close()

# fonction représentant les menus offerts à l'utilisateur 
def menu_user(dico_entrant):
    #récupère toutes mes clés et valeurs d'association dans 2 listes différentes   
    liste_de_cles = list(dico_entrant.keys())
    liste_de_vals = list(dico_entrant.values())
    #
    selection_repo = int(input("En quoi êtes-vous intéressé? \n"
                               "1. Vos cours \n"
                               "2. Vos enseignants \n"
                               "3. Ajout d'un cours/enseignant \n"))
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
    elif selection_repo == 3: 
        nouveau_cours = input("\nEntrez le nom du nouveau cours: ")
        nouveau_enseignant = input("\nEntrez le nom de votre nouveau(elle) enseignant(e): ")
        mise_a_jour_dico(nouveau_cours, nouveau_enseignant)
    else: 
        print("Choix invalide")
    return


dico_cours = remplissage_dico()
menu_user(dico_cours)