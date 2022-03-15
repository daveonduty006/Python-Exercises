#Exercice 8:
#Écrire une fonction prenant deux nombres et vérifiant si le premier nombre est plus petit que le deuxième, 
#si ce n'est pas le cas, les retourner dans l'ordre inverse. Ex.: fonction(4, 3) retournerait 3 et, ensuite, 
#4.

def ordre(nb1, nb2):
    if nb1 < nb2:
        ordre = f"Ordre = {nb1}, {nb2}"
    else:
        ordre = f"Ordre = {nb2}, {nb1}"
    return ordre


n1 = int(input("Entrez un premier nombre: "))
n2 = int(input("Entrez un second nombre: "))

print(ordre(n1, n2))