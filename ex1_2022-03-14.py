#Exercice 1:
#Créer une fonction prenant 4 paramètres et les retournant en ordre croissant en 
#utilisant que des conditions(en n’utilisant pas de loops).

def ordre_croissant(p1, p2, p3, p4):
    ordre = ""
    if p1 <= p2 and p1 <= p3 and p1 <= p4:
        ordre = p1
        if p2 <= p3 and p2 <= p4:
            ordre = p1 + "," + p2
            if p3 <= p4:
                ordre = p1 + "," + p2 + "," + p3 + "," + p4
            else:
                ordre = p1 + "," + p2 + "," + p4 + "," + p3
        elif p3 <= p2 and p3 <= p4:
            ordre = p1 + "," + p3
            if p2 <= p4:
                ordre = p1 + "," + p3 + "," + p2 + "," + p4
            else:
                ordre = p1 + "," + p3 + "," + p4 + "," + p2
        else: 
            ordre = p1 + "," + p4
            if p2 <= p3:
                ordre = p1 + "," + p4 + "," + p2 + "," + p3
            else: 
                ordre = p1 + "," + p4 + "," + p3 + "," + p2

    if p2 <= p1 and p2 <= p3 and p2 <= p4:
        ordre = p2
        if p1 <= p3 and p1 <= p4:
            ordre = p2 + "," + p1
            if p3 <= p4:
                ordre = p2 + "," + p1 + "," + p3 + "," + p4
            else:
                ordre = p2 + "," + p1 + "," + p4 + "," + p3
        elif p3 <= p1 and p3 <= p4:
            ordre = p1 + "," + p3
            if p1 <= p4:
                ordre = p2 + "," + p3 + "," + p1 + "," + p4
            else:
                ordre = p2 + "," + p3 + "," + p4 + "," + p1
        else: 
            ordre = p2 + "," + p4
            if p1 <= p3:
                ordre = p2 + "," + p4 + "," + p1 + "," + p3
            else: 
                ordre = p2 + "," + p4 + "," + p3 + "," + p1

    if p3 <= p1 and p3 <= p2 and p3 <= p4:
        ordre = p3
        if p1 <= p2 and p1 <= p4:
            ordre = p3 + "," + p1
            if p2 <= p4:
                ordre = p3 + "," + p1 + "," + p2 + "," + p4
            else:
                ordre = p3 + "," + p1 + "," + p4 + "," + p2
        elif p2 <= p1 and p2 <= p4:
            ordre = p3 + "," + p2
            if p1 <= p4:
                ordre = p3 + "," + p2 + "," + p1 + "," + p4
            else:
                ordre = p3 + "," + p2 + "," + p4 + "," + p1
        else: 
            ordre = p3 + "," + p4
            if p1 <= p2:
                ordre = p3 + "," + p4 + "," + p1 + "," + p2
            else: 
                ordre = p3 + "," + p4 + "," + p2 + "," + p1

    if p4 <= p1 and p4 <= p2 and p4 <= p3:
        ordre = p4
        if p1 <= p2 and p1 <= p3:
            ordre = p4 + "," + p1
            if p2 <= p3:
                ordre = p4 + "," + p1 + "," + p2 + "," + p3
            else:
                ordre = p4 + "," + p1 + "," + p3 + "," + p2
        elif p2 <= p1 and p2 <= p3:
            ordre = p4 + "," + p2
            if p1 <= p3:
                ordre = p4 + "," + p2 + "," + p1 + "," + p3
            else:
                ordre = p4 + "," + p2 + "," + p3 + "," + p1
        else: 
            ordre = p4 + "," + p3
            if p1 <= p2:
                ordre = p4 + "," + p3 + "," + p1 + "," + p2
            else: 
                ordre = p4 + "," + p3 + "," + p2 + "," + p1

    return ordre

    
n1 = input("Entrez un nombre: ")
n2 = input("Entrez un nombre: ")
n3 = input("Entrez un nombre: ")
n4 = input("Entrez un nombre: ")

print(ordre_croissant(n1, n2, n3, n4))
