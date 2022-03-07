#Créez un programme demandant à un utilisateur d'entrer sa date de fête, 
# si la date est le 7 mars, affichez un message souhaitant bonne fête 
# à l'utilisateur, sinon affichez le message suivant: 
# Ce n'est pas ta fête aujourd'hui :(.

def bonne_fete(date_entrant):
    if date_fete == "7 mars":
        message = "bonne fête!!!"
        return message 
    else:
        message = "ce n'est pas ta fête aujourd'hui :("
        return message 

date_fete = input("Entrez votre jour et mois de fête (ex: 25 octobre)...")

print(bonne_fete(date_fete))




