note_to_frequency = {
    "B0": 31,
    "C1": 33,
    "C#1": 35,  # or "Db1": 35
    "D1": 37,
    "D#1": 39,  # or "Eb1": 39
    "E1": 41,
    "F1": 44,
    "F#1": 46,  # or "Gb1": 46
    "G1": 49,
    "G#1": 52,  # or "Ab1": 52
    "A1": 55,
    "A#1": 58,  # or "Bb1": 58
    "B1": 62,
    "C2": 65,
    "C#2": 69,  # or "Db2": 69
    "D2": 73,
    "D#2": 78,  # or "Eb2": 78
    "E2": 82,
    "F2": 87,
    "F#2": 93,  # or "Gb2": 93
    "G2": 98,
    "G#2": 104,  # or "Ab2": 104
    "A2": 110,
    "A#2": 117,  # or "Bb2": 117
    "B2": 123,
    "C3": 131,
    "C#3": 139,  # or "Db3": 139
    "D3": 147,
    "D#3": 156,  # or "Eb3": 156
    "E3": 165,
    "F3": 175,
    "F#3": 185,  # or "Gb3": 185
    "G3": 196,
    "G#3": 208,  # or "Ab3": 208
    "A3": 220,
    "A#3": 233,  # or "Bb3": 233
    "B3": 247,
    "C4": 262,
    "C#4": 277,  # or "Db4": 277
    "D4": 294,
    "D#4": 311,  # or "Eb4": 311
    "E4": 330,
    "F4": 349,
    "F#4": 370,  # or "Gb4": 370
    "G4": 392,
    "G#4": 415,  # or "Ab4": 415
    "A4": 440,
    "A#4": 466,  # or "Bb4": 466
    "B4": 494,
    "C5": 523,
    "C#5": 554,  # or "Db5": 554
    "D5": 587,
    "D#5": 622,  # or "Eb5": 622
    "E5": 659,
    "F5": 698,
    "F#5": 740,  # or "Gb5": 740
    "G5": 784,
    "G#5": 831,  # or "Ab5": 831
    "A5": 880,
    "A#5": 932,  # or "Bb5": 932
    "B5": 988,
    "C6": 1047,
    "C#6": 1109,  # or "Db6": 1109
    "D6": 1175,
    "D#6": 1245,  # or "Eb6": 1245
    "E6": 1319,
    "F6": 1397,
    "F#6": 1480,  # or "Gb6": 1480
    "G6": 1568,
    "G#6": 1661,  # or "Ab6": 1661
    "A6": 1760,
    "A#6": 1865,  # or "Bb6": 1865
    "B6": 1976,
    "C7": 2093,
    "C#7": 2217,  # or "Db7": 2217
    "D7": 2349,
    "D#7": 2489,  # or "Eb7": 2489
    "E7": 2637,
    "F7": 2794,
    "F#7": 2960,  # or "Gb7": 2960
    "G7": 3136,
    "G#7": 3322,  # or "Ab7": 3322
    "A7": 3520,
    "A#7": 3729,  # or "Bb7": 3729
    "B7": 3951,
    "C8": 4186,
    "C#8": 4435,  # or "Db8": 4435
    "D8": 4699,
    "D#8": 4978,  # or "Eb8": 4978
}


# Fonction pour générer une séquence de notes
def generate_note_sequence(min_notes=10, max_notes=20):
    # Générer un nombre aléatoire de notes dans l'intervalle spécifié
    num_notes = random.randint(min_notes, max_notes)

    # Générer la liste de notes
    sequence = []
    for _ in range(num_notes):
        note_name = random.choice(list(note_to_frequency.keys()))
        frequency = note_to_frequency[note_name]
        note = Note(name=note_name, frequency=frequency)
        sequence.append(note)

    return sequence