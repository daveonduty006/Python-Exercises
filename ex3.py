# Créer une fonction prenant 1 ou 2 nombres et effectuer l'addition de leur carré. Si un seul nombre 
# est passé en paramètre, assumez que sa valeur est 1.

def add_carre(n1=1, n2=1):
    return n1**2 + n2**2


n1 = 10
n2 = 20
print(add_carre(n1, n2))
print(add_carre(n1))
print(add_carre())