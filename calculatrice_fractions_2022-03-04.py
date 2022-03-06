#Exercice 2, Partie 1:
#Créer une calculatrice pour fractions incluant les opérations suivantes: 
#Addition (a/b + d/c)
#Soustraction (a/b - d/c)
#Multiplication (a/b * d/c)
#Divisions (a/b / d/c)

#Exercice 2, Partie 2:
#Écrivez vos fonctions de sorte qu'ils ne prennent que deux termes. Ex: fct(fraction1, fraction2).

#Exercice 2, Partie 3:
#Affichez vos résultats sous forme de fraction et sous forme d'un float.
#Testez vos fonctions avec plusieurs fractions pour vous assurer du bon fonctionnement.

def fract_equi(num1_entrant, den1_entrant, num2_entrant, den2_entrant):
    den_commun = den1_entrant * den2_entrant 
    proper_num1 = int(num1_entrant*den2_entrant)
    proper_num2 = int(num2_entrant*den1_entrant)
    return proper_num1, proper_num2, den_commun

def addition(fraction1_entrante, fraction2_entrante):
    prop_num1, den_commun, deci_fract1 = fraction1_entrante
    prop_num2, den_commun, deci_fract2 = fraction2_entrante 
    add_proper_fraction = f"{prop_num1+prop_num2}/{den_commun}"
    return deci_fract1+deci_fract2, add_proper_fraction

def soustraction(fraction1_entrante, fraction2_entrante):
    prop_num1, den_commun, deci_fract1 = fraction1_entrante
    prop_num2, den_commun, deci_fract2 = fraction2_entrante 
    sous_proper_fraction = f"{prop_num1-prop_num2}/{den_commun}"
    return deci_fract1-deci_fract2, sous_proper_fraction

def multiplication(fraction1_entrante, fraction2_entrante):
    prop_num1, den_commun, deci_fract1 = fraction1_entrante
    prop_num2, den_commun, deci_fract2 = fraction2_entrante 
    mul_proper_fraction = f"{prop_num1*prop_num2}/{den_commun*den_commun}"
    return deci_fract1*deci_fract2, mul_proper_fraction

def division(fraction1_entrante, fraction2_entrante):
    prop_num1, den_commun, deci_fract1 = fraction1_entrante
    prop_num2, den_commun, deci_fract2 = fraction2_entrante 
    div_proper_fraction = f"{prop_num1*den_commun}/{den_commun*prop_num2}"
    return deci_fract1/deci_fract2, div_proper_fraction

    
NUM1, DEN1 = 3, 6
NUM2, DEN2 = 5, 14
pnum1, pnum2, pden = fract_equi(NUM1, DEN1, NUM2, DEN2)

DECI_FRACT1 = 3 / 6
DECI_FRACT2 = 5 / 14

fraction1 = pnum1, pden, DECI_FRACT1
fraction2 = pnum2, pden, DECI_FRACT2

print(addition(fraction1, fraction2))
print(soustraction(fraction1, fraction2))
print(multiplication(fraction1, fraction2))
print(division(fraction1, fraction2))




