#Exercice 4:
#En se basant sur l'exercice 3, créer un fichier bdd.txt fonctionnant comme une base de données et remplir le dictionnaire à partir de ce 
#fichier. Pour vous faciliter la tâche, vous pouvez écrire les informations de la manière suivante:
#Nom de cours 1
#Nom de prof 1
#Nom de cours 2
#....

def remplissage_dico():
    dico = {}
    fichier = open("bdd.txt", "r", encoding="utf8")
    liste_lignes = fichier.readlines()
    fichier.close()
    prog, math, os = liste_lignes[0], liste_lignes[2], liste_lignes[4]  
    dico = {prog : liste_lignes[1], math : liste_lignes[3], os : liste_lignes[5]}
    return print(f"{prog} : {dico[prog]}"), print(f"{math} : {dico[math]}"), \
           print(f"{os} : {dico[os]}")


remplissage_dico()

    



