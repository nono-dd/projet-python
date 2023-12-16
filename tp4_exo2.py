import os


# Programme pour déterminer la taille d'un fichier
def taille_fichier(nom_fichier):
    try:
        taille = os.path.getsize(nom_fichier)
        print(f"La taille du fichier {nom_fichier} est de {taille} octets.")
    except FileNotFoundError:
        print(f"Le fichier {nom_fichier} n'a pas été trouvé.")


# Programme pour copier le contenu d'un fichier dans un autre (avec option d'ordre)
def copier_fichier(nom_fichier_source, nom_fichier_destination, ordre_normal=True):
    try:
        with open(nom_fichier_source, 'r') as fichier_source:
            lignes = fichier_source.readlines()
            if not ordre_normal:
                lignes.reverse()

        with open(nom_fichier_destination, 'w') as fichier_destination:
            fichier_destination.writelines(lignes)

        print(f"Le contenu de {nom_fichier_source} a été copié avec succès dans {nom_fichier_destination}.")
    except FileNotFoundError:
        print(f"Le fichier {nom_fichier_source} n'a pas été trouvé.")


# Programme pour afficher les quatre premières lignes d'un fichier
def apercu_fichier(nom_fichier):
    try:
        with open(nom_fichier, 'r') as fichier:
            lignes = fichier.readlines()
            for i in range(min(4, len(lignes))):
                print(lignes[i].strip())
    except FileNotFoundError:
        print(f"Le fichier {nom_fichier} n'a pas été trouvé.")


# Exemple d'utilisation
nom_fichier_apercu = input("Veuillez saisir le nom du fichier pour l'aperçu : ")
apercu_fichier(nom_fichier_apercu)

# Exemple d'utilisation
fichier_source = 'source.txt'
fichier_destination = 'destination.txt'
copier_fichier(fichier_source, fichier_destination, ordre_normal=True)

# Exemple d'utilisation
nom_fichier = 'exemple.txt'
taille_fichier(nom_fichier)
