import random
import sys
import os
from turtle import pos

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
        rows, cols = self.array_dim
        self.array = []
        for row in range(cols):
            row_go = []
            for col in range(rows):
                if row == cols-1 and col == 0:
                    self.player = Player( (row,col) )
                    row_go.append(self.player)
                elif row == 0 and col == rows-1:
                    self.exit = Exit( (row,col) )
                    row_go.append(self.exit)
                elif (row,col) != self.player.pos and (row,col) != self.exit.pos:
                    ob_set = self.make_obstacles_set()
                    row_go.append(self.go)
            self.array.append(row_go)

    def print_board(self):
        for row in self.array:
            print(row)  

    def make_obstacles_set(self):
        obstacle_set = []
        for i in range(self.array_dim[0]*self.array_dim[1]//4):
            self.obstacle = Obstacle()
            obstacle_set.append(self.obstacle)
        
        for i 
        return obstacle_set


    def menu(self):     
        print("Menu d'accueil")
        run = int(input("Press 1 for starting a new game: "))
        if run == 1:
            self.start_game()

    def start_game(self):
        running = True
        self.print_board()
        while running:
            self.move()                    

    def move(self):
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

    def __init__(self, pos):
        self.pos = pos

    def __str__(self):
        return " "

    def isObstacle(self):
        return False

    def isExit(self):
        return False

class Player(GameObject):

    def __init__(self, pos):
        super().__init__(pos)

    def __str__(self):
        return "▲"

class Obstacle(GameObject):

    def __init__(self, pos):
        super().__init__(pos)

    def __str__(self):
        return "X"

    def isObstacle(self):
        return True

class Exit(GameObject):

    def __init__(self, pos):
        super().__init__(pos)

    def __str__(self):
        return "◘"

    def isExit(self):
        return True 


array_dim = [10,10]
board = Board(array_dim)
board.menu()



    





