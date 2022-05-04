def p (mot):
    t=""
    for i in range (-1,-len(mot),-1):
        t=t+mot[i]
    t=t+mot[0]
    if t==mot :
        return True
    else:
        return False

#Ici, le programe sert a trouver si le mots est palindrome ou non.

#Pour cela, la boucle "i" sert a lire le mots a l'envers lettre par lettre et ajoute chaque lettre a la variable "t"
#afin de réecrire le mots a l'envers.

#Ensuite on compare les deux mots.Et donc si le mots est palindrome l'ordinateur renvois que c'est vrais sinon, il lui renvoie que c'est faux.
