#Exercice 4:
#Créer un menu demandant à un utilisateur d'entrer un nombre pair, divisible par 
#3 et entre 10 et 29. 
#Si l'utilisateur entre un nombre ne correspondant pas à ces conditions, 
#offrez-lui l'opportunité de faire un nouvel essai, tant et aussi longtemps 
#qu'il n'entre pas un bon nombre.

def menu():
    user_input = 0
    while not(10 <= user_input <= 29): 
        user_input = int(input("Entrez un nombre pair entre 10 et 29 divisible " \
                               "par 3: "))
        while user_input % 3 != 0:
            user_input = int(input("Entrez nombre pair entre 10 et 29 et " \
                                   "divisible par 3 SVP: "))
    return print(user_input)



menu()