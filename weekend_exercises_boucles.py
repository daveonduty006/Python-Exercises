#Algorithme de Seuil 
#Aujourd'hui un appartement vaut 100 000 euros.
#Sa valeur augmente de 1% chaque année.
#étape 1: écrire un programme pour connaître sa valeur au bout de 10 ans.
#étape 2: écrire un programme pour savoir au bout de combien d'années sa valeur 
#         aura doublé. 

#APPART = 100000

#for annee in range(1,11):
#    APPART = APPART * 1.01

#print(APPART)

#annee = 0
#while APPART < 200000:
#    APPART = APPART * 1.01
#    annee = annee + 1

#print(annee)


#5.4.1 Boucles de base
#Soit la liste ["vache", "souris", "levure", "bacterie"]. 
#Affichez l'ensemble des éléments de cette liste (un élément par ligne) 
#de trois manières différentes (deux avec for et une avec while).

#liste = ["vache", "souris", "levure", "bacterie"]

#for animal in liste:
#    print(animal)

#for i in range(len(liste)):
#    print(liste[i])

#i = 0
#while i < len(liste):
#    print(liste[i])
#    i = i + 1


#5.4.2 Boucle et jours de la semaine
#Constituez une liste semaine contenant les 7 jours de la semaine.
#Écrivez une série d'instructions affichant les jours de la semaine 
#(en utilisant une boucle for), ainsi qu'une autre série d'instructions affichant 
#les jours du week-end (en utilisant une boucle while).

#semaine = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]

#for jour in semaine[0:5]:
#    print(f"{jour} ", end="")

#i = -2
#while i <= -1:
#    print(f"{semaine[i]} ", end="")
#    i = i + 1


#5.4.3 Nombres de 1 à 10 sur une ligne
#Avec une boucle, affichez les nombres de 1 à 10 sur une seule ligne.
#Conseil : n'hésitez pas à relire le début du chapitre 3 Affichage qui discute de la 
#fonction print().

#for n in range(11):
#    if n == 0:
#        continue
#    else:
#        print(f"{n} ", end="")


#5.4.4 Nombres pairs et impairs
#Soit impairs la liste de nombres [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]. 
#Écrivez un programme qui, à partir de la liste impairs, construit une liste pairs 
#dans laquelle tous les éléments de impairs sont incrémentés de 1.

#n_impairs = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
#n_pairs = []

#for i in range(len(n_impairs)):
#    n_pairs.append(n_impairs[i]+1)

#print(n_pairs)


#5.4.5 Calcul de la moyenne ???
#Voici les notes d'un étudiant [14, 9, 6, 8, 12]. Calculez la moyenne de ces notes. 
#Utilisez l'écriture formatée pour afficher la valeur de la moyenne avec deux 
#décimales.

#notes = [14, 9, 6, 8, 12]


#5.4.6 Produit de nombres consécutifs
#Avez les fonctions list() et range(), créez la liste entiers contenant les nombres
#entiers pairs de 2 à 20 inclus.
#Calculez ensuite le produit des nombres consécutifs deux à deux de entiers en 
#utilisant une boucle. Exemple pour les premières itérations :
#8
#24
#48
#[...]

#n_pairs = list(range(2,21,2))

#i = 0
#for n in n_pairs:
#    if n != 20:
#        print(n*n_pairs[i+1])
#        i = i + 1


#5.4.7 Triangle
#Créez un script qui dessine un triangle comme celui-ci:
#*
#**
#***
#****
#*****
#******
#*******
#********
#*********
#**********

#triangle = ""

#icone = "*"
#while len(triangle) < 10:
#    triangle = icone 
#    print(triangle)
#    icone = icone + "*"


#5.4.8 Triangle inversé
#Créez un script qui dessine un triangle comme celui-ci:
#**********
#*********
#********
#*******
#******
#*****
#****
#***
#**
#*

#triangle = "**********"

#icone = "*"
#MUL = 10
#while len(triangle) > 0:
#    print(triangle)
#    MUL = MUL - 1
#    triangle = icone * MUL 


#5.4.9 Triangle gauche
#Créez un script qui dessine un triangle comme celui-ci :
#         *
#        **
#       ***
#      ****
#     *****
#    ******
#   *******
#  ********
# *********
#**********

#triangle = ""

#icone = "*"
#while triangle != "**********":
#    triangle = f"{icone:>10s}" 
#    print(triangle)
#    icone = icone + "*"


#5.4.10 Pyramide
#Créez un script qui dessine une pyramide comme celle-ci:
#         *
#        ***
#       *****
#      *******
#     *********
#    ***********
#   *************
#  ***************
# *****************
#*******************
#Essayez de faire évoluer votre script pour dessiner la pyramide à partir d'un 
#nombre arbitraire de lignes N. 
#Vous pourrez demander à l'utilisateur le nombre de lignes de la pyramide avec 
#les instructions suivantes qui utilisent la fonction input():
#reponse = input("Entrez un nombre de lignes (entier positif): ")
#N = int(reponse)

#reponse = int(input("Entrez un nombre de lignes (entier positif): "))

#triangle = ""

#icone = "*"
#for l in range(reponse):
#    triangle = f"{icone:^{reponse*2-1}s}"
#    print(triangle)
#    icone = icone + "**"


#5.4.11 Parcours de matrice
#Imaginons que l'on souhaite parcourir tous les éléments d'une matrice carrée, 
#c'est-à-dire d'une matrice qui est constituée d'autant de lignes que de colonnes.
#Créez un script qui parcourt chaque élément de la matrice et qui affiche le 
#numéro de ligne et de colonne uniquement avec des boucles for.
#Pour une matrice 2×2, l'affichage attendu est :
#ligne colonne
#   1    1
#   1    2
#   2    1
#   2    2
#Attention à bien respecter l'alignement des chiffres qui doit être justifié à 
#droite sur 4 caractères. Testez pour une matrice 3×3.

#print("ligne colonne")
#for l in range(3):
#    l = l + 1
#    for c in range(3):
#        c = c + 1
#        print(f"{l:>4d}", end=""), print(f"{c:>5d}")




    


































