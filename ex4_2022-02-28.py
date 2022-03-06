# Créer une fonction prenant trois nombres et retournant la moyenne de leur carré + 1.

def moy(a, b, c):

    def fonc(n):
        e = 2
        return n**e+1

    return (fonc(a)+fonc(b)+fonc(c))/3


x= 5
y= 4
z= 3
print(moy(x,y,z))


# Ensuite, modifier la fonction pour retourner la moyenne de leur cube + 2.

def moy(a, b, c):

    def fonc(n):
        e = 3
        return n**e+2

    return (fonc(a)+fonc(b)+fonc(c))/3


x= 5
y= 4
z= 3
print(moy(x,y,z))


# Finalement retournant la moyenne de la fonction suivante: x**x + x + 3, pour les 3 nombres.

def moy(a, b, c):

    def fonc(n):
        return n**n+n+3

    return (fonc(a)+fonc(b)+fonc(c))/3


x= 5
y= 4
z= 3
print(moy(x,y,z))
