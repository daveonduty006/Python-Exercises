# Vous travaillez sur un système de géolocation s'intitulant à la recherche du pôle Nord utilisant 
# des coordonnées sous la forme degrés minutes secondes (DMS).

# Pour faciliter l'utilisation du système, on vous demande de créer un court programme permettant de 
# convertir ces données sous la forme de degrés décimaux (DD).

# De plus, considérant que le but de l'application est d'indiquer la distance des usagers du pôle 
# Nord magnétique en plus d'indiquer leur position, on vous demande d'ajouter à votre programme une 
# fonction permettant de calculer cette distance.

# Versionner votre travail avec GitHub desktop et publié le sur votre profil GitHub Web une fois 
# terminé.

import math

def dms_to_DD(deg_dms, min_dms, sec_dms):
    deg_dd = float(deg_dms)
    min_dd = min_dms/60
    sec_dd = sec_dms/3600
    return deg_dd+min_dd+sec_dd
# distance de quel nord? # deux lignes vides entre définition de fonction
def distance_du_nord(coord_lat, coord_long):
    distance_lat = (86-coord_lat)**2
    distance_long = (172-coord_long)**2
    return math.sqrt(distance_lat+distance_long)*111.16

# définir le degré-minute-seconde de quoi (dans ce cas, degré-minute-seconde DMS)
# définir quelle ville est représentée par ces données
DEG_LAT = 35
MIN_LAT = 39
SEC_LAT = 10.08

DEG_LONG = 139
MIN_LONG = 50
SEC_LONG = 21.84

mes_coord_lat = dms_to_DD(DEG_LAT, MIN_LAT, SEC_LAT)
mes_coord_long = dms_to_DD(DEG_LONG, MIN_LONG, SEC_LONG)

print(distance_du_nord(mes_coord_lat, mes_coord_long))

