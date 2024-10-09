from MusicPlayer import MusicPlayer
import FreqMap as fm

# Fonction pour permettre à l'utilisateur de choisir un instrument
def choose_instrument():
    print("Choisissez un instrument : ")
    print("1. Piano")
    print("2. Guitare")
    print("3. Violon")

    choice = input("Entrez le numéro correspondant à l'instrument : ")

    if choice == '1':
        return 'piano'
    elif choice == '2':
        return 'guitar'
    elif choice == '3':
        return 'violin'
    else:
        print("Choix invalide, piano par défaut.")
        return 'piano'

# Méthode pour appliquer la tonalité en fonction de l'instrument
def apply_instrument_tone(instrument):
    instrument_tones = {
        "piano": 1.0,  # Pas de modification pour le piano
        "guitar": 0.9,  # Légèrement plus bas pour la guitare
        "violin": 1.2  # Légèrement plus haut pour le violon
    }
    return instrument_tones.get(instrument, 1.0)

instrument = choose_instrument()  # Laisse l'utilisateur entrer son choix

tone = apply_instrument_tone(instrument)
print(f"Tonalité appliquée pour {instrument}: {tone}")

