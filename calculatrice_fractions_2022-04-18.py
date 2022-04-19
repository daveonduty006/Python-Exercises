def gcd(num, den): 
    # Euclidean algorithm for finding the greatest common divisor
    if num == 0:
        return abs(den)
    else:
        return gcd(den % num, num)
    

class Fraction:

    def __init__(self, f1_tuple, f2_tuple):
        self.f1 = f"{f1_tuple[0]}/{f1_tuple[1]}"
        self.f2 = f"{f2_tuple[0]}/{f2_tuple[1]}"

def fraction_input():
    exit = False
    while not exit: 
        f1_num = input("Entrez le numérateur de votre première fraction: ")
        if f1_num.lstrip("-").isdecimal():
            f1_den = input("Entrez le dénominateur de votre première fraction: ")
            if f1_den.lstrip("-").isdecimal():
                f2_num = input("Entrez le numérateur de votre deuxième fraction: ")
                if f2_num.lstrip("-").isdecimal():
                    f2_den = input("Entrez le dénominateur de votre deuxième fraction: ")
                    if f2_den.lstrip("-").isdecimal(): 
                        exit = True
    f1_tuple = (f1_num, f1_den) 
    f2_tuple = (f2_num, f2_den)
    return f1_tuple, f2_tuple

def execution():
    f1_tuple, f2_tuple = fraction_input()
    f1, f2 = Fraction(f1_tuple, f2_tuple)
    print(f1)
    exit = False
    while not exit:
        user_sel = 0
        while not 1 <= user_sel <= 6:
            user_sel = int(input(f"Menu des options:\n"
                                 f"1. Additionner les fractions\n"
                                 f"2. Soustraire les fractions\n"
                                 f"3. Multiplier les fractions\n"
                                 f"4. Diviser les fractions\n"
                                 f"5. Modifier les fractions\n"
                                 f"6. Terminer\n"
                                 f"Choisissez l'une des options: "))





execution()

        

