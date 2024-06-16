
import time
#import beepy
import winsound

# Porjet Cuisson des oeufs

DUREE_PROGRESSION = 10
print("Minuteur pour la cuisson des oeufs")
print("1 - Oeufs à la coque : 3 minutes")
print("2 - Oeufs mollets : 6 minutes")
print("3 - Oeufs durs : 9 minutes")
while True:
    choix = input("Votre choix : ")
    if choix == "1" or choix == "2" or choix == "3":
         break
    print("ERREUR: Vous devez choisir 1, 2 ou 3\n")

duree = 0
if choix == "1":
    duree = 3 * 60
if choix == "2":
    duree = 6 * 60
if choix == "3":
    duree = 9 * 60

while True:
    for i in range(DUREE_PROGRESSION):
        time.sleep(1)
        print(".", end="", flush=True)  # flush qui veut dire vider l'affichage/ forcer l'affichage
                                    # end="" prmet d'aligner les points sur la mm ligne
        duree -= 1
        if duree <= 0:
            break

    if duree <= 0:
        break
    min = duree//60  #division entière (pas de virgules) 100= 1,'40 sec
    sec = duree-min*60
    print()
    print(f"Temps restant : {min:02d}:{sec:02d}", end="", flush=True)

print()
print("Cuisson terminée")
#beepy.beep(sound="ping")
winsound.Beep(frequency=500, duration=500)
#winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)  # dautre si préféré




"""

- Oeufs à la coque : 3 minutes
- Oeufs mollets : 6 minutes
- Oeufs durs : 9 minutes

import time
time.sleep(1)
print(".", end="", flush=True)

d = 100  # 100       seconde égale 1 min 40
min = d//60 # division entière (pas de virgules)   pr avoir le nbre de minute
sec = d-min*60

print(f"{min:02d}")

"""



