# Créer une fonction qui permet de calculer la fonction suivante: (x + y) / z.
# Essayer ensuite avec z = 0.

def fonct1(x, y, z):             # la fonction 1 est ici complètement inutile
    
    def fonct2(x, y, z):
        return (x+y)/z
    
    return fonct2(x, y, z)


a = 1
b = 2
c = 3                            # si c = 0 le message d'erreur ZeroDivisionError va apparaître
print(fonct1(a,b,c))