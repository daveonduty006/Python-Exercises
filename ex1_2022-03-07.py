#Créez un programme demandant à un utilisateur d'entrer un entier et retournez-lui le carré. Si le nombre 
#est positif, retournez-lui aussi la racine carrée.

import math 

def operations(nb_entrant):
    if nb_entrant > 0:
        return nb_entrant**2, math.sqrt(nb_entrant)
    else:
        return nb_entrant**2 


nb = int(input("Entrez votre nombre"))
if nb > 0:
    carre, racine_carre = operations(nb)
    print(carre, racine_carre)
else:
    print(operations(nb))



