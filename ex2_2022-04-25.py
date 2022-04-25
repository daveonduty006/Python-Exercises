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

#Implémenter une classe player héritant de game object ayant:
#une méthode __str__ retournant un ▲(alt-30) ou un symbole équivalent
#une méthode go up déplaçant le joueur vers le haut et vérifiant si la sortie est 
#atteinte et empechant le déplacement s'il y a un obstacle(avec un message)
#une méthode go down déplaçant le joueur vers le bas et vérifiant si la sortie est 
#atteinte et empechant le déplacement s'il y a un obstacle(avec un message)
#une méthode go left déplaçant le joueur vers la gauche et vérifiant si la sortie 
#est atteinte et empechant le déplacement s'il y a un obstacle(avec un message)
#une méthode go right déplaçant le joueur vers la droite et vérifiant si la sortie 
#est atteinte et empechant le déplacement s'il y a un obstacle(avec un message)
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