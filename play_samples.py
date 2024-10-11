import os
from play_file_upload import play_file_upload

def play_samples():
    # Lister les fichiers .txt dans le répertoire "./samples"
    files = [f for f in os.listdir("./samples") if f.endswith('.txt')]

    if not files:
        print("Aucun fichier disponible dans le répertoire './samples'.")
        return

    # Afficher la liste des fichiers disponibles
    print("Fichiers disponibles :")
    for i, file in enumerate(files):
        print(f"{i + 1}. {file[:-4]}")  # Afficher le nom sans l'extension .txt

    # Demander à l'utilisateur de sélectionner un fichier
    try:
        file_choice = int(input(f"Entrez le numéro du fichier à jouer (1-{len(files)}) : "))
        if 1 <= file_choice <= len(files):
            file_name = files[file_choice - 1]
        else:
            print("Numéro invalide.")
            return
    except ValueError:
        print("Entrée non valide.")
        return

    file_path = os.path.join("./samples", file_name)

    # Appeler la fonction pour jouer le fichier
    play_file_upload(file_path)

# Exécuter la fonction
if __name__ == "__main__":
    play_samples()
