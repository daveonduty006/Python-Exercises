#Exercice 6:
#En partant de l'exercice du système de géolocation, modifiez votre code pour que les positions en 
#DMS incluent la direction cardinale(N, S, E, W ou O) et retourne une position en DD pouvant être 
#négative. 
#Modifiez ensuite votre code pour permettre à un utilisateur de manuellement rentrer sa 
#position.


# conversion de données DMS à DD
def decimal_degrees(position):
    if position == pos_x:
        pos_deg_x, pos_min_x, pos_sec_x, pos_dir_x = position
        if pos_dir_x == "N":
            pos_dd = pos_deg_x + pos_min_x/60 + pos_sec_x/3600
        else:
            pos_dd = -(pos_deg_x + pos_min_x/60 + pos_sec_x/3600)
    else:
        pos_deg_y, pos_min_y, pos_sec_y, pos_dir_y = position
        if pos_dir_y == "E":
            pos_dd = pos_deg_y + pos_min_y/60 + pos_sec_y/3600
        else:
            pos_dd = -(pos_deg_y + pos_min_y/60 + pos_sec_y/3600)
    return pos_dd 


# entrées de l'utilisateur pour la latitude
pos_deg_x = int(input("Entrez la partie degré de la latitude en DMS de la position \n"))
pos_min_x = int(input("Entrez la partie minute de la latitude en DMS de la position \n"))
pos_sec_x = float(input("Entrez la partie seconde de la latitude en DMS de la position \n"))
pos_dir_x = input("Entrez la direction cardinale de la latitude en DMS de la position \n")
pos_x = pos_deg_x, pos_min_x, pos_sec_x, pos_dir_x

# entrées de l'utilisateur pour la longitude
pos_deg_y = int(input("Entrez la partie degré de la longitude en DMS de la position \n"))
pos_min_y = int(input("Entrez la partie minute de la longitude en DMS de la position \n"))
pos_sec_y = float(input("Entrez la partie seconde de la longitude en DMS de la position \n"))
pos_dir_y = input("Entrez la direction cardinale de la longitude en DMS de la position \n")
pos_y = pos_deg_y, pos_min_y, pos_sec_y, pos_dir_y

# positions en données DD
pos_dd_x = decimal_degrees(pos_x)
pos_dd_y = decimal_degrees(pos_y)

print(f"Latitude en DD: {pos_dd_x:.6f}") 
print(f"Longitude en DD: {pos_dd_y:.6f}")







# positions en données DMS 
#POLE_NORD_X = 81, 17, 60
#POLE_NORD_Y = -110, 47, 60
#pole_nord_dir_x = "N"
#pole_nord_dir_y = "W"
#MONTREAL_X = 45, 30, 31.9968, "N"
#MONTREAL_Y = 73, 33, 42.0048, "W"

# positions en données DD
#polenord_dd_x = decimal_degrees(POLE_NORD_X)
#polenord_dd_y = decimal_degrees(POLE_NORD_Y)



