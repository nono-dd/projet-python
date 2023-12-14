def annee_bissextile():
    print("Bonjour bienvenue dans le programme qui determine l'annee bissextile ")
    anni_users = None
    while anni_users is None or type(anni_users) == str:
        anni_users = input("Entrer une anne a verifier : ")
        try:
            anni_users = int(anni_users)
        except ValueError:
            print("{} n'est pas un age valide".format(anni_users))
    if anni_users % 4 != 0:
        print("Desole mais cette annee n'est pas bissextile")
    elif anni_users % 100 == 0:
        if anni_users % 400 == 0:
            print("BISSEXTILE")
        else:
            print("NON bissextile !!")

   # print("Table de multiplication")
   # nbr = int(input("ENtrer un nombre pour une table de multiplication : "))
    #i = 0
    #while i < 10:
     #   print("=", i * nbr)
      #  i += 1

def chane():
    chaiine = " Bonjour les noobs"
    for lettre in chaiine:
        if lettre in "oqaecjemqdnzr":
            print(lettre)
        else:
            print(" * * ")

class VDP:
    def __init__(self, matricule, nom, prenom, jour_enrolement, mois_enrolement, annee_enrolement):
        self.matricule = matricule
        self.nom = nom
        self.prenom = prenom
        self.jour_enrolement = jour_enrolement
        self.mois_enrolement = mois_enrolement
        self.annee_enrolement = annee_enrolement

    def afficher_informations(self):
        print("Matricule : {}".format(self.matricule))
        print(f"Nom : {self.nom}")
        print(f"Prénom : {self.prenom}")
        print(f"Date d'enrôlement : {self.jour_enrolement}/{self.mois_enrolement}/{self.annee_enrolement}")

    # Nom des fichiers d'entrée
fichier1 = "fichier1.txt"
fichier2 = "fichier2.txt"

# Nom du fichier de sortie
fichier_sortie = "union_triee_sans_doublons.txt"

# Ouvrir les fichiers d'entrée en mode lecture
with open(fichier1, 'r') as file1, open(fichier2, 'r') as file2:
    # Lire les données des fichiers et les stocker dans des ensembles pour éliminer les doublons
    ensemble1 = set(file1.read().splitlines())
    ensemble2 = set(file2.read().splitlines())

    # Fusionner les ensembles triés en les convertissant en listes
    union_triee = sorted(ensemble1.union(ensemble2))

# Écrire le résultat dans un fichier de sortie
with open(fichier_sortie, 'w') as output_file:
    for element in union_triee:
        output_file.write(element + "\n")

print("Union triée sans doublons écrite dans", fichier_sortie)



if __name__ == '__main__':
    # annee_bissextile()
    # vdp1 = VDP(1, "Doe", "John", 15, 6, 2022)
    # vdp2 = VDP(2, "Smith", "Alice", 25, 3, 2023)
    print(1, 2, 3, sep="-....-")
    # vdp1.afficher_informations()
    # vdp2.afficher_informations()

    # tu as  aussi vue la l'intruction lambda qui sert comme def mais plus specifique
    # #
