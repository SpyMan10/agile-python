import FreqMap as fm

class Note:
    _freq: float
    _time: float

    def __init__(self, frequency: float, time: float):
        self._freq = frequency
        self._time = time

    @property
    def freq(self):
        return self._freq

    @property
    def time(self):
        return self._time


def load_partition(filepath: str) -> list[str]:
    with open(filepath, 'r') as file:
        lines =  file.readlines()
    return lines

def parse_partition(lines) -> list[Note]:
    sequence = []
    for line in lines:
        # Split line using blank space
        # [Note name] <space> [Note duration]
        parts = line.strip().split(sep=' ')
        if len(parts) != 2:
            print(f"Ligne ignorée (format incorrect) : {line}")
            continue

        try:
            note_str = parts[0].strip()
            if note_str != '0':
                freq = fm.note_to_frequency[note_str]
                try:
                    duration = float(parts[1])
                    sequence.append(Note(freq, duration))
                except ValueError:
                    print(f"Durée invalide sur la ligne : {line}")
                    continue
        except KeyError:
            continue

    return sequence
