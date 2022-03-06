# Créer une fonction qui calcule la moyenne de 4 paramètre et qui retourne aussi la somme de ces 4 
# paramètres.

def fonction(a,b,c,d):
    som = a+b+c+d
    return som/4, som


w = 2
x = 3
y = 4
z = 5
m, n = fonction(w,x,y,z)
print(m)
print(n)

