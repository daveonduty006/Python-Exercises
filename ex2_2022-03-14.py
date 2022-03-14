#Exercice 2:
#Créer un programme prenant en paramètre les conditions météorologiques suivantes:
#   L'état du ciel(Ensoleillé, nuageux ou éclaircies), les précipitations (aucune, pluie, neige ou verglas), la vitesse des vents en km/h et la 
#   température en C.
#Ensuite, affichez à l'écran un message d'alerte météorologique si les conditions suivantes sont respectées:
#   Il y a des précipitations et les vents sont supérieurs à 30 km/h
#   Il y a du verglas
#   Il fait soleil, mais les vents sont supérieurs à 70km/h ou les températures sont supérieures à 30C ou inférieures à -25C.
#   Il fait nuageux et les vents sont supérieurs à 50km/h.
#   Il fait nuageux et les vents sont supérieurs à 30km/h, mais la température est supérieure à 25C ou inférieure à -20C
#   Il neige et la température est inférieure à -25C.
#   Il fait ensoleillé, il n'y a pas de vent et la température est supérieure à 25C.
#Permettez à un utilisateur de rentrer les conditions météorologiques à l'aide d'un menu et assurez-vous qu'il soit impossible de rentrer des 
#conditions météorologiques qui ne font pas de sens.

def alerte_meteo(ciel, prec, vent, temp):
    message = "Bonne journée!"
    if (prec == 2 or prec == 3 or prec == 4) and vent > 30:
        message = "!!!ALERTE MÉTÉOROLOGIQUE!!!"
    elif prec == 4:
        message = "!!!ALERTE MÉTÉOROLOGIQUE!!!" 
    elif ciel == 1 and (vent > 70 or (temp < -25 or temp > 30)): 
        message = "!!!ALERTE MÉTÉOROLOGIQUE!!!"  
    elif ciel == 2 and vent > 50:
        message = "!!!ALERTE MÉTÉOROLOGIQUE!!!"
    elif ciel == 2 and vent > 30 and (temp < -20 or temp > 25):
        message = "!!!ALERTE MÉTÉOROLOGIQUE!!!"
    elif prec == 3 and temp < 25:
        message = "!!!ALERTE MÉTÉOROLOGIQUE!!!"  
    elif ciel == 1 and vent == 0 and temp > 25:
        message = "!!!ALERTE MÉTÉOROLOGIQUE!!!"
    return message 


ciel_rep = int(input(f"Entrez l'état du ciel: \n"
                     f"1. Ensoleillé \n"
                     f"2. Nuageux \n"
                     f"3. Éclaircie \n"))
if 1 <= ciel_rep <= 3:
    prec_rep = int(input(f"Entrez l'état des précipitations: \n"
                     f"1. Aucune \n"
                     f"2. Pluie \n"
                     f"3. Neige \n"
                     f"4. Verglas \n"))
    if 1 <= prec_rep <= 4:
        vent_rep = int(input("Entrez la vitesse des vents en km/h: \n"))
        temp_rep = int(input("Entrez la température en celsius: \n"))
        print(alerte_meteo(ciel_rep, prec_rep, vent_rep, temp_rep))
    else:
        print("Valeur d'état des précipitations invalide \n "
              "Fin du programme")
else:
    print("Valeur de l'état du ciel invalide \n "
          "Fin du programme")




