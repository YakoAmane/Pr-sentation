import math
L= float(input("Quelle est la taille en mètre ?"))
M= float(input("Quelle est la masse en kilogramme ?"))
S=(math.sqrt(L*M))/6
print ("La surface corporelle de l'induvidu de ",L, "mètre et de ", M, "kg est d'environ", S, "m^2")
retry= input("Voulez vous calculer une autre surface corporelle ?")
while retry =="oui":
   L= float(input("Quelle est la taille en mètre ?"))
   M= float(input("Quelle est la masse en kilogramme ?"))
   S=(math.sqrt(L*M))/6
   print ("La surface corporelle de l'induvidu de ",L, "mètre et de ", M, "kg est d'environ", S, "m^2")
   retry= input("Voulez vous calculer une autre surface corporelle ?")

#Ici, le programme sert à calculer la surface corporelle d'un individu avec les valeurs que celui-ci lui envoie
#puis lui demande à la fin si celui-ci veut faire une nouvelle conversion ou non
