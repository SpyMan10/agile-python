M_FREE_MODE = 0
M_RAND_MODE = 1
M_RELOAD_MODE = 2
ALL_MODES = [M_FREE_MODE, M_RAND_MODE, M_RELOAD_MODE]

def ask_for_mode() -> int:
    """
    Demande à l'utilisateur ce qu'il souhaite faire.
    0: Mode libre (joue des notes avec le clavier du PC)
    1: Génération aléatoire de séquence musicale.
    2: Relecture de partitions (fichier texte).

    :return: Mode as int (0, 1 and 2)
    """

    print("0: Mode libre (joue des notes avec le clavier du PC)")
    print("1: Génération aléatoire de séquence musicale.")
    print("2: Relecture de partitions (fichier texte).")
    # Blank line
    print()

    while True:
        val = input("Mode : ")
        try:
            choice = int(val)
            if choice in ALL_MODES:
                return choice
        except ValueError:
            print("[Error]: Choice invalide !, choisir parmis les propositons ci-dessus.")

