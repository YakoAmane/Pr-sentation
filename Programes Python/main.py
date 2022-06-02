import machine
import time
import codeur
from motors import DRV8833
from motors import SERVO

# mise en fonction du robot
marche = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)

# détermination du camp de départ
camp = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_UP)

# motorisation
moteurs = DRV8833(12, 13, 26, 27)
moteurs.stop()

# codeurs roue gauche
codeurG = codeur.Codeur(4, 16)
codeurG.razNbImpulsions()
# codeurs roue droite
codeurD = codeur.Codeur(18, 19)
codeurD.razNbImpulsions()

# servo bras ventouse
brasVentouse = SERVO(23)

# pompe ventouse
pompeVentouse = machine.Pin(5, machine.Pin.OUT)

# capteur ligne droit
ld = machine.ADC(machine.Pin(39))
ld.atten(ld.ATTN_11DB)
ld.width(ld.WIDTH_10BIT)
# capteur ligne gauche
lg = machine.ADC(machine.Pin(36))
lg.atten(lg.ATTN_11DB)
lg.width(lg.WIDTH_10BIT)


def avancer(distancemm):
    dist0 = codeurG.nbImpulsions
    dist = 0
    tourRoue = 204
    moteurs.avant(1023, 962)
    while dist < distancemm:
        impsG = codeurG.nbImpulsions
        impsD = codeurD.nbImpulsions
        delta = impsG - impsD
        if abs(delta) > 20:
            print(impsG, impsD)
            if impsG > impsD:
                moteurs.avant(0, 1023)
                print("g>d")
                while impsG > impsD:
                    impsD = codeurD.nbImpulsions
            else:
                if impsD > impsG:
                    moteurs.avant(962, 0)
                    print("d>g")
                    while impsD > impsG:
                        impsG = codeurG.nbImpulsions
            print(impsG, impsD)
            print(dist)
        moteurs.avant(1023, 962)
        dist = (impsG - dist0) * tourRoue / 823.1
    moteurs.frein()


def reculer(distancemm):
    dist0 = codeurG.nbImpulsions
    dist = 0
    tourRoue = 204
    moteurs.arriere(1023, 962)
    while dist < distancemm:
        impsG = codeurG.nbImpulsions
        impsD = codeurD.nbImpulsions
        delta = impsG - impsD
        if abs(delta) > 20:
            print(impsG, impsD)
            if impsG > impsD:
                moteurs.arriere(0, 1023)
                print("g>d")
                while impsG > impsD:
                    impsD = codeurD.nbImpulsions
            else:
                if impsD > impsG:
                    moteurs.arriere(962, 0)
                    print("d>g")
                    while impsD > impsG:
                        impsG = codeurG.nbImpulsions
            print(impsG, impsD)
            print(dist)
        moteurs.arriere(1023, 962)
        dist = (impsG - dist0) * tourRoue / 823.1
    moteurs.frein()


def pivoterDroite(imps):
    moteurs.pivoteDroite(1023)
    nbImps = 0
    while nbImps < imps:
        nbImps = codeurG.nbImpulsions
        print(nbImps)
    moteurs.frein()


def pivoterGauche(imps):
    moteurs.pivoteGauche(1023)
    nbImps = 0
    while nbImps < imps:
        nbImps = codeurG.nbImpulsions
        print(nbImps)
    moteurs.frein()


brasVentouse.position(40)
while marche.value() == 0:
    pass
