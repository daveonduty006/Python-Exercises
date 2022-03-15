#Exercice 3:
#Écrire un programme offrant un menu à un utilisateur avec 3 choix et lui affichant la phrase suivante une 
#fois sélectionné:
#  1. Bonjour
#  2. Au revoir
#  3. À plus tard

def phrase():
    mot = int(input("Sélectionnez un mot: \n"
                "1. Bonjour \n"
                "2. Au revoir \n"
                "3. À plus tard \n"))
    phrase = ""
    if mot == 1:
        phrase = "Bonjour"
    elif mot == 2:
        phrase = "Au revoir"
    elif mot == 3:
        phrase = "À plus tard"
    else:
        phrase = "Sélection invalide"
    return phrase 


print(phrase())