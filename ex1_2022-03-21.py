#Exercice 1:
#Créer une liste contenant tous les nombres premiers entre 2 et 20. Ensuite, demander à l'utilisateur d'écrire un nombre entre 2 et 20 
#(bien vérifier si c'est le cas) et vérifier si ce nombre est prime à l'aide de votre liste en affichant le résultat à la console.

def verification_prime():
    N_PREMIER = [2, 3, 5, 7, 11, 13, 17, 19]
    user_chiffre = int(input("Entrez un nombre entre 2 et 20: "))
    if 2 <= user_chiffre <= 20: 
        if user_chiffre in N_PREMIER:
            print("Votre chiffre est prime")
        else:
            print("Votre chiffre n'est pas prime")
    else: 
        print("Votre chiffre est invalide") 
    return 


verification_prime()