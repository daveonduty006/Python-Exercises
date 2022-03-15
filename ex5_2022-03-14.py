#Exercice 5:
#Écrire un programme prenant l'année de naissance et lui retournant sa génération. Vous pouvez utiliser la 
#source suivante: https://www.eurecia.com/blog/generations-x-y-z-sont-elles/

def generation(annee_naissance):
    if 1946 <= annee_naissance < 1965:
        gen = "Baby Boomer"
    elif 1965 <= annee_naissance < 1980:
        gen = "Gen X"
    elif 1980 <= annee_naissance < 2000: 
        gen = "Gen Y"
    elif 2000 <= annee_naissance:
        gen = "Gen Z"
    else: 
        gen = "(année de naissance non-gérée)"
    return f"Vous êtes un {gen}"

naissance = int(input("Entrez votre année de naissance: "))
print(generation(naissance))