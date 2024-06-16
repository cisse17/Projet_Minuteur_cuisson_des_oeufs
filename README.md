
#   ____Enoncer de l'Exercice_____
"""
## Cuisson des oeufs

Vous aimez les oeufs à la coque, ou les oeufs durs ? Dans tous les cas le plus important c'est de respecter la cuisson.
Pour cet exercice de code, vous allez réaliser un programme de type "minuteur" qui permettra d'afficher en temps réel 
le temps restant de cuisson.

#### -> Votre programme proposera 3 options :

#### - Oeufs à la coque : 3 minutes

#### - Oeufs mollets : 6 minutes

#### - Oeufs durs : 9 minutes

Une fois l'option choisie, votre programme commencera à attendre la durée concernée.

A chaque seconde, vous afficherez un "." sur une même ligne (afin que l'on voit un effet de progression).

Et toutes les 10 secondes vous irez à la ligne suivante en affichant le temps restant.

Exemple:
..........

#### Temps restant : 2:50..........

#### Temps restant : 2:40.....

Quand le temps est écoulé, vous afficherez "Cuisson terminée", et votre programme se terminera.

#### BONUS : Vous pourrez aussi jouer un son une fois la cuisson terminée


#### NOTION SUPPLÉMENTAIRES

Pour réaliser ce programme vous aurez besoin des notion supplémentaires suivantes :

-> Bloquer le programme pendant 1 seconde :

import time
time.sleep(1)


-> Afficher un point sans aller à la ligne :

print(".", end="", flush=True)


-> Boucler 5 secondes et afficher un "." à chaque seconde :

for i in range(5):
    time.sleep(1)
    print(".", end="", flush=True)


#### -> Convertir la durée "d" en secondes, en minutes/secondes :

d = 100
min = d//60 # division entière (pas de virgules)
sec = d-min*60

-> Afficher un nombre avec 2 chiffres complétés par un "0" (si nécessaire) :

print(f"{min:02d}")

-> Jouer un son

"""
