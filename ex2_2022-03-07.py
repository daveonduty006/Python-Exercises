#Exercice 2:
#Créez un programme demandant à l'utilisateur un animal, une couleur et un lieu et retournez-lui la 
#phrase suivante: J'ai trouvé un (nom de l'animal) de couleur (nom de la couleur) dans mon lieu 
#préféré: (nom du lieu). Implémentez la fonction de sorte qu'elle ne prenne qu'un seul paramètre pour 
#représenter les trois mots de l'utilisateur.

def phrase(reponses_entrantes):
    animal, couleur, lieu = reponses_entrantes
    return (f"J'ai trouvé un {animal} de couleur {couleur} dans mon lieu "
            f"préféré: {lieu}.")
    
    
animal = input("Entrez le nom d'un animal quelconque: ")
couleur = input("Entrez le nom d'une couleur quelconque: ")
lieu = input("Entrez le nom d'un lieu quelconque: ")
reponses = animal, couleur, lieu

print(phrase(reponses))




