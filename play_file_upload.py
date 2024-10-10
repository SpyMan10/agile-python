from MusicPlayer import MusicPlayer
import FreqMap as fm
from load_partition import load_partition
from partition_parser import parse_partition
import pygame

def play_file_upload(file_path):
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
            pygame.time.delay(int(duration * 1000))  # Attend la durée du silence
        else:
            frequency = fm.note_to_frequency.get(note)
            if frequency:
                mp._play(frequency, duration)  # Appeler la méthode _play directement
            else:
                print(f"Note inconnue : {note}, ignorée")
