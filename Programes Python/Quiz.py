bonne =0
mauvaise=0
rep=float (input ("En multipliant des secondes par des watts on obtient ? Tapez 1 pour des joules, 2 pour des watts heure, 3 pour des Volts "))
if rep == 1 :
    bonne= bonne +1
    print ("Bravo, c'est correct")
else :
    mauvaise= mauvaise +1
print ("mauvaise(s) réponse(s) =" ,mauvaise , "bonne(s) réponse(s)=" ,bonne, )
rep=float (input ("Laquelle des quantités suivante correspond à 1 W.h ? Tapez 1 pour 1/3600 Joules, 2 pour 3600 Joules, 3 pour 3600 Watts "))
if rep == 2 :
    bonne=bonne +1
    print ("Bravo, c'est correct")
else :
    mauvaise= mauvaise+1
print ("mauvaise(s) réponse(s) =" ,mauvaise, "bonne(s) réponse(s)=" ,bonne, )
rep=float (input ("Quelle association grandeur physique : Unité de mesure est fausse ? tapez 1 puissance mécanique : watt, 2 pour énergie : watt heure, 3 pour couple : newton "))
if rep ==3 :
    bonne=bonne+1
    print ("Bravo, c'est correct")
else :
    mauvaise=mauvaise+1
print ("mauvaise(s) réponse(s) =" ,mauvaise, "bonne(s) réponse(s)=" ,bonne, )
print ("merci de votre visite")
réessayer= str( input ("Vouler vous réessayer ?"))
while réessayer == "oui":
    bonne =0
    mauvaise=0
    rep=float (input ("En multipliant des secondes par des watts on obtient ? Tapez 1 pour des joules, 2 pour des watts heure, 3 pour des Volts "))
    if rep == 1 :
        bonne= bonne +1
        print ("Bravo, c'est correct")
    else :
        mauvaise= mauvaise +1
    print ("mauvaise(s) réponse(s) =" ,mauvaise , "bonne(s) réponse(s)=" ,bonne, )
    rep=float (input ("Laquelle des quantités suivante correspond à 1 W.h ? Tapez 1 pour 1/3600 Joules, 2 pour 3600 Joules, 3 pour 3600 Watts "))
    if rep == 2 :
        bonne=bonne +1
        print ("Bravo, c'est correct")
    else :
        mauvaise= mauvaise+1
    print ("mauvaise(s) réponse(s) =" ,mauvaise, "bonne(s) réponse(s)=" ,bonne, )
    rep=float (input ("Quelle association grandeur physique : Unité de mesure est fausse ? tapez 1 puissance mécanique : watt, 2 pour énergie : watt heure, 3 pour couple : newton "))
    if rep ==3 :
        bonne=bonne+1
        print ("Bravo, c'est correct")
    else :
        mauvaise=mauvaise+1
    print ("mauvaise(s) réponse(s) =" ,mauvaise, "bonne(s) réponse(s)=" ,bonne, )
    print ("merci de votre visite")
    réessayer= str( input ("Vouler vous réessayer ?"))
else:
    print ("merci de votre visite")

#Se programe est un Quiz a 3 question qui compte les bonne et mauvaise reponse puis demande si l'ont veut rejouer.
