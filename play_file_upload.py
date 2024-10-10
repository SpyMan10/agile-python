from MusicPlayer import MusicPlayer
import FreqMap as fm
from load_partition import load_partition
from partition_parser import parse_partition
import pygame
import os

def play_file_upload(temps_pause):
    # Demander à l'utilisateur de saisir le nom du fichier sans avoir à ajouter l'extension .txt
    file_name = input("Entrez le nom du fichier (ex: mario) : ")

    # Ajouter l'extension .txt si elle n'est pas déjà présente
    if not file_name.endswith('.txt'):
        file_name += '.txt'

    file_path = os.path.join("./samples", file_name)
    
    if not os.path.exists(file_path):
        print(f"Erreur : le fichier '{file_name}' n'existe pas dans le répertoire './samples'.")
        return

    # Charger le fichier de partition
    lines = load_partition(file_path)

    # Parser la partition
    sequence = parse_partition(lines)

    # Créer une instance de MusicPlayer
    mp = MusicPlayer()

    # Jouer la séquence
    for note, duration in sequence:
        if note == "silence":
            # Ignorer les silences, juste attendre la durée
            pygame.time.delay(int(duration * temps_pause))  # Attend la durée du silence
        else:
            frequency = fm.note_to_frequency.get(note)
            if frequency:
                mp.play(frequency, duration)
            else:
                print(f"Note inconnue : {note}, ignorée")

if __name__ == "__main__":
    temps_pause = 1000
    play_file_upload(temps_pause)
