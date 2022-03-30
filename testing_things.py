list_of_integers = [4, 7, 10]

def calculate_mode(list_of_integers):
    dico = {}
    i = 0
    while i <= (len(list_of_integers)-1):
        new_entry = {list_of_integers[i] : 0}
        dico.update(new_entry)
        i = i + 1

    i = 0
    while i <= (len(list_of_integers)-1):
        dico[list_of_integers[i]] += 1 
        i = i + 1

    if max(dico.values()) > 1:
        mode = max(dico, key=dico.get)
    else:
        mode = "none"
    
    return mode 

calculate_mode(list_of_integers)