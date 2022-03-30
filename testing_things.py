list_of_integers = [4, 7, 10, 7, 1, 9, 2, 7, 3]

sorted_list = list_of_integers[:]
for i in range(len(sorted_list)-1):
    min = sorted_list[i]
    pos = i
    for j in range(i, len(sorted_list)):
        if sorted_list[j] < min:
            min = sorted_list[j] 
            pos = j
    sorted_list[i], sorted_list[pos] = sorted_list[pos], sorted_list[i]
    

print(sorted_list)