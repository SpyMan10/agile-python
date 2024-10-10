
from app.MusicPlayer import MusicPlayer  # Importer la classe MusicPlayer



player = MusicPlayer()

# Génération d'une séquence de notes
sequence = player.generate_note_sequence(min_notes=10, max_notes=20)

# Optionnel : Appliquer un rythme ici, en assignant des durées aux notes si besoin

# Jouer la séquence

# player.play_sequence(sequence)
# for seq in sequence:
#     print(seq)


print(sequence)

