import mode
import MusicPlayer
import randseq
from key_map import KeyMap
from load_partition import load_partition
from partition_parser import parse_partition
from random_rythm import random_rhythm
from FreqMap import note_to_frequency as nf


def main():
    # Mode choisi par l'utilisateur (Piano mode, Random mode, Reload mode)
    choice = mode.ask_for_mode()

    # Instrument choisi par l'utilisateur
    inst = MusicPlayer.choisir_instrument()

    should_ask_for_input = True

    if choice == mode.M_FREE_MODE:
        km = KeyMap()
        should_ask_for_input = True
        while should_ask_for_input:
            km.read_and_play_seq(inst)
            should_ask_for_input = input("Encore (y/n) ? ").strip().lower().startswith("y")
    elif choice == mode.M_RAND_MODE:
        while should_ask_for_input:
            file = random_rhythm(randseq.generate_note_sequence())
            part = parse_partition(load_partition("samples/" + file + '.txt'))
            mp = MusicPlayer.MusicPlayer()
            for (k, v) in part:
                print(k, v)
                mp.play_instrument(inst, None if k is None else v, 1)
            should_ask_for_input = input("Encore (y/n) ? ").strip().lower().startswith("y")
    elif choice == mode.M_RELOAD_MODE:
        file = input('File : ')
        part = parse_partition(load_partition("samples/" + file + '.txt'))
        mp = MusicPlayer.MusicPlayer()
        while should_ask_for_input:
            for (k, v) in part:
                f = nf[k if k in nf.keys() else 'B0']
                mp.play_instrument(inst, f, v)
            should_ask_for_input = input("Encore (y/n) ? ").strip().lower().startswith("y")


if __name__ == "__main__":
    main()
