from FreqMap import note_to_frequency as ntf
from MusicPlayer import MusicPlayer
import pygame as pg

class Key:
    _level: int
    _note: str

    def __init__(self, lvl: int, note: str):
        self._level = lvl
        self._note = note

    @property
    def note(self) -> int:
        return self._note
    
    @property
    def level(self) -> int:
        return self._level


class KeyMap:
    KEYS = [
        {
            'A': 'A1',
            'Z': 'B1',
            'E': 'C1',
            'R': 'D1',
            'T': 'E1',
            'Y': 'F1',
            'U': 'G1'
        },
        {
            'Q': 'A2',
            'S': 'B2',
            'D': 'C2',
            'F': 'D2',
            'G': 'E2',
            'H': 'F2',
            'J': 'G2'
        },
        {
            'X': 'A3',
            'C': 'B3',
            'V': 'C3',
            'B': 'D3',
            'N': 'E3',
            '?': 'F3',
            '.': 'G3'
        }
    ]


    def read_key_seq(self) -> list[Key]:
        seq = input('Sequence: ').upper()
        ls: list[str] = []
        if len(seq) == 0:
            return []
        for c in seq:
            k = self.map_key(c)
            if k is not None:
                ls.append(k)
        return ls
        

    def map_key(self, key: str) -> Key | None:
        for ks in self.KEYS:
            if key in ks:
                return Key(self.KEYS.index(ks), ks[key])
        return None
    

    def read_and_play_seq(self):
        seq = self.read_key_seq()
        player = MusicPlayer()
        for k in seq:
            player.play(ntf[k.note] * (k.level * 0.2), 1.0)