if camp.value() == 0:  # Si gpio2 à la masse départ camp Jaune
    print("camp Jaune")
    avancer(540)  # avancer vers le 1er palet à déterminer *****
    codeurG.razNbImpulsions()
    codeurD.razNbImpulsions()
    brasVentouse.position(20)  # baisser la ventouse
    time.sleep(0.5)
    pompeVentouse.value(1)  # activer la pompe
    time.sleep(1)
    brasVentouse.position(110)  # Relever la ventouse
    time.sleep(1)
    reculer(60)  # reculer à déterminer *****
    codeurG.razNbImpulsions()
    codeurD.razNbImpulsions()
    pivoterGauche(530)  # pivoter à gauche (1/4 de tour)
    avancer(500)  # à déterminer avancer vers la galerie *****
    codeurG.razNbImpulsions()
    codeurD.razNbImpulsions()
    brasVentouse.position(70)  # positionner ventouse avant dépose palet
    time.sleep(1)
    pompeVentouse.value(0)  # désactiver la ventouse (dépose palet)
    time.sleep(1)
    brasVentouse.position(110)  # Relever la ventouse
    reculer(520)  # reculer pour se positionner vers le 2ème palet à déterminer *****
    brasVentouse.position(40)  # redescendre la ventouse
    codeurG.razNbImpulsions()
    codeurD.razNbImpulsions()
    pivoterDroite(600)  # pivoter droite (1/4 tr) pour se positonner face au 2ème palet
    codeurG.razNbImpulsions()
    codeurD.razNbImpulsions()
    avancer(120)  # avancer vers le 2ème palet à déterminer *****
    codeurG.razNbImpulsions()
    codeurD.razNbImpulsions()
    brasVentouse.position(20)  # baisser la ventouse
    time.sleep(0.5)
    pompeVentouse.value(1)  # activer la pompe
    time.sleep(1)
    brasVentouse.position(120)  # Relever la ventouse
    time.sleep(1)
    avancer(340)  # avancer un petit peu
    codeurG.razNbImpulsions()
    codeurD.razNbImpulsions()
    pivoterGauche(600)  # pivoter à gauche (1/4 de tour)
    codeurG.razNbImpulsions()
    codeurD.razNbImpulsions()
    avancer(700)  # à déterminer avancer vers la galerie *****
    codeurG.razNbImpulsions()
    codeurD.razNbImpulsions()
    brasVentouse.position(70)  # positionner ventouse avant dépose palet
    time.sleep(1)
    pompeVentouse.value(0)  # désactiver la ventouse (dépose palet)
    time.sleep(2)
    brasVentouse.position(1000)  # Relever la ventouse
    reculer(300)  # reculer pour se positionner face au camp *****
    codeurG.razNbImpulsions()
    codeurD.razNbImpulsions()
    pivoterGauche(600)  # pivoter à gauche (1/4 de tour) pour s'orienter vers le camp
    codeurG.razNbImpulsions()
    codeurD.razNbImpulsions()
    avancer(830)  # avancer jusqu'au camp à déterminer *****
else:  # sinon départ camp violet
    print("camp Violet")
    avancer(550)  # à déterminer
    codeurG.razNbImpulsions()
    codeurD.razNbImpulsions()
    brasVentouse.position(20)
    time.sleep(0.5)
    pompeVentouse.value(1)
    time.sleep(1)
    brasVentouse.position(180)
    time.sleep(1)
    reculer(60)  # à déterminer
    codeurG.razNbImpulsions()
    codeurD.razNbImpulsions()
    pivoterDroite(460)  # pivoter à gauche 1/4 de tour
    avancer(500)  # à déterminer
    codeurG.razNbImpulsions()
    codeurD.razNbImpulsions()
    brasVentouse.position(80)
    time.sleep(2)
    pompeVentouse.value(0)
    time.sleep(2)
    brasVentouse.position(180)
    reculer(580)
    brasVentouse.position(40)
    codeurG.razNbImpulsions()
    codeurD.razNbImpulsions()
    pivoterGauche(600)
    codeurG.razNbImpulsions()
    codeurD.razNbImpulsions()
    avancer(160)
    codeurG.razNbImpulsions()
    codeurD.razNbImpulsions()
    brasVentouse.position(20)
    time.sleep(2)
    pompeVentouse.value(1)
    time.sleep(2)
    brasVentouse.position(180)
    time.sleep(2)
    avancer(410)
    codeurG.razNbImpulsions()
    codeurD.razNbImpulsions()
    pivoterDroite(600)
    codeurG.razNbImpulsions()
    codeurD.razNbImpulsions()
    avancer(700)
    codeurG.razNbImpulsions()
    codeurD.razNbImpulsions()
    brasVentouse.position(80)
    time.sleep(2)
    pompeVentouse.value(0)
    time.sleep(2)
    brasVentouse.position(100)
    reculer(300)
    codeurG.razNbImpulsions()
    codeurD.razNbImpulsions()
    pivoterDroite(600)
    codeurG.razNbImpulsions()
    codeurD.razNbImpulsions()
    avancer(830)
