import mode
import MusicPlayer
import randseq
import partition_parser as Parser
from mode import M_QUIT
from random_rythm import random_rhythm
import FreqMap as fm
import keyboard
import key_map

def main():
    should_restart = True

    while should_restart:
        # Mode choisi par l'utilisateur (Piano mode, Random mode, Reload mode)
        choice = mode.ask_for_mode()

        if choice == M_QUIT:
            return

        # Instrument choisi par l'utilisateur
        inst = MusicPlayer.choisir_instrument()

        if choice == mode.M_FREE_MODE:
            mp = MusicPlayer.MusicPlayer()
            while True:
                # Attend qu'une touche soit pressée
                event = keyboard.read_event()
                if event.event_type == keyboard.KEY_DOWN:
                    key = event.name
                    if key == 'q':
                        break
                    elif key in key_map.keyboard_to_note:
                        note = key_map.keyboard_to_note[key]
                        frequency = fm.note_to_frequency[note]
                        mp.play_instrument(inst, frequency, 1)
                    else:
                        print("Touche invalide, essaie encore.")
        elif choice == mode.M_RAND_MODE:
            should_ask_for_input = True
            while should_ask_for_input:
                file = random_rhythm(randseq.generate_note_sequence())
                part = Parser.parse_partition(Parser.load_partition("samples/" + file + '.txt'))
                mp = MusicPlayer.MusicPlayer()
                for note in part:
                    mp.play_instrument(inst, note.freq, note.time + 0.25)
                should_ask_for_input = input("Encore (y/n) ? ").strip().lower().startswith("y")
        elif choice == mode.M_RELOAD_MODE:
            file = input('File : ')
            part = Parser.parse_partition(Parser.load_partition("samples/" + file + '.txt'))
            mp = MusicPlayer.MusicPlayer()
            should_ask_for_input = True
            while should_ask_for_input:
                for note in part:
                    t = note.time + 0.25
                    mp.play_instrument(inst, note.freq * 0.3, t)
                should_ask_for_input = input("Encore (y/n) ? ").strip().lower().startswith("y")

        choice = input("Retour au menu principal ? (y/n) ? ")
        print(choice)
        should_restart = choice.strip().lower().startswith("y")

if __name__ == "__main__":
    main()
