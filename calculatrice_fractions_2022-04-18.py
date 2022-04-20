import math

#Implémenter une calculatrice de fraction en utilisant une classe fraction qui implémente les surcharges 
#d'opérateurs suivants: add(+), sub(-), eq(==), mul(*), div(/), str(), pow(**)

#Vous devez donc pouvoir faire des additions, soustractions, multiplications, divisions, et des puissances. 
#Vous devez aussi pouvoir vérifier si 2 fractions sont égales (faites attention de vérifier les formes 
#réduites, 1/2 == 2/4 devrait retourner True). Finalement vous devez surcharger str pour retourner votre 
#fraction sous forme d'un string pour pouvoir l'imprimer.

#Suite à l'implémentation, on devrait pouvoir écrire: fraction1 + fraction2 et avoir le résultat de 
#l'addition. Le principe est le même pour tous les opérateurs.

#Faites attention à pow(**), car on est censé faire (fraction1)^fraction2. Donc (4/1)**(1/2) = 2.

class Fraction:

    def __init__(self, num, den):
        self.num = num
        self.den = den
        gcd = self.get_gcd()
        self.num = self.num // gcd
        self.den = self.den // gcd

    def get_gcd(self):
        m, n = self.num, self.den
        while m % n != 0:
            oldm = m
            oldn = n
            m = oldn
            n = oldm % oldn
        return n

    def __add__(self, f2):
        self.num = (self.num * f2.den) + (self.den * f2.num)
        self.den = self.den * f2.den
        gcd = self.get_gcd()
        return Fraction(self.num//gcd, self.den//gcd)

    def __sub__(self, f2):
        self.num = (self.num * f2.den) - (self.den * f2.num)
        self.den = self.den * f2.den
        gcd = self.get_gcd()
        return Fraction(self.num//gcd, self.den//gcd)

    def __mul__(self, f2):
        self.num = self.num * f2.num 
        self.den = self.den * f2.den
        gcd = self.get_gcd()
        return Fraction(self.num//gcd, self.den//gcd)

    def __truediv__(self, f2):
        self.num = self.num * f2.den
        self.den = self.den * f2.num
        gcd = self.get_gcd()
        return Fraction(self.num//gcd, self.den//gcd)

    def __pow__(self, f2):
        return f"{math.pow(self.num, f2.num/f2.den)/math.pow(self.den, f2.num/f2.den):.2f}"

    def __eq__(self, f2):
        return self.num * f2.den == self.den * f2.num

    def __str__(self):
        return f"{self.num}/{self.den}"


f1 = Fraction(4,1)
f2 = Fraction(1,2)
f3 = f1 * f2
print(f3)