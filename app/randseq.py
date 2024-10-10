import random
from FreqMap import note_to_frequency

def generate_note_sequence(self, min_notes=10, max_notes=20):
    num_notes = random.randint(min_notes, max_notes)
    sequence = []

    # Récupérer les noms des notes et leur index
    note_names = list(note_to_frequency.keys())
    center_index = note_names.index("C4")  # Note centrale autour de laquelle distribuer
    std_dev = 5  # Écart-type pour la distribution

    for _ in range(num_notes):
        # Générer un indice autour du centre avec une distribution gaussienne
        note_index = int(random.gauss(center_index, std_dev))

        # S'assurer que l'indice est dans les limites de la liste
        note_index = max(0, min(note_index, len(note_names) - 1))

        # Récupérer le nom de la note correspondant à l'indice
        note_name = note_names[note_index]
        sequence.append(note_name)  # Ajouter uniquement le nom de la note

    return sequence