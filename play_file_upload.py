from MusicPlayer import MusicPlayer
import FreqMap as fm
from load_partition import load_partition
from partition_parser import parse_partition
import pygame


def play_file_upload(chemin_fichier, temps_pause):
    # Chemin vers le fichier de partition

    # Charger le fichier de partition
    lines = load_partition(chemin_fichier)

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
