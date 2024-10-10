import os
from play_file_upload import play_file_upload 

def play_samples():
    # Demander à l'utilisateur de saisir le nom du fichier sans avoir à ajouter l'extension .txt
    file_name = input("Entrez le nom du fichier (ex: mario) : ")

    # Ajouter l'extension .txt si elle n'est pas déjà présente
    if not file_name.endswith('.txt'):
        file_name += '.txt'

    file_path = os.path.join("./samples", file_name)
    
    if not os.path.exists(file_path):
        print(f"Erreur : le fichier '{file_name}' n'existe pas dans le répertoire './samples'.")
        return

    # Appeler la fonction pour jouer le fichier
    play_file_upload(file_path)

# Exécuter la fonction
if __name__ == "__main__":
    play_samples()
