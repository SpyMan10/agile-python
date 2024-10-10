
import MusicPlayer

if __name__ == "__main__":
    mp = MusicPlayer.MusicPlayer()
    instrument = MusicPlayer.choisir_instrument()

    # Jouer quelques notes
    mp.play(instrument, MusicPlayer.note_to_frequency["B3"], 1)
