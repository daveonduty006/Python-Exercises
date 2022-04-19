#Exercice 1:
#À partir de votre exercice sur les données DMS (exercice du mardi, semaine du 
#28 février et exercice 6, semaine du 07 mars), créez un programme permettant 
#de recevoir une liste de données(en DMS) dans un fichier data.txt d'une 
#taille indéterminée et trouvez la position la plus proche du Pôle-Nord.
#Pour tester l'exécution de votre programme vous devez créer une liste ayant 
#les positions en DMS d'au moins 10 villes et les placer dans le fichier data.txt.

def closest_to_north_pole():
    def data_compil():
        f = open("data.txt", "r", encoding="utf8")
        data_list = f.readlines()
        f.close()

        for i in (len(data_list)-1):
            if data_list





        cities_dms_val = {}


        return data_list




    data_list = data_compil()
    return print(data_list)



closest_to_north_pole()