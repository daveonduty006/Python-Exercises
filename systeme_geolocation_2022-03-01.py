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

# conversion de données DMS à DD
def decimal_degrees(position):
    degrees, minutes, seconds = position
    return degrees + minutes / 60 + seconds / 3600

# calcul de distance entre deux points
def distance(p1_x, p1_y, p2_x, p2_y):
    return math.sqrt((p2_x-p1_x)**2+(p2_y-p1_y)**2) * 111.16 + 1000


# locations en données DMS 
POLE_NORD_X = 80, 65, 38
POLE_NORD_Y = 72, 68, 1
MONTREAL_X = 45, 50, 7
MONTREAL_Y = 73, 56, 73

# locations en données DD
polenord_dd_x = decimal_degrees(POLE_NORD_X)
polenord_dd_y = decimal_degrees(POLE_NORD_Y)
montreal_dd_x = decimal_degrees(MONTREAL_X)
montreal_dd_y = decimal_degrees(MONTREAL_Y)

print(f"Pôle Nord magnétique: {polenord_dd_x:.3f}, {polenord_dd_y:.3f}")
print(f"Montréal: {montreal_dd_x:>18.3f}, {montreal_dd_y:.3f}")
print(f"Distance: {distance(polenord_dd_x, polenord_dd_y, montreal_dd_x, montreal_dd_y):>20.3f}")

