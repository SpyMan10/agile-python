import pygame
import numpy as np

# Initialisation de pygame
pygame.init()

# Fonction pour permettre à l'utilisateur de choisir un instrument
def choose_instrument():
    print("Choisissez un instrument : ")
    print("1. Piano")
    print("2. Guitare")
    print("3. Violon")

    choice = input("Entrez le numéro correspondant à l'instrument : ")

    if choice == '1':
        return 'piano'
    elif choice == '2':
        return 'guitar'
    elif choice == '3':
        return 'violin'
    else:
        print("Choix invalide, piano par défaut.")
        return 'piano'

# Méthode pour appliquer la tonalité en fonction de l'instrument
def apply_instrument_tone(instrument):
    instrument_tones = {
        "piano": 1.0,  # Pas de modification pour le piano
        "guitar": 0.9,  # Légèrement plus bas pour la guitare
        "violin": 1.2  # Légèrement plus haut pour le violon
    }
    return instrument_tones.get(instrument, 1.0)

# Fonction pour générer une onde sonore
def generate_wave(frequency, duration, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)  # temps
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)  # onde sinusoidale
    return wave

# Fonction pour jouer le son
def _play_tone(tone, duration):
    stereo_tone = np.vstack((tone, tone)).T  # Créer un son stéréo
    contiguous_tone = np.ascontiguousarray((32767 * stereo_tone).astype(np.int16))  # Convertir en format audio
    sound = pygame.sndarray.make_sound(contiguous_tone)  # Créer un objet son
    sound.set_volume(0.05)  # Régler le volume
    sound.play()  # Jouer le son
    pygame.time.delay(int(duration * 1000))  # tenir la note la durée voulue

# Choisir l'instrument et appliquer la tonalité
instrument = choose_instrument()
tone_factor = apply_instrument_tone(instrument)

# Exemple de fréquence pour une note (La 440 Hz)
base_frequency = 440.0  # La note A4
frequency = base_frequency * tone_factor  # Appliquer le facteur de tonalité

# Générer la onde sonore
duration = 2.0  # Durée en secondes
tone = generate_wave(frequency, duration)

# Jouer le son
_play_tone(tone, duration)

# Quitter pygame à la fin
pygame.quit()
