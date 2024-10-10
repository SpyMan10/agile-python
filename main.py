import mode
import MusicPlayer
from key_map import KeyMap


def main():
    choice = mode.ask_for_mode()
    if choice == mode.M_FREE_MODE:
        inst = MusicPlayer.choisir_instrument()
        km = KeyMap()
        while True:
            km.read_and_play_seq(inst)
    elif choice == mode.M_RAND_MODE:
        return
    elif choice == mode.M_RELOAD_MODE:
        return


if __name__ == "__main__":
    main()
