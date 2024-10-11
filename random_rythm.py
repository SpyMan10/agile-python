import random
import time
from math import floor


def random_rhythm(random_notes_list: list[str]) -> str:
    # Choix vitesse de lecture
    print("""
#-------------------------------#
#     Génération Aléatoire      #
#-------------------------------#

Choix de votre vitesse de lecture : 
1 : Rapide
2 : Normal
3 : Lent
          """.strip())
    user_speed_choice = input()
    speed = ["Lent", "Normal", "Rapide"]
    print(f"""
#----------------------------------------------------------#
     Vous avez choisi une lecture : {speed[int(user_speed_choice) - 1]}
#----------------------------------------------------------#
        """.strip())

    # Choix du nom du fichier du client
    print("""Donner un nom à votre moreau :""")
    user_track_name = input()

    # Ouvre (ou crée) un fichier texte en mode écriture ('w')
    with open(f'samples/{user_track_name}.txt', 'w') as fichier:
        # déteerminer le temps de la note
        initial_duration = random.randint(80, 125) / 1000

        for note in random_notes_list:
            # Ajouter un muliplicatur de durée pour 20% des notes
            multiplier = random.randint(2, 3) if 8 < random.randint(1, 10) else 1
            multiplier *= int(user_speed_choice)
            duration = round(initial_duration * multiplier, 3)

            # déterminer le nombre de blanc
            random_int = random.randint(1, 6)
            fichier.write(str(note) + " " + str(duration) + "\n")

            # Reperter le nombre de blanc
            index_flag = 0

            while index_flag < random_int:
                fichier.write("0 " + str(duration) + "\n")
                index_flag = index_flag + 1

    print(f"""
    #----------------------------------------------------------#
          Votre morceau {user_track_name} a était généré.
          Lecture de votre morceau.
    #----------------------------------------------------------#
          """)

    return user_track_name
