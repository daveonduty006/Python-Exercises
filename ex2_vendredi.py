# Exercice 2, Partie 1:
#Créer une calculatrice pour fractions incluant les opérations suivantes: 
#Addition (a/b + d/c)
#Soustraction (a/b - d/c)
#Multiplication (a/b * d/c)
#Divisions (a/b / d/c)

def addition(fractions_entrantes):
    decimal_fractions = fraction1+fraction2
    return decimal_fractions, 

def soustraction(fractions_entrantes):
    decimal_fractions = fraction1-fraction2
    return decimal_fractions, f"{decimal_fractions*100:.0f}/100"

def multiplication(fractions_entrantes):
    decimal_fractions = fraction1*fraction2
    return decimal_fractions, f"{decimal_fractions*100:.0f}/100"

def division(fractions_entrantes):
    decimal_fractions = fraction1/fraction2
    return decimal_fractions, f"{decimal_fractions*100:.0f}/100"

    
FRACTIONS = 1/3, 5/6
fraction1, fraction2 = FRACTIONS

print(addition(FRACTIONS))
print(soustraction(FRACTIONS))
print(multiplication(FRACTIONS))
print(division(FRACTIONS))




