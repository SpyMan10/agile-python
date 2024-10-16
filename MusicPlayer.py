import numpy as np
import pygame


# classe qui permet de jouer de la musique grâce à pygame
class MusicPlayer:
    def __init__(self, sample_rate=44100):
        pygame.mixer.init(frequency=sample_rate, size=-16, channels=2)
        self.sample_rate = sample_rate

    # Générer une enveloppe ADSR (Attack, Decay, Sustain, Release)
    def _apply_adsr(self, tone: float, duration: float):
        attack_time = 0.1  # Temps d'attaque
        decay_time = 0.2  # Temps de décroissance
        sustain_level = 0.7  # Niveau de maintien
        release_time = 0.2  # Temps de relâchement

        n_samples = int(self.sample_rate * duration)

        envelope = np.ones_like(tone)

        # Attack phase
        attack_samples = int(self.sample_rate * attack_time)
        envelope[:attack_samples] = np.linspace(0, 1, attack_samples)

        # Decay phase
        decay_samples = int(self.sample_rate * decay_time)
        decay_start = attack_samples
        decay_end = attack_samples + decay_samples
        envelope[decay_start:decay_end] = np.linspace(1, sustain_level, decay_samples)

        # Sustain phase
        sustain_start = decay_end
        sustain_end = n_samples - int(self.sample_rate * release_time)
        envelope[sustain_start:sustain_end] = sustain_level

        # Release phase
        release_start = sustain_end
        envelope[release_start:] = np.linspace(sustain_level, 0, n_samples - release_start)

        return tone * envelope

    # Méthode pour générer une onde sinusoïdale avec harmoniques (piano)
    def _generate_piano_tone(self, frequency, duration):
        t = np.linspace(0, duration, int(self.sample_rate * duration), False)
        # Ajout d'harmoniques avec des coefficients plus faibles pour les ordres supérieurs
        tone = 0.2 * np.sin(2 * frequency * 2 * np.pi * t)  # 2ème harmonique
        # tone += 0.25 * np.sin(3 * frequency * 2 * np.pi * t)  # 3ème harmonique
        tone += 0.3 * np.sin(6 * frequency * 2 * np.pi * t)  # 4ème harmonique
        tone += 0.4 * np.sin(5 * frequency * 2 * np.pi * t)  # 5ème harmonique
        return self._apply_adsr(tone, duration)

    # Méthode pour générer une onde triangulaire avec harmoniques (guitare)
    def _generate_guitar_tone(self, frequency, duration):
        t = np.linspace(0, duration, int(self.sample_rate * duration), False)

        tone = (t * frequency - np.floor(0.5 + t * frequency))  # Onde en dents de scie
        # Ajout d'harmoniques
        # tone += 0.5 * np.sin(2 * frequency * 2 * np.pi * t)  # 2ème harmonique
        tone += 0.2 * np.sin(3 * frequency * 2 * np.pi * t)  # 3ème harmonique
        tone += 0.15 * np.sin(4 * frequency * 2 * np.pi * t)  # 4ème harmonique
        tone += 0.10 * np.sin(5 * frequency * 2 * np.pi * t)  # 5ème harmonique
        tone += 0.05 * np.sin(5 * frequency * 2 * np.pi * t)  # 5ème harmonique

        return self._apply_adsr(tone, duration)

    # Méthode pour générer une onde en dents de scie avec harmoniques (violon)
    def _generate_violin_tone(self, frequency, duration):
        t = np.linspace(0, duration, int(self.sample_rate * duration), False)
        tone = 0.2 * (t * frequency - np.floor(0.5 + t * frequency))  # Onde en dents de scie
        # Ajout d'harmoniques
        # tone += 0.5 * np.sin(2 * frequency * 2 * np.pi * t)  # 2ème harmonique
        tone += 0.25 * np.sin(3 * frequency * 2 * np.pi * t)  # 3ème harmonique
        tone += 0.2 * np.sin(4 * frequency * 2 * np.pi * t)  # 4ème harmonique
        tone += 0.15 * np.sin(5 * frequency * 2 * np.pi * t)  # 5ème harmonique
        tone += 0.1 * np.sin(5 * frequency * 2 * np.pi * t)  # 5ème harmonique
        return self._apply_adsr(tone, duration)

    # Jouer le son correspondant à l'instrument choisi
    def play_instrument(self, instrument: str, frequency: float, duration: float):
        tone = 0

        if instrument == "piano":
            tone = self._generate_piano_tone(frequency, duration)
        elif instrument == "guitare":
            tone = self._generate_guitar_tone(frequency, duration)
        elif instrument == "violon":
            tone = self._generate_violin_tone(frequency, duration)
        else:
            print("Instrument inconnu")
            return

        # Créer un tableau stéréo (2D) en dupliquant le ton
        stereo_tone = np.vstack((tone, tone)).T

        # S'assurer que le tableau est contigu en mémoire
        contiguous_tone = np.ascontiguousarray((32767 * stereo_tone).astype(np.int16))

        # Convertir l'onde en un format audio et jouer
        sound = pygame.sndarray.make_sound(contiguous_tone)
        sound.set_volume(0.05)  # Réglez le volume
        sound.play()
        pygame.time.delay(int(duration * 1000))

    # cette méthode pourra être appelée ensuite quelque soit l'instrument choisis
    def _play_tone(self, tone, duration):
        stereo_tone = np.vstack((tone, tone)).T
        contiguous_tone = np.ascontiguousarray((32767 * stereo_tone).astype(np.int16))
        sound = pygame.sndarray.make_sound(contiguous_tone)
        sound.set_volume(0.05)  # Réglez le volume
        sound.play()
        pygame.time.delay(int(duration * 1000))  # tenir la note la durée voulue

    def _play(self, frequency, duration):
        # Créer une onde sinusoïdale à la fréquence spécifiée
        t = np.linspace(0, duration, int(self.sample_rate * duration), False)
        tone = np.sin(frequency * 2 * np.pi * t)

        # Créer un tableau stéréo (2D) en dupliquant le ton
        stereo_tone = np.vstack((tone, tone)).T

        # S'assurer que le tableau est contigu en mémoire
        contiguous_tone = np.ascontiguousarray((32767 * stereo_tone).astype(np.int16))

        # Convertir l'onde sinusoïdale en un format audio et jouer
        sound = pygame.sndarray.make_sound(contiguous_tone)
        sound.set_volume(0.05)  # Réglez le volume
        sound.play()
        pygame.time.delay(int(duration * 500))

    # Demander à l'utilisateur de choisir un instrument


def choisir_instrument():
    print("Choisissez un instrument : piano, guitare, violon")
    instrument = input("Entrez l'instrument: ").strip().lower()
    if instrument not in ["piano", "guitare", "violon"]:
        print("Instrument invalide, choix par défaut: piano")
        return "piano"
    return instrument