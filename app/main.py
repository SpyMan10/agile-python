import MusicPlayer
import FreqMap as fm

# code exemple pour jouer des notes :
if __name__ == "__main__" :
    mp = MusicPlayer()
    mp.play(fm.note_to_frequency["F7"], 1)
    mp.play(fm.note_to_frequency["B3"], 4)
    mp.play(fm.note_to_frequency["E5"], 0.5)