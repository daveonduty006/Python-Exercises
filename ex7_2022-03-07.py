#Exercice 7:
#Créer une calculatrice d'IMC demandant à l'utilisateur d'entrer sa grandeur(en mètres) et son poids(en kg). Retournez ensuite la catégorie 
#dans laquelle se trouve la personne.

# calculatrice de IMC 
def imc():
    grandeur = float(input("Entrez votre grandeur en mètres... \n"))
    poids = float(input("Entrez votre poids en kilogrammes... \n"))
    return poids / grandeur**2

# détermination de la catégorie IMC 
def categorie_imc(imc_entrant):
    categorie = ""
    if imc_entrant < 18.5:
        categorie = "Poids insuffisant"
    if imc_entrant >= 18.5:
        if imc_entrant < 25:
            categorie = "Poids normal"
    if imc_entrant >= 25:
        if imc_entrant < 30: 
            categorie = "Embonpoint"
    if imc_entrant >= 30:
        if imc_entrant < 35: 
            categorie = "Obésité classe I"
    if imc_entrant >= 35:
        if imc_entrant < 40:
            categorie = "Obésité classe II"
    if imc_entrant >= 40:
        categorie = "Obésité classe III"
    return categorie


# appel de la fonction imc
imc_obtenu = imc()

# appel de la fonction categorie_imc 
cat_imc_obtenu = categorie_imc(imc_obtenu) 

print(f"Votre catégorie IMC est: {cat_imc_obtenu}")
    

