list_of_strs = ["4", "7", "10", "6", "1", "9", "2", "8"]
copied_list = list_of_strs[:]
list_of_strs = []


for card in range(1, len(copied_list)+1):
    if card % 4 == 0 and card != 0:
        list_of_strs.append(card-3)
        list_of_strs.append(card-2)
        list_of_strs.append(card-1)
        list_of_strs.append(card)

    

print(list_of_strs)