def fonct1(x, y, z=0):
    
    def fonct2(x, y, z):
        return ((x+y)/z)
    
    return fonct2(x, y, z)

a = 1
b = 2
c = 3
print(fonct1(a,b,c))