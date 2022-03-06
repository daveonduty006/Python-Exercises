# Créer une fonction prenant 2 nombres en paramètre et retournant leur addition et soustraction.

def add_sous(n1, n2):
    return n1+n2, n1-n2

    
x = 20
y = 10
a, b = add_sous(x, y)
print(a)
print(b)