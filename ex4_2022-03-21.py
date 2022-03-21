#Exercice 4:
#En se basant sur l'exercice 3, créer un fichier bdd.txt fonctionnant comme une base de données et remplir le dictionnaire à partir de ce 
#fichier. Pour vous faciliter la tâche, vous pouvez écrire les informations de la manière suivante:
#Nom de cours 1
#Nom de prof 1
#Nom de cours 2
#....

def remplissage_dico():
    dico = {}
    file = open("bdd.txt", "r", encoding="utf8")
    liste_lignes = file.readlines()
    cours1 = str(liste_lignes[0])
    prof1 = str(liste_lignes[1])
    cours2 = str(liste_lignes[2])
    prof2 = str(liste_lignes[3])
    cours3 = str(liste_lignes[4])
    prof3 = str(liste_lignes[5])
    dico = {"cours1" : "prof1", "cours2" : "prof2", "cours3" : "prof3"}
    return print(dico["cours1"])


remplissage_dico()

    



