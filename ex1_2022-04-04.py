#Exercice 1:
#Vous devez implémenter 5 animations différentes à l'intérieur d'un menu 
#similairement à l'exemple publié au cours. Notez qu'un déplacement vers la 
#gauche et vers la droite ne compte pas commes 2 animations différentes. Les 
#animations doivent être plus distincte qu'un changement de direction. Vous ne 
#pouvez pas non plus reprendre les exemples publiés dans les notes de cours, 
#soyez créatifs!
#Faire la revue de paires pour l'exercice 1.

from time import sleep, time 
import os 
import sys 

#Permet d'effacer ce qui est afficher à la console.
#Taken from https://stackoverflow.com/questions/2084508/clear-terminal-in-python
#By user: poke
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def loading():
    end = time() + 5
    while time() < end:
        for ele in ["|", "/", "-", "\\"]:
            cls()
            if ele == "|":
                print(f"loading...{ele}")
            elif ele == "/":
                print(f"loading...{ele}")
            elif ele == "-":
                print(f"loading...{ele}")
            elif ele == "\\":
                print(f"loading...{ele}")
            sleep(.2)
    cls()
    print("ready!")

def chasing_unicode():
    end = time() + 1
    bird = "\U0001f99c"
    dave = "\U0001f3c7"
    while time() < end:
        for i in range(15,0,-1):
            cls()
            print(f"""                 {bird.rjust(i)}
                       {dave.rjust(i)}""")
            sleep(.08)
    cls()

#Code structure taken from 
#https://stackoverflow.com/questions/19911346/create-a-typewriter-effect-animation-for-strings-in-python
#By user: TobiMarg  
def spooky_chorus():
    line_1 = "A terrifying scream wakes you from a deep slumber\n"
    line_2 = "Slowly, you come to your senses, and realize where you are:\n"
    line_3 = "IT`S A MADHOUSE\n"
    line_4 = "OR SO THEY CLAIM\n"
    line_5 = "IT`S A MADHOUSE\n"
    line_6 = "OH, AM I INSANE ?"

    list_of_lines = [line_1, line_2, line_3, line_4, line_5, line_6]
    for i in range(len(list_of_lines)-1):
        for x in list_of_lines[i]:
            print(x, end='')
            sys.stdout.flush()
            sleep(.1)
    print(list_of_lines[-1][:2])
    sleep(1)
    for x in list_of_lines[-1][4:]:
        print(x, end='')
        sys.stdout.flush()
        sleep(.2)
        if x == list_of_lines[-1][-1]:
            print("\n")

def blind_superman():
    obstacle = "          <|"
    player= "==:::o"
    for c in range(1,11):
        cls()
        print(f"{player}{obstacle.replace(' ', '', c)}")
        sleep(.2)
        if c == 10:
            cls()
            print(f"{'BOOM'}")
            sleep(.2)


exit = False
while not exit:
    user_res = int(input(f"Main menu:\n"
                         f"1. Loading\n"
                         f"2. Chasing Bird while on a Horse\n"
                         f"3. Spooky Chorus\n"
                         f"4. Blind Superman\n"))
    if user_res == 1:
        loading()
    elif user_res == 2:
        chasing_unicode()
    elif user_res == 3:
        spooky_chorus()
    elif user_res == 4:
        blind_superman()



