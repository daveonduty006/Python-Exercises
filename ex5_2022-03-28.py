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

# fonction controllant le flux du programme 
def control():
    file_name, int_list = user_data()
    file_write(file_name, int_list)
    return

# fonction récoltant les retours de l'utilisateur
def user_data():
    file_name = input("Entrez le nom de votre futur fichier: ")

    int_list = []
    n = 1
    while n > 0:
        n = int(input("Entrez un nombre entier positif: "))
        if n > 0:
            int_list.append(n)

    return file_name, int_list

# fonction ajoutant les statistiques dans un fichier txt via une boucle "for"
# (le calcul des stats les plus simples à obtenir est également effectuée ici)
def file_write(name_of_file, list_of_integers):
    ascending_order = f"ordre croissant: {sorted(list_of_integers)}\n"

    descending_order = (f"ordre décroissant: "
                        f"{sorted(list_of_integers, reverse=True)}\n")

    maximum = f"maximum: {max(list_of_integers)}\n"

    minimum = f"minimum: {min(list_of_integers)}\n"

    average = f"moyenne: {sum(list_of_integers)/len(list_of_integers)}\n"

    median = calculate_median(list_of_integers) 
    median = f"médiane: {median}\n"
 
    mode = calculate_mode(list_of_integers)
    mode = f"mode: {mode}\n"

    stats = [ascending_order, descending_order, maximum, minimum, average, \
             median, mode]

    f = open(f"{name_of_file}.txt", "w", encoding="utf8")
    for stat in stats:
        f.write(stat)
    f.close()

    return 

# fonction calculant la médiane de la liste de positifs 
def calculate_median(list_of_integers):
    sorted_list = sorted(list_of_integers)
    index = len(list_of_integers) // 2 
    if len(sorted_list) % 2 == 1:
        return sorted_list[index]
    else: 
        return (sorted_list[index-1] + sorted_list[index]) / 2

# fonction calculant le mode de la liste de positifs avec méthode dictionnaire
def calculate_mode(list_of_integers):
    dico = {}
    i = 0
    while i <= (len(list_of_integers)-1):
        new_entry = {list_of_integers[i] : 0}
        dico.update(new_entry)
        i = i + 1

    i = 0
    while i <= (len(list_of_integers)-1):
        dico[list_of_integers[i]] += 1 
        i = i + 1

    if max(dico.values()) > 1:
        mode = max(dico, key=dico.get)
    else:
        mode = "none"
    
    return mode 


# appel de la fonction "control"
control() 

    

    

   #if len(list_of_integers) != len(set(list_of_integers)):
   #     mode = max(set(list_of_integers), key=list_of_integers.count)
   #     return mode 
   # else:
   #     mode = "none"
   #     return mode 

