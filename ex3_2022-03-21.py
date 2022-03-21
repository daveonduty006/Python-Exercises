#Exercice 3:
#Créer un dictionnaire possédant les cours que vous suivez cette session et leur enseignant respectif. Par exemple:
#Keven Presseau-St-Laurent - Concepts de programmation 1
#Ensuite, afficher un menu à la console présentant les 5 cours et offrant à l'utilisateur d'en sélectionner 1. Lorsque l'utilisateur à fait sa 
#sélection, afficher le nom de l'enseignant et le nom du cours à l'écran.

def menu_cours(): 
    dico_cours = {"prog" : "Keven Presseau-St-Laurent", "math" : "Emma Parent Senez", "os" : "Jean-Pierre Fiset"}
    selection_user = int(input("Voici le menu de vos cours: \n"
                               "1. Concepts de Programmation 1 \n"
                               "2. Logique Mathématique pour l'Informatique \n"
                               "3. Systèmes d'Exploitation \n"
                               "Choisissez un cours: "))
    if selection_user == 1:
        print(f"{dico_cours['prog']} - Concepts de Programmation 1")
    elif selection_user == 2:
        print(f"{dico_cours['math']} - Logique Mathématique pour l'Informatique") 
    elif selection_user == 3:
        print(f"{dico_cours['os']} - Systèmes d'Exploitation")     
    else:
        print("Votre sélection est invalide")           
    return


menu_cours()
