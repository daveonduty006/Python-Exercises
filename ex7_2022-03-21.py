#Exercice 7:
#Offrir à l'utilisateur d'entrer un nom de fichier et 5 nombres. Ensuite, créer une liste avec les
#nombres et imprimer les résultats suivant dans le fichier nommé par l'utilisateur:
#Afficher en ordre croissant
#Afficher en ordre décroissant
#Afficher le maximum
#Afficher le minimum
#Afficher chaque nombre puissance lui-même dans l'ordre initial entré par l'utilisateur ex: pow(a, a)
#Afficher la moyenne de la liste
#Afficher la médianne

def file_create():
    file_name = input("Entrez le nom du fichier: ")

    n1 = int(input("\nEntrez un premier nombre entier: "))
    n2 = int(input("\nEntrez un second nombre entier: "))
    n3 = int(input("\nEntrez un troisième nombre entier: "))
    n4 = int(input("\nEntrez un quatrième nombre entier: "))
    n5 = int(input("\nEntrez un cinquième nombre entier: "))

    numbers_list = [n1, n2, n3, n4, n5]

    #file path pour travail à la maison
    f = open("C:\\Users\\David\\Documents\\Github Exercises\\"+file_name+".txt", "w")
    #
    #file path pour travail à l'école 
    #f = open("??????????????????????????????????????????????"+file_name+".txt", "w")
    # 

    #la fonction sorted ne modifie pas l'ordre initial de la liste suite à son 
    #utilisation
    ordre_croi = sorted(numbers_list)
    ordre_decroi = sorted(numbers_list, reverse=True)
    #
    maximum = max(numbers_list)
    minimum = min(numbers_list)

    #copie superficielle de la liste numbers_list 
    powers_list = numbers_list[:]
    #
    powers_list[0] = pow(powers_list[0], powers_list[0])
    powers_list[1] = pow(powers_list[1], powers_list[1])
    powers_list[2] = pow(powers_list[2], powers_list[2])
    powers_list[3] = pow(powers_list[3], powers_list[3])
    powers_list[4] = pow(powers_list[4], powers_list[4])

    moyenne = sum(numbers_list) / len(numbers_list)

    #rappel: la médianne est le chiffre à la position centrale d'une série de chiffres 
    #dont le nombre d'éléments est impair et dont les chiffres sont en ordre croissant
    medianne = ordre_croi[2]
    #

    f.write(f"liste originale: {numbers_list}\n")
    f.write(f"en ordre croisant: {ordre_croi}\n")
    f.write(f"en ordre décroissant: {ordre_decroi}\n")
    f.write(f"plus grand nombre: {maximum}\n")
    f.write(f"plus petit nombre: {minimum}\n")
    f.write(f"n à la puissance n: {powers_list}\n")
    f.write(f"moyenne: {moyenne}\n")
    f.write(f"médianne: {medianne}\n")

    f.close() 

    return 




file_create() 