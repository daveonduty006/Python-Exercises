#Exercice 3:
#Créer une fonction permettant de faire la puissance d'un nombre pour ensuite en faire la division. 
#Votre fonction doit prendre de 1 à 3 paramètres, le premier paramètre étant la base, le deuxième 
#paramètre étant l'exposant et le troisième paramètre étant la division. Si aucun exposant n'est 
#donné, faites le carré. Si aucun diviseur n'est donné, n'effectuez pas de division.

def operations(nb, exp=2, div=1):
    return (nb**exp)/div


CHIFFRE_DE_BASE = 3
EXPOSANT = 3
DIVISEUR = 2

print(operations(CHIFFRE_DE_BASE, EXPOSANT, DIVISEUR))





    