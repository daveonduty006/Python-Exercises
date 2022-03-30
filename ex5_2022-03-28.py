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

# module regroupant des sous-fonctions pour des calculs de statistiques 
def statistiques():
    # sous-fonction récoltant les données de l'utilisateur
    def user_input():
        file_name = input("Entrez le nom du fichier: ")

        user_list = []
        exit = False 
        while not exit:
            user_number = int(input("Entrez un entier positif: "))
            if user_number >= 0:
                user_list.append(user_number)
            else:
                exit = True

        return file_name, user_list
    # sous-fonction rangeant la liste en ordre croissant
    def ascending_order(user_list):
        sorted_list = user_list[:]
        for i in range(len(sorted_list)-1):
            min = sorted_list[i]
            pos = i
            for j in range(i, len(sorted_list)):
                if sorted_list[j] < min:
                    min = sorted_list[j] 
                    pos = j
            sorted_list[i], sorted_list[pos] = sorted_list[pos], sorted_list[i]

        return sorted_list
    # sous-fonction rangeant la liste en ordre décroissant
    def descending_order(user_list):
        sorted_list = ascending_order(user_list)

        reversed_list = sorted_list[::-1]

        return reversed_list 
    # sous-fonction obtenant le plus grand nombre dans la liste
    def max_number(user_list):

        return ascending_order(user_list)[-1]
    # sous-fonction obtenant le plus petit nombre dans la liste
    def min_number(user_list):

        return ascending_order(user_list)[0]
    # sous-fonction obtenant la moyenne des nombres de la liste
    def average(user_list):
        sum = 0 
        for n in user_list:
            sum += n

        return sum / len(user_list)
    # sous-fonction obtenant la médianne de la liste
    def median(user_list):
        sorted_list = ascending_order(user_list)

        i = len(sorted_list) // 2

        if len(sorted_list) % 2 == 0:
            return (sorted_list[i]+sorted_list[i-1]) / 2
        else:
            return sorted_list[i]
    # sous-fonction obtenant le mode de la liste 
    def mode(user_list):
        counts = {}
        for n in user_list:
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1
    
        max_count = max(counts.values()) 
        if max_count >= 2:
            keys_with_max_count = [k for k,v in counts.items() if v == max_count]
            return keys_with_max_count
        else:
            return None 

    file_name, user_list = user_input()
    stats = []
    stats.append(f"Liste initiale: {user_list}\n")
    stats.append(f"Ordre croissant: {ascending_order(user_list)}\n")
    stats.append(f"Ordre décroissant: {descending_order(user_list)}\n")
    stats.append(f"Nombre maximal: {max_number(user_list)}\n")
    stats.append(f"Nombre minimal: {min_number(user_list)}\n")
    stats.append(f"Moyenne: {average(user_list)}\n")
    stats.append(f"Médianne: {median(user_list)}\n")
    stats.append(f"Mode: {mode(user_list)}\n")

    f = open(f"{file_name}.txt", "w", encoding="utf8")
    for stat in stats:
        f.write(stat)
    f.close()


statistiques() 


