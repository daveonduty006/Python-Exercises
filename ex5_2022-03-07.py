#Exercice 5:
#Créez une fonction demandant à un utilisateur un nombre pair et un nombre impair, une fonction 
#permettant de vérifier que les nombres ne sont pas les deux pairs ou impairs, et affichez la phrase 
#suivante: Votre nombre impair est le x, votre nombre pair est le y et le résultat de leur division 
#est égal à z. Vous ne devez qu'afficher 3 chiffres après le point.


def nombres():
    nb_pair = int(input("Entrez un nombre pair"))
    nb_impair = int(input("Entrez un nombre impair"))
    return nb_pair, nb_impair 

def verification(nb1_pair, nb2_impair):
    if nb1_pair % 2 != 0:
        print("Votre nombre pair n'est pas pair!")
        return 
    if nb2_impair % 2 != 1:
        print("Votre nombre impair n'est pas impair!")
        return 
    ok = 1 
    return ok 


nombre_pair, nombre_impair = nombres()

checkup = verification(nombre_pair, nombre_impair)

if checkup == 1:
    phrase = (f"Votre nombre impair est le {nombre_impair}, votre nombre "
              f"pair est le {nombre_pair} et le résultat de leur division est "
              f"égal à {nombre_impair/nombre_pair:.3f}."
    )
    print(phrase)

            







