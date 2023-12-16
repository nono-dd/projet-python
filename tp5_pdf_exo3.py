class Etudiant:
    def __init__(self, nom, prenom, annee_naissance, notes):
        self.nom = nom
        self.prenom = prenom
        self.annee_naissance = annee_naissance
        self.notes = notes

    def calculer_moyenne(self):
        return sum(self.notes) / len(self.notes)


# Fonction pour afficher la liste de la classe par ordre alphabétique du nom
def afficher_liste_par_ordre_alpha(etudiants):
    etudiants_tries = sorted(etudiants, key=lambda x: x.nom)
    for etudiant in etudiants_tries:
        print(f"{etudiant.nom} {etudiant.prenom}")


# Fonction pour afficher la moyenne de la classe
def afficher_moyenne_classe(etudiants):
    moyenne_classe = sum(etudiant.calculer_moyenne() for etudiant in etudiants) / len(etudiants)
    print(f"Moyenne de la classe : {moyenne_classe:.2f}")


# Fonction pour afficher la meilleure moyenne et les détails de l'étudiant
def afficher_meilleure_moyenne(etudiants):
    meilleur_etudiant = max(etudiants, key=lambda x: x.calculer_moyenne())
    print(
        f"Meilleure moyenne : {meilleur_etudiant.calculer_moyenne():.2f} - {meilleur_etudiant.nom} {meilleur_etudiant.prenom}")


# Fonction pour afficher la plus faible moyenne et les détails de l'étudiant
def afficher_plus_faible_moyenne(etudiants):
    plus_faible_etudiant = min(etudiants, key=lambda x: x.calculer_moyenne())
    print(
        f"Plus faible moyenne : {plus_faible_etudiant.calculer_moyenne():.2f} - {plus_faible_etudiant.nom} {plus_faible_etudiant.prenom}")


# Fonction pour afficher les étudiants par ordre de mérite
def afficher_etudiants_par_ordre_de_merite(etudiants):
    etudiants_tries = sorted(etudiants, key=lambda x: x.calculer_moyenne(), reverse=True)
    for etudiant in etudiants_tries:
        print(f"{etudiant.nom} {etudiant.prenom} - Moyenne : {etudiant.calculer_moyenne():.2f}")


# Fonction pour afficher le plus jeune et le plus âgé de la classe
def afficher_plus_jeune_et_plus_age(etudiants):
    plus_jeune = min(etudiants, key=lambda x: x.annee_naissance)
    plus_age = max(etudiants, key=lambda x: x.annee_naissance)
    print(f"Plus jeune : {plus_jeune.nom} {plus_jeune.prenom} - Année de naissance : {plus_jeune.annee_naissance}")
    print(f"Plus âgé : {plus_age.nom} {plus_age.prenom} - Année de naissance : {plus_age.annee_naissance}")


# Exemple d'utilisation
etudiants = [
    Etudiant("Doe", "John", 2000, [80, 85, 90]),
    Etudiant("Smith", "Alice", 1999, [75, 80, 85]),
    Etudiant("Johnson", "Bob", 2001, [90, 92, 88]),
]

afficher_liste_par_ordre_alpha(etudiants)
afficher_moyenne_classe(etudiants)
afficher_meilleure_moyenne(etudiants)
afficher_plus_faible_moyenne(etudiants)
afficher_etudiants_par_ordre_de_merite(etudiants)
afficher_plus_jeune_et_plus_age(etudiants)
