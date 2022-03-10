#Exercice 8:
#Reprendre l'exercice de la calculatrice de fraction, et implémenter un menu permettant à 
#l'utilisateur d'effectuer les opérations définies et retourner les résultats sous forme de fraction 
#réduite et sous forme de float avec 3 chiffres après la virgule. 

from fractions import Fraction

def fract_equi(num1_entrant, den1_entrant, num2_entrant, den2_entrant):
    den_commun = den1_entrant * den2_entrant 
    proper_num1 = int(num1_entrant*den2_entrant)
    proper_num2 = int(num2_entrant*den1_entrant)
    return proper_num1, proper_num2, den_commun

def addition(fraction1_entrante, fraction2_entrante):
    prop_num1, den_commun, deci_fract1 = fraction1_entrante
    prop_num2, den_commun, deci_fract2 = fraction2_entrante 
    fract_redu = str(Fraction(prop_num1+prop_num2, den_commun))
    return f"{deci_fract1+deci_fract2:.3f}", fract_redu

def soustraction(fraction1_entrante, fraction2_entrante):
    prop_num1, den_commun, deci_fract1 = fraction1_entrante
    prop_num2, den_commun, deci_fract2 = fraction2_entrante 
    fract_redu = str(Fraction(prop_num1-prop_num2, den_commun))
    return f"{deci_fract1-deci_fract2:.3f}", fract_redu

def multiplication(fraction1_entrante, fraction2_entrante):
    prop_num1, den_commun, deci_fract1 = fraction1_entrante
    prop_num2, den_commun, deci_fract2 = fraction2_entrante 
    fract_redu = str(Fraction(prop_num1*prop_num2, den_commun*den_commun))   
    return f"{deci_fract1*deci_fract2:.3f}", fract_redu

def division(fraction1_entrante, fraction2_entrante):
    prop_num1, den_commun, deci_fract1 = fraction1_entrante
    prop_num2, den_commun, deci_fract2 = fraction2_entrante 
    fract_redu = str(Fraction(prop_num1*den_commun, den_commun*prop_num2))
    return f"{deci_fract1/deci_fract2:.3f}", fract_redu 


num1 = int(input("Entrez le numérateur de la première fraction: "))
den1 = int(input("Entrez le dénominateur de la première fraction: "))
num2 = int(input("Entrez le numérateur de la deuxième fraction: "))
den2 = int(input("Entrez le dénominateur de la deuxième fraction: "))

pnum1, pnum2, pden = fract_equi(num1, den1, num2, den2)
deci_fract1 = num1 / den1
deci_fract2 = num2 / den2 
fraction1 = pnum1, pden, deci_fract1
fraction2 = pnum2, pden, deci_fract2

rep_operation = int(input("""
Menu de la calculatrice de fraction:
Pour faire l'addition de fractions, entrez 1
Pour faire la soustraction de fractions, entrez 2 
Pour faire la multiplication de fractions, entrez 3
Pour faire la division de fractions, entrez 4 
"""))

if rep_operation == 1:
    print(addition(fraction1, fraction2))
elif rep_operation == 2:
    print(soustraction(fraction1, fraction2))
elif rep_operation == 3:
    print(multiplication(fraction1, fraction2))
elif rep_operation ==4:
    print(division(fraction1, fraction2))
else:
    print("Le chiffre que vous avez entré est invalide :(")
    