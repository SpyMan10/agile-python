![MusicaLau !](/assets/image/image.png "image")

## Projet d'application musicale pour MusicaLau

MusicaLau, un magasin d'instruments de musique, souhaite élargir sa clientèle en s'adressant à des acheteurs avec des revenus plus faibles. L'idée est de proposer une application musicale avec les fonctionnalités suivantes :

- Permettre aux utilisateurs de créer de la musique en choisissant un instrument virtuel.
- Offrir la possibilité de jouer des notes et de générer des séquences musicales aléatoires avec un rythme défini.
- Permettre la lecture de partitions depuis des fichiers. Un exemple de format est disponible sur Moodle, car les clients pourraient vouloir utiliser des partitions qu'ils trouvent sur internet.

## Présentation de l'application

Pour pouvoir lancer l'application rentrer la commande python ./main.py.
Le programme s'exécute et vous avez ceci qui apparaît :
![Phase0 !](/assets/image/phase0.png "Phase0")

Il vous propose de choisir un mode:

1. **0: Mode libre** Ce mode vous permet de jouer librement avec l'instrument de votre choix.
2. **1: Génération aléatoire de séquence musicale** Ce mode vous permet de générer une séquence musicale aléatoire avec l'instrument de votre choix.
3. **2: Relecture de partitions** Ce mode vous permet de lire des séquences enregistrer avec l'instrument de votre choix.

#### Si vous choisissez le mode 0

![Phase0 !](/assets/image/phase000.png "Phase0")

Vous devez choisir en premier temps un instrument.

Puis vous jouer votre séquence.

![Phase0 !](/assets/image/phase00.png "Phase0")

Après avoir jouer votre séquence on vous demande si vous voulez rejouer une autre séquence (y) ou quitter et revenir a umenu principal (n).

#### Si vous choisissez le mode 1

![Phase0 !](/assets/image/phase1.png "Phase0")

Comme avant on vous demande de choisir un instrument.
On vous demande ensuite la vitesse de lecture.

![Phase0 !](/assets/image/phase11.png "Phase0")

Puis donner un nom au morceau.

**Le morceau est joué.**

#### Si vous choisissez le mode 2

![Phase0 !](/assets/image/phase2.png "Phase0")

Comme avant on vous demande de choisir un instrument.
Et le fichier que vous voulez lire.

**Le fichier ce joue.**

## Les différentes fonctions mises en place pour la réalisation du projet

- **play_samples** : permet la lecture de partitions depuis des fichiers
- **randseq.py** : permet de generer des notes aléatoires

### Comment les utiliser

Pour pouvoir exécuter ces commandes vous devez vous rendre dans votre terminal,
vous placez dans le dossier agile-python et écrire cette commande : **python ./nom_du_fichier.py**
