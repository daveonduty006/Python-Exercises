#Exercice 9 (En équipe):
#Partie 1:

#Créer une calculatrice permettant de calculer combien couteraient en 2021, un article acheté en 1970. Utilisez le IPC moyenne annuelle de ces 
#années respectives. Les données sont disponibles ici: https://www150.statcan.gc.ca/n1/pub/71-607-x/2018016/cpilg-ipcgl-fra.htm
#Vous pouvez comparer vos résultats ici: https://www.banqueducanada.ca/taux/renseignements-complementaires/feuille-de-calcul-de-linflation/

#Partie 2:
#En utilisant le salaire minimum de ces années respectives, affichez le résultat en nombre d'heures de travail. Vous pouvez utiliser le salaire 
#minimum fédéral ou provincial, tant que vous restez constant.

#Partie 3:
#Ensuite, comparez le nombre d'heures de travail nécessaire pour payer l'article au salaire minimum de 1970 en 2021 en fonction du coût de 1970
#ajusté pour l'inflation et en fonction de son coût en 2021. Faites attention d'utiliser le bon salaire minimum dans vos calculs, pour le 
#nombre d'heures en 1970, utilisez le salaire de 1970, alors que pour le nombre d'heures en 2021, utilisez le salaire minimum de 2021.



def main():
    prix_influe, prix_original = prix1970_to_prix2021()
    nb_heures_2021, nb_heures_1970 = nb_heures_travail(prix_influe, prix_original)
    nb_heures_ajuste = nb_heures_sal_influs(prix_original, nb_heures_2021, nb_heures_1970)

def prix1970_to_prix2021():
    IPC_MOY_ANNU_1970, IPC_MOY_ANNU_2021 = 20.2, 138.2
    prix_1970 = float(input("Entrez le prix d'un article en 1970: "))
    prix_2021 = IPC_MOY_ANNU_2021 / IPC_MOY_ANNU_1970 * prix_1970
    print(f"Prix de l'article en 2021: {prix_2021:.2f}$")
    return prix_2021, prix_1970

def nb_heures_travail(prix_en_2021, prix_en_1970):
    SAL_MIN_1970, SAL_MIN_2021 = 1.65, 15.0
    heures_requis_1970 = prix_en_1970 / SAL_MIN_1970
    heures_requis_2021 = prix_en_2021 / SAL_MIN_2021
    print(f"Nombre d'heures de travail requis pour l'achat d'un article "
          f"de {prix_en_1970}$ en 1970: {heures_requis_1970:.1f} \n"
          f"Nombre d'heures de travail requis pour l'achat d'un article "
          f"de {prix_en_2021:.2f}$ en 2021: {heures_requis_2021:.1f}")
    return heures_requis_2021, heures_requis_1970

def nb_heures_sal_influs(prix_en_2021, heures_req_2021, heures_req_1970):
    SAL_MIN_1970, SAL_MIN_2021 = 1.65, 15.0


main()





