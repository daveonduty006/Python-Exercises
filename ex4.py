# Créer une fonction prenant trois nombres et retournant la moyenne de leur carré + 1.

def moy(a, b, c):
    e = 2

    def exp(n):
        return n**e+1

    return (exp(a)+exp(b)+exp(c))


x= 5
y= 4
z= 3
print(moy(x,y,z))


# Ensuite, modifier la fonction pour retourner la moyenne de leur cube + 2.

def moy(a, b, c):
    e = 3

    def exp(n):
        return n**e+2

    return (exp(a)+exp(b)+exp(c))


x= 5
y= 4
z= 3
print(moy(x,y,z))


# Finalement retournant la moyenne de la fonction suivante: x**x + x + 3, pour les 3 nombres.

def moy(a, b, c):

    def exp(n):
        return n**n+n+3

    return (exp(a)+exp(b)+exp(c))/3


x= 5
y= 4
z= 3
print(moy(x,y,z))