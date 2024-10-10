def load_partition(chemin_fichier):
    with open(chemin_fichier, 'r') as fichier:
        lignes = fichier.readlines()
        return lignes
    

    