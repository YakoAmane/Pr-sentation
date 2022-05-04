from random import randint

essais = 1
x = randint(1, 100)
choix = int(input("Entrer un nombre entre 1 et 100 :"))
while choix != x:
    if choix > x:
        essais = essais + 1
        print("trop grand")
        choix = int(input("Entrer un nombre entre 1 et 100 :"))
    elif choix < x:
        essais = essais + 1
        print(" trop petit ")
        choix = int(input("Entrer un nombre entre 1 et 100 :"))
    if choix == x:
        print("vous avez trouver au bout de ", essais, " essai(s)")

#Ici, le programme est un petit jeu qui consiste à trouver un nombre au hasard entre 1 et 100
#défini aléatoirement au début de la partie par l'ordinateur.

#l'utilisateur choisie un nombre et l'ordinateur lui indique si celui-ci est trop grand ou trop petit et ajoute un nombre au compteur.
#A la fin de la partie quand le joueur a trouvé le nombre, l'ordinateur lui dit le nombre d'essai qu'il a fait.
