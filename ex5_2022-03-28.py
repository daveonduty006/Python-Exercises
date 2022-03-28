#Exercice 5:
#Offrir à l'utilisateur d'entrer un nom de fichier et un nombre illimité de 
#nombres positifs, tant et aussi longtemps qu'il ne rentre pas un nombre négatif. 
#Ajouter les nombres entrés par l'utilisateur à une liste en excluant le nombre négatif. 
#Ensuite, écrire les résultats suivants dans le fichier nommé par l'utilisateur:
#La liste en ordre croissant
#La liste en ordre décroissant
#Le maximum
#Le minimum
#La moyenne de la liste
#La médiane (la valeur à la position centrale si la longueur de la liste est impaire et 
#la moyenne des deux valeurs centrales si paire)
#Ex: 1, 2, 3, 5, 4. Médiane = 3.
#Ex: 1, 2, 3, 4, 5, 6. Médiane = 3.5
#Le mode (l'occurrence la plus fréquente s'il y a lieu. Si chaque entrée est unique, 
#inscrire que le mode = none)
#Ex: 1, 2, 2, 2, 3, 4, 3, 4. La mode = 3

def control():
    file_name, int_list = user_data()
    file_write(file_name, int_list)
    return


def user_data():
    file_name = input("Entrez le nom de votre futur fichier: ")

    int_list = []
    n = 1
    while n > 0:
        n = int(input("Entrez un nombre entier positif: "))
        if n > 0:
            int_list.append(n)

    return file_name, int_list


def file_write(name_of_file, list_of_integers):

    ordre_croissant = f"ordre croissant: {sorted(list_of_integers)}\n"

    ordre_decroissant = f"ordre décroissant: {sorted(list_of_integers, reverse=True)}\n"

    maximum = f"maximum: {max(list_of_integers)}\n"

    minimum = f"minimum: {min(list_of_integers)}\n"

    moyenne = f"moyenne: {sum(list_of_integers)/len(list_of_integers)}\n"

    if len(list_of_integers) % 2 == 1:
        o_croissant = sorted(list_of_integers)
        index = int((len(list_of_integers)-1)/2) 
        mediane = f"médiane: {o_croissant[index]}\n"
    else: 
        o_croissant = sorted(list_of_integers)
        half_index1 = int((len(list_of_integers))/2)
        half_index2 = int(((len(list_of_integers))/2)+1)
        mediane = f"médiane: {(o_croissant[half_index1]+o_croissant[half_index2])/2}\n"

    mode = f"mode: {max(set(list_of_integers), key=list_of_integers.count)}\n"

    stats = [ordre_croissant, ordre_decroissant, maximum, minimum, moyenne, \
             mediane, mode]

    f = open(f"{name_of_file}.txt", "w", encoding="utf8")

    for stat in stats:
        f.write(stat)

    f.close()

    return 



control() 
