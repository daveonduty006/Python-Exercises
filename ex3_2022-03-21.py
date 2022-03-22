#Exercice 3:
#Créer un dictionnaire possédant les cours que vous suivez cette session et leur enseignant respectif. Par exemple:
#Keven Presseau-St-Laurent - Concepts de programmation 1
#Ensuite, afficher un menu à la console présentant vos cours et offrant à l'utilisateur d'en sélectionner 1. Lorsque l'utilisateur à fait sa 
#sélection, afficher le nom de l'enseignant et le nom du cours à l'écran.

def menu_user(dico_entrant): 
    selection_user = int(input("Voici le menu de vos cours: \n"
                               "1. Concepts de Programmation 1 \n"
                               "2. Logique Mathématique pour l'Informatique \n"
                               "3. Systèmes d'Exploitation \n"
                               "Choisissez un cours: "))
                         
    liste_de_cles = list(dico_entrant.keys())

    if selection_user == 1:
        print(f"\n{liste_de_cles[0]} - {dico_entrant[liste_de_cles[0]]}")

    elif selection_user == 2:
        print(f"\n{liste_de_cles[1]} - {dico_entrant[liste_de_cles[1]]}")

    elif selection_user == 3:
        print(f"\n{liste_de_cles[2]} - {dico_entrant[liste_de_cles[2]]}")    

    else:
        print("\nVotre sélection est invalide")     
              
    return




dico_cours = {"Keven Presseau-St-Laurent" : "Concepts de Programmation 1", \
              "Emma Parent Senez" : "Logique Mathématique pour l'Informatique", \
              "Jean-Pierre Fiset" : "Systèmes d'Exploitation"}
              
menu_user(dico_cours)
