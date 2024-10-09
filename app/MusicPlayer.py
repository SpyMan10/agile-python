# installer avec: pip install pygame
#                 pip install numpy 
      
import numpy as np
import pygame

from app.FreqMap import note_to_frequency



import numpy as np
import pygame
import random
from app.FreqMap import note_to_frequency

class MusicPlayer:
    def __init__(self, sample_rate=44100):
        pygame.mixer.init(frequency=sample_rate, size=-16, channels=2)
        self.sample_rate = sample_rate

    # Méthode pour générer une séquence de noms de notes aléatoires
    def generate_note_sequence(self, min_notes=10, max_notes=20):
        num_notes = random.randint(min_notes, max_notes)
        sequence = []

        for _ in range(num_notes):
            note_name = random.choice(list(note_to_frequency.keys()))
            sequence.append(note_name)  # Ajouter uniquement le nom de la note

        return sequence

    # Méthode pour jouer une seule note avec une durée fixe
    def play(self, note_name, duration=1.0):
        frequency = note_to_frequency[note_name]  # Récupérer la fréquence de la note
        t = np.linspace(0, duration, int(self.sample_rate * duration), False)
        tone = np.sin(frequency * 2 * np.pi * t)

        stereo_tone = np.vstack((tone, tone)).T
        contiguous_tone = np.ascontiguousarray((32767 * stereo_tone).astype(np.int16))

        sound = pygame.sndarray.make_sound(contiguous_tone)
        sound.set_volume(0.05)
        sound.play()
        pygame.time.delay(int(duration * 1000))  # multiplier par 1000 pour convertir en millisecondes

    # Méthode pour jouer une séquence de notes avec une durée fixe par note
    def play_sequence(self, sequence, fixed_duration=1.0):
        for note_name in sequence:
            self.play(note_name, fixed_duration)





# second
# classe qui permet de jouer de la musique grâce à pygame
import numpy as np
import pygame
import random
from app.FreqMap import note_to_frequency

# Classe Note pour stocker le nom et la fréquence
# class Note:
#     def __init__(self, name, frequency):
#         self.name = name
#         self.frequency = frequency
#         self.duration = 0  # initialisé à 0, on peut définir la durée plus tard
#
#     def __repr__(self):
#         return f"Note: {self.name}, Frequency: {self.frequency}, Duration: {self.duration}"
#
# # Classe qui permet de jouer de la musique grâce à pygame
# class MusicPlayer:
#     def __init__(self, sample_rate=44100):
#         pygame.mixer.init(frequency=sample_rate, size=-16, channels=2)
#         self.sample_rate = sample_rate
#
#     # Méthode pour générer une séquence de notes aléatoires
#     def generate_note_sequence(self, min_notes=10, max_notes=20):
#         num_notes = random.randint(min_notes, max_notes)
#         sequence = []
#
#         for _ in range(num_notes):
#             note_name = random.choice(list(note_to_frequency.keys()))
#             frequency = note_to_frequency[note_name]
#             note = Note(name=note_name, frequency=frequency)
#             sequence.append(note)
#
#         return sequence
#
#     # Exemple de tonalité, extraire ce qui va bien pour pouvoir faire varier, pour simuler différents instruments
#     def play(self, frequency, duration):
#         t = np.linspace(0, duration, int(self.sample_rate * duration), False)
#         tone = np.sin(frequency * 2 * np.pi * t)
#
#         stereo_tone = np.vstack((tone, tone)).T
#         contiguous_tone = np.ascontiguousarray((32767 * stereo_tone).astype(np.int16))
#
#         sound = pygame.sndarray.make_sound(contiguous_tone)
#         sound.set_volume(0.05)
#         sound.play()
#         pygame.time.delay(int(duration * 1000))  # multiplier par 1000 pour convertir en millisecondes

    # Méthode pour jouer une séquence de notes
    # def play_sequence(self, sequence, default_duration=1.0):
    #     for note in sequence:
    #         self.play(note.frequency, note.duration or default_duration)  # Utilise la durée de la note, ou une durée par défaut
    #

