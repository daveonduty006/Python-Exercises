#Créez un programme demandant à un utilisateur d'entrer sa date de fête 
# et retournez-lui sa saison de naissance s'il est né dans l'hémisphère Nord. 
# (Vous pouvez assumer que les équinoxes et solstices ont lieu le 21 du mois.)

def saison_naissance(jour_fete_entrant, mois_fete_entrant):
        if mois_fete_entrant == 3:
            if jour_fete_entrant < 21:
                saison_fete = "hiver"
        elif mois_fete_entrant == 12:
            if jour_fete_entrant >= 21:
                saison_fete = "hiver"
        elif mois_fete_entrant <= 2:
            if mois_fete_entrant >= 1:
                saison_fete = "hiver"

        elif mois_fete_entrant == 6:
           if jour_fete_entrant < 21:
                saison_fete = "printemps"
        elif mois_fete_entrant == 3:
            if jour_fete_entrant >= 21:
                saison_fete = "printemps"
        elif mois_fete_entrant <= 5:
            if mois_fete_entrant >= 4:
                saison_fete = "printemps"

        elif mois_fete_entrant == 9:
            if jour_fete_entrant < 21:
                saison_fete = "été"
        elif mois_fete_entrant == 6:
            if jour_fete_entrant >= 21:
                saison_fete = "été"
        elif mois_fete_entrant <= 8:
            if mois_fete_entrant >= 7:
                saison_fete = "été"

        elif mois_fete_entrant == 12:
            if jour_fete_entrant < 21:
                saison_fete = "automne"
        elif mois_fete_entrant == 9:
            if jour_fete_entrant >= 21:
                saison_fete = "automne"
        elif mois_fete_entrant <= 11:
            if mois_fete_entrant >= 10:
                saison_fete = "automne"
        return saison_fete


jour_fete = int(input("Entrez votre jour de fête..."))
mois_fete = int(input("Entrez votre mois de fête en chiffres..."))

saison_naissance_fete = saison_naissance(jour_fete, mois_fete)

print(f"Vous êtes né en {saison_naissance_fete}!")

