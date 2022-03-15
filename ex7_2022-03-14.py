#Exercice 7:
#Écrire un programme demandant à l'utilisateur de rentrer un nombre entre 1 et 20, vérifier si ce dernier 
#est bel et bien entre 1 et 20 et indiquez-lui si son nombre est un nombre premier (ayant aucun autre facteur 
#entier que 1 et lui-même)

def primalite(nombre):
    message = ""
    if not(1 <= nombre <= 20):
        message = "Votre nombre n'est pas entre 1 et 20"
    else: 
        if nombre == 2 or nombre == 3 or nombre == 5 or nombre == 7 or nombre == 11 or \
           nombre == 13 or nombre == 17 or nombre == 19:
            message = f"Votre nombre, {nombre}, est un nombre premier"
        else:
            message = f"Votre nombre, {nombre}, n'est pas un nombre premier"
    return message 


nb = int(input("Entrez un nombre entre 1 et 20: "))

print(primalite(nb))



