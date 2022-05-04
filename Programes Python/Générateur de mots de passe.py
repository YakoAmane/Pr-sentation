from random import choice
def mdp(x):
    chaine = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    pwd = " "
    for i in range(x):
        pwd = pwd + choice(chaine)
    return pwd
#Ici, importe "choice" de la bibliptèque "random" on prend un caractère au hasard de la chaine si dessus qu'on ajoute a "pwd"
#et tout cela x fois pour avoir un nombre limiter de caractère defini par l'utilisateur pour lui générer un mots de passe
#aléatoire
