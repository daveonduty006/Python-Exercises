<<<<<<< Updated upstream
=======
<<<<<<< HEAD
        for i in range(len(copy_list)//4):
            if i == 0:
                for card in range(len(d7)):
                    deck_list.append(d7[card])
            if i == 1:
                for card in range(len(d1)):
                    deck_list.append(d1[card])
            if i == 2:
                for card in range(len(d3)):
                    deck_list.append(d3[card])
            if i == 3:
                for card in range(len(d13)):
                    deck_list.append(d13[card])
            if i == 4:
                for card in range(len(d2)):
                    deck_list.append(d2[card])
            if i == 5:
                for card in range(len(d4)):
                    deck_list.append(d4[card])
            if i == 6:
                for card in range(len(d11)):
                    deck_list.append(d5[card])
            if i == 7:
                for card in range(len(d6)):
                    deck_list.append(d6[card])
            if i == 8:
                for card in range(len(d8)):
                    deck_list.append(d8[card])
            if i == 9:
                for card in range(len(d5)):
                    deck_list.append(d5[card])
            if i == 10:
                for card in range(len(d12)):
                    deck_list.append(d12[card])
            if i == 11:
                for card in range(len(d10)):
                    deck_list.append(d10[card])
            if i == 12:
                for card in range(len(d9)):
                    deck_list.append(d9[card])
=======
>>>>>>> Stashed changes
list_of_strs = ["4", "7", "10", "6", "1", "9", "2", "8"]
copied_list = list_of_strs[:]
list_of_strs = []


for card in range(1, len(copied_list)+1):
    if card % 4 == 0 and card != 0:
        list_of_strs.append(card-3)
        list_of_strs.append(card-2)
        list_of_strs.append(card-1)
        list_of_strs.append(card)

    

<<<<<<< Updated upstream
print(list_of_strs)
=======
print(list_of_strs)
>>>>>>> 7b355bce57e33b29d24ba6d15c1bd460b86e8cea
>>>>>>> Stashed changes
