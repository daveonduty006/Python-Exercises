#Créez un programme demandant à un utilisateur d'entrer sa date de fête 
#et retournez-lui sa saison de naissance s'il est né dans l'hémisphère Nord. 
#(Vous pouvez assumer que les équinoxes et solstices ont lieu le 21 du mois.)

# !!!EXERCISE EXPRESSÉMENT FAIT SANS UTILISATION D'OPÉRATEURS LOGIQUES!!!

# détermination de la saison à la naissance
def saison_naissance(jour_fete_entrant, mois_fete_entrant):
        if mois_fete_entrant == 3:
            if jour_fete_entrant < 21:
                saison_fete = "hiver"
            else:
                saison_fete = "printemps"
        if mois_fete_entrant == 6:
            if jour_fete_entrant < 21:
                saison_fete = "printemps"
            else:
                saison_fete = "été"
        if mois_fete_entrant == 9:
            if jour_fete_entrant < 21: 
                saison_fete = "été"
            else: 
                saison_fete = "automne"
        if mois_fete_entrant == 12:
            if jour_fete_entrant < 21:
                saison_fete = "automne"
            else:
                saison_fete = "hiver"
        if mois_fete_entrant == 1:
            saison_fete = "hiver"
        if mois_fete_entrant == 2:
            saison_fete = "hiver"
        if mois_fete_entrant == 4:
            saison_fete = "printemps"
        if mois_fete_entrant == 5:
            saison_fete = "printemps"
        if mois_fete_entrant == 7:
            saison_fete = "été"
        if mois_fete_entrant == 8:
            saison_fete = "été"
        if mois_fete_entrant == 10:
            saison_fete = "automne"
        if mois_fete_entrant == 11:
            saison_fete = "automne"
        return saison_fete


# question initiale pour démarrer le programme
rep = input("Êtes-vous né dans l'hémisphère nord? ")

# confirmation de l'hémisphère et entrées de l'utilisateur
if rep == "oui":
    jour_fete = int(input("Entrez le jour votre fête: "))
    mois_fete = int(input("Entrez le mois votre fête en chiffre(s): "))
    saison_naissance_fete = saison_naissance(jour_fete, mois_fete)
    print(f"Vous êtes né en {saison_naissance_fete}!")
else: 
    print("fin du programme")


