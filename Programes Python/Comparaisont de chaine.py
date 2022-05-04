def comparaison(chaine1, chaine2):
    if chaine1 == chaine2:
        return "chaines égales"
    elif chaine1 < chaine2:
        return chaine1, chaine2
    else:
        return chaine2, chaine1

#Ici, le programe compare les deux chaines indiquer par l'utilisateurs pour les ranger de la plus petite a la plus grande.
#(On definie plus petite/grande en fonctione du nombre de caractère)
