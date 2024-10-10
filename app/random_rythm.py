# Créer une séquence aléatoire
import FreqMap as fm
import numpy as np
import random

#
# - Random list des notes -
#
# Simplification en variable
notes_dict = fm.note_to_frequency
# Récueration du nom de la note uniquement
list_note = list(notes_dict.keys())
# Faire une variable pour le nombre de note random
random_size = 50
# Création de la liste random d'index
list_random = np.random.randint(89, size=random_size).tolist()
# Association des index au notes dans une liste
random_notes_list = [list_note[note] for note in list_random]
# Affichage de la liste final des notes
# print(random_notes_list)

# Liste to do
# Déterminer une durée pour chacune des notes
# la durée de la note est la même que la durée des blancs qui suivent
# Le nombre de blanc qui suivent est de 1 à 6 et de même durée que la note qui precèdent

def randomRythm():
    # Choix vitesse de lecture
    print("""
          #-------------------------------#
          #     Génération Aléatoire      #
          #-------------------------------#

          Choix de votre vitesse de lecture : 
          1 : Lent
          2 : Normal
          3 : Rapide
          """)
    user_speed_choice = input()
    speed = ["Lent", "Normal", "Rapide"]
    print(f"""
    #----------------------------------------------------------#
         Vous avez choisi une lecture : {speed[int(user_speed_choice)-1]}
    #----------------------------------------------------------#
        """)

    # Choix du nom du fichier du client
    print("""
          Donner un nom à votre moreau :""")
    user_track_name = input()

    # Ouvre (ou crée) un fichier texte en mode écriture ('w')
    with open(f'samples/{user_track_name}.txt', 'w') as fichier:

        # Faire une boucle avec la liste de note random
        random_int = random.randint(1, 6)

        # Variable first_line_flag pour reperer la premer ligne
        first_line_flag = True
        # déteerminer le temps de la note
        initial_duration = random.randint(80, 125)/1000

        for note in random_notes_list:

            # Ajouter un muliplicatur de durée pour 20% des notes
            multiplier = random.randint(2, 3) if 8 < random.randint(1, 10) else 1
            multiplier *= int(user_speed_choice)
            duration = round(initial_duration * multiplier, 3)

            # Inscrire la première ligne
            if (first_line_flag):
                write = "Unknow " + str(duration) + "\n"
                fichier.write(write)
                first_line_flag = False

            # déterminer le nombre de blanc
            random_int = random.randint(1, 6)
            write = str(note) + " " + str(duration) + "\n"
            fichier.write(write)

            # Reperter le nombre de blanc
            index_flag = 0

            while index_flag < random_int:
                write = "0 " + str(duration) + "\n"
                fichier.write(write)
                index_flag = index_flag + 1

    print(f"""
    #----------------------------------------------------------#
          Votre morceau {user_track_name} a était généré.
          Lecture de votre morceau.
    #----------------------------------------------------------#
          """)

randomRythm()
