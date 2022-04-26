import random
import sys
import os

#Implémenter une classe board ayant:
#une matrice en 2D de grosseur 15x15 possédant remplie d'objets de type game object. 
#Vous devez avoir un seul objet de type joueur et le quart de votre tableau doit 
#être remplis d'obstacles.
#une méthode start game
#une méthode print board
#une méthode menu implémentant un menu d'acceuil
#une méthode success pour afficher un écran de succès pendant 10 secondes
#une méthode failed pour afficher un écran d'échec pendant 10 secondes
#une méthode move prennant une entrée utilisateur pour indiquer une direction et 
#faire bouger le joueur.
#les méthodes nécessaires au reste de l'implémentation

#Implémenter une classe game object ayant :
#le game object en haut, à gauche, à droite et en bas (None si elle n'existe pas)
#sa position dans la matrice du board
#une méthode __str__ retournant un espace vide (" ")
#une méthode isObstacle() retournant False
#une méthode isExit() retournant False
#les méthodes nécessaires au reste de l'implémentation

 

#Implémenter une classe obstacle héritant de game object ayant:
#une méthode __str__ retournant un X
#une méthode isObstacle() retournant True

#Implémenter une classe exit héritant de game object ayant:
#une méthode __str__ retournant un ◘ (alt-8) ou un autre symbole de votre choix
#une méthode isExit() retournant True

#Bonus:
#Implémenter une classe enemy héritant de game object se déplaçant aléatoirement 
#après chaque mouvement du joueur et terminant le jeu en rentrant en contact avec 
#le joueur.


class Board:

    def __init__(self, array_dim:list):
        self.array_dim = array_dim

    def menu(self):     
        print("Menu d'accueil")
        run = int(input("Press 1 for starting a new game: "))
        if run == 1:
            self.start_game()

    def start_game(self):
        running = True
        while running:
            self.move()

    def print_board(self):
        rows, columns = self.array_dim
        array = [[0]*columns]*rows
        for row in array:
            print(row)

    def move(self):
        self.print_board()
        print("Press W for going Up")
        print("Press S for going Down")
        print("Press A for going Left")
        print("Press D for going Right")
        user_inp = input("Input: ")
        while not (user_inp == "W" or user_inp == "S" or user_inp == "A" or\
                   user_inp == "D"):
            user_inp = input("Invalid input, try again: ")
        Player(user_inp)


class GameObject:

    def __init__(self, pos, north_go=None, south_go=None, east_go=None, west_go=None):
        self.pos = pos
        self.north_go = north_go
        self.south_go = south_go
        self.east_go = east_go
        self.west_go = west_go

    def __str__(self):
        return " "

    def isObstacle(self):
        return False

    def isExit(self):
        return False

class Player(GameObject):

    def __init__(self, input):
        self_input = input

    def __str__(self):
        return "▲"

class Obstacle(GameObject):

    def __init__(self):
        obstacles = []
        for i in range(25):
            obstacles.append(str(self))

    def __str__(self):
        return "X"

    def isObstacle(self):
        return True

class Exit(GameObject):

    def __str__(self):
        return "◘"

    def isExit(self):
        return True 


array_dim = [10,10]
board = Board(array_dim)
board.menu() 



    





