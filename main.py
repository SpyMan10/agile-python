import MusicPlayer
import FreqMap as fm

if __name__ == "__main__":
    mp = MusicPlayer.MusicPlayer()
    instrument = MusicPlayer.choisir_instrument()

    # Jouer quelques notes
    mp.play_instrument(instrument, fm.note_to_frequency["B3"], 1)
