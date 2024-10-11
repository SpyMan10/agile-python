# from FreqMap import note_to_frequency as ntf
# from MusicPlayer import MusicPlayer
# import pygame as pg
#
# class Key:
#     _level: int
#     _note: str
#
#     def __init__(self, lvl: int, note: str):
#         self._level = lvl
#         self._note = note
#
#     @property
#     def note(self) -> int:
#         return self._note
#
#     @property
#     def level(self) -> int:
#         return self._level
#
#
# class KeyMap:
#     KEYS = [
#         {
#             'A': 'A1',
#             'Z': 'B1',
#             'E': 'C1',
#             'R': 'D1',
#             'T': 'E1',
#             'Y': 'F1',
#             'U': 'G1'
#         },
#         {
#             'Q': 'A2',
#             'S': 'B2',
#             'D': 'C2',
#             'F': 'D2',
#             'G': 'E2',
#             'H': 'F2',
#             'J': 'G2'
#         },
#         {
#             'X': 'A3',
#             'C': 'B3',
#             'V': 'C3',
#             'B': 'D3',
#             'N': 'E3',
#             '?': 'F3',
#             '.': 'G3'
#         }
#     ]
#
#
#     def read_key_seq(self) -> list[Key]:
#         seq = input('Sequence: ').upper()
#         ls: list[str] = []
#         if len(seq) == 0:
#             return []
#         for c in seq:
#             k = self.map_key(c)
#             if k is not None:
#                 ls.append(k)
#         return ls
#
#
#     def map_key(self, key: str) -> Key | None:
#         for ks in self.KEYS:
#             if key in ks:
#                 return Key(self.KEYS.index(ks), ks[key])
#         return None
#
#
#     def read_and_play_seq(self):
#         seq = self.read_key_seq()
#         player = MusicPlayer()
#         for k in seq:
#             player.play(ntf[k.note] * (k.level * 0.2), 1.0)
#

import pygame
import numpy as np
import keyboard

# Initialisation de Pygame
pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=1)

# Dictionnaire de fréquences complet avec dièses
note_to_frequency = {
    "B0": 31,
    "C1": 33, "C#1": 35,  # or "Db1": 35
    "D1": 37, "D#1": 39,  # or "Eb1": 39
    "E1": 41,
    "F1": 44, "F#1": 46,  # or "Gb1": 46
    "G1": 49, "G#1": 52,  # or "Ab1": 52
    "A1": 55, "A#1": 58,  # or "Bb1": 58
    "B1": 62,
    "C2": 65, "C#2": 69,  # or "Db2": 69
    "D2": 73, "D#2": 78,  # or "Eb2": 78
    "E2": 82,
    "F2": 87, "F#2": 93,  # or "Gb2": 93
    "G2": 98, "G#2": 104,  # or "Ab2": 104
    "A2": 110, "A#2": 117,  # or "Bb2": 117
    "B2": 123,
    "C3": 131, "C#3": 139,  # or "Db3": 139
    "D3": 147, "D#3": 156,  # or "Eb3": 156
    "E3": 165,
    "F3": 175, "F#3": 185,  # or "Gb3": 185
    "G3": 196, "G#3": 208,  # or "Ab3": 208
    "A3": 220, "A#3": 233,  # or "Bb3": 233
    "B3": 247,
    "C4": 262, "C#4": 277,  # or "Db4": 277
    "D4": 294, "D#4": 311,  # or "Eb4": 311
    "E4": 330,
    "F4": 349, "F#4": 370,  # or "Gb4": 370
    "G4": 392, "G#4": 415,  # or "Ab4": 415
    "A4": 440, "A#4": 466,  # or "Bb4": 466
    "B4": 494,
    "C5": 523, "C#5": 554,  # or "Db5": 554
    "D5": 587, "D#5": 622,  # or "Eb5": 622
    "E5": 659,
    "F5": 698, "F#5": 740,  # or "Gb5": 740
    "G5": 784, "G#5": 831,  # or "Ab5": 831
    "A5": 880, "A#5": 932,  # or "Bb5": 932
    "B5": 988,
    "C6": 1047, "C#6": 1109,  # or "Db6": 1109
    "D6": 1175, "D#6": 1245,  # or "Eb6": 1245
    "E6": 1319,
    "F6": 1397, "F#6": 1480,  # or "Gb6": 1480
    "G6": 1568, "G#6": 1661,  # or "Ab6": 1661
    "A6": 1760, "A#6": 1865,  # or "Bb6": 1865
    "B6": 1976,
    "C7": 2093, "C#7": 2217,  # or "Db7": 2217
    "D7": 2349, "D#7": 2489,  # or "Eb7": 2489
    "E7": 2637,
    "F7": 2794, "F#7": 2960,  # or "Gb7": 2960
    "G7": 3136, "G#7": 3322,  # or "Ab7": 3322
    "A7": 3520, "A#7": 3729,  # or "Bb7": 3729
    "B7": 3951,
    "C8": 4186, "C#8": 4435,  # or "Db8": 4435
    "D8": 4699, "D#8": 4978  # or "Eb8": 4978
}

# Dictionnaire liant les touches du clavier aux notes
keyboard_to_note = {
    "a": "C4",  # a = Do
    "z": "D4",  # z = Ré
    "e": "E4",  # e = Mi
    "r": "F4",  # r = Fa
    "t": "G4",  # t = Sol
    "y": "A4",  # y = La
    "u": "B4",  # u = Si
    "2": "C#4",  # 2 = Do#
    "3": "D#4",  # 3 = Ré#
    "5": "F#4",  # 5 = Fa#
    "6": "G#4",  # 6 = Sol#
    "7": "A#4",  # 7 = La#
    "v": "C5",  # v = Do octave supérieure
    "b": "D5",  # b = Ré
    "n": "E5",  # n = Mi
    "m": "F5",  # m = Fa
    ",": "G5",  # , = Sol
    ".": "A5",  # . = La
    "g": "C#5",  # g = Do# octave supérieure
    "h": "D#5",  # h = Ré#
    "k": "F#5",  # k = Fa#
    "l": "G#5",  # l = Sol#
    ";": "A#5"  # ; = La#
}


# Fonction pour générer une onde sinusoïdale
def generate_sine_wave(frequency, duration, sample_rate=44100, amplitude=4096):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = amplitude * np.sin(2 * np.pi * frequency * t)
    return np.array(wave, dtype=np.int16)


# Fonction pour jouer une note
def play_note(frequency, duration=1):
    # print(f"Jouer la note à {frequency} Hz pour {duration} seconde(s)...")

    wave = generate_sine_wave(frequency, duration)
    stereo_wave = np.array([wave, wave]).T
    sound_array = np.ascontiguousarray(stereo_wave)

    try:
        sound = pygame.sndarray.make_sound(sound_array)
    except Exception as e:
        print(f"Erreur lors de la création du son : {e}")
        return

    sound.play()
    pygame.time.delay(int(duration * 800))
    sound.stop()


# Fonction principale
def main():
    print("Appuie sur une touche pour jouer une note. Appuie sur 'q' pour quitter.")

    while True:
        # Attend qu'une touche soit pressée
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            key = event.name
            if key == 'q':
                print("Fermeture du programme.")
                break
            elif key in keyboard_to_note:
                note = keyboard_to_note[key]
                frequency = note_to_frequency[note]
                play_note(frequency, duration=1)
            else:
                print("Touche invalide, essaie encore.")

    pygame.quit()


# Exécuter la fonction principale
if __name__ == "__main__":
    main()
