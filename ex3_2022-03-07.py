#Exercice 3:
#Créez un programme demandant à un utilisateur d'entrer sa date de fête, si la date est le 7 mars, 
#affichez un message souhaitant bonne fête à l'utilisateur, sinon affichez le message suivant: Ce 
#n'est pas ta fête aujourd'hui :(.

def messages(jour_entrant, mois_entrant):
    if jour_entrant == 7:
        if mois_entrant == 3:
            message = "Bonne fête!"
    else:
        message = "Ce n'est pas ta fête aujourd'hui :(."
    return message 


jour_fete = int(input("Entrez le jour de votre naissance: "))
mois_fete = int(input("Entrez le mois de votre fête en chiffre(s): "))

print(messages(jour_fete, mois_fete))