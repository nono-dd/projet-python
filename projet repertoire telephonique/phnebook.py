# phonebook
# Auteur : Nono
# Date : 15/01/2024

# importation des modules
import time
# from pathlib import Path
from datetime import datetime


# Initialisation du répertoire téléphonique
phonebook_stock = {}
temps_actuelle = datetime.now()


def ajouter_un_numero():
    # Fonction pour ajouter un numéro au répertoire
    first_name = input("Nom : ").capitalize()
    last_name = input("Prénom : ").capitalize()

    # Vérification du nom et prénom
    while not first_name.isalpha():
        print("Désolé nom invalide !!!")
        first_name = input("Nom : ").capitalize()
    while not last_name.isalpha():
        print("Désolé prénom invalide !!!")
        last_name = input("Prénom : ").capitalize()

    number = input('Numéro : ')

    # Vérification du numéro
    while not number.isdigit():
        print("Désolé numéro invalide !!!")
        number = input('Numéro : ')

    # Stockage des informations dans le répertoire téléphonique
    all_name = first_name + ' ' + last_name
    phonebook_stock[all_name] = number
    time.sleep(1)
    print(f"{all_name} a été ajouté au répertoire avec le numéro {number}")
    time.sleep(1.4)


# ...
def recherche_contact():
    check = input('''Connaissez-vous le nom complet de la personne a rechercher ??
                1. OUI
                2. NON 

                    >>> :  ''')
    stop = True
    while stop:
        if check.isdigit() or 1 <= int(check) <= 2:
            stop = False
        else:
            print(f"{check} n'est pas une valeur valable !!! ")

    if check == "1":
        name_to_delete = input("Nom complet de la personne à rechercher : ").strip().title()
        for name, number in phonebook_stock.items():
            if name_to_delete is name:
                print(f"Nom    : {name_to_delete}\n"
                      f"------------------"
                      f"Numéro : {number}")
            else:
                print(f"{name_to_delete} n'est pas dans le répertoire.")
                time.sleep(2)

    elif check == "2":
        verif = input('''
                        1. Faire une recherche à partir du nom de famille 
                        2. Faire une recherche à partir du numéro de téléphone
                            >>> : ''')
        pause = True
        while pause:
            if verif.isdigit() or 1 <= int(verif) <= 2:
                pause = False
            else:
                print(f"{verif} n'est pas une valeur valable !!! ")
                user_input = input('Continuer ou sauter [ Y/N ] : ').lower()
                if user_input.lower() == "y":
                    print('''

                        ''')
                elif user_input.lower() == "n":
                    pause = False

        if verif == "1":
            recherche_fam = input('entrer le nom de famille : ')
            for name, number in phonebook_stock.items():
                if recherche_fam in name:
                    print(f"  Nom    : {name}\n"
                          f"-------------------"
                          f"  Numéro : {number}")
                elif recherche_fam[0].lower() in name[0].lower():
                    print(f"Pas de noms correspondant a  {recherche_fam.upper()}")
                    time.sleep(2)
                    print(f"Voici tous les noms commencent par {recherche_fam[0].upper()}")
                    time.sleep(2)
                    print(f"  Nom    : {name}\n"
                          f"-------------------"
                          f"  Numéro : {number}")
                else:
                    print(f"Aucun nom ne commence par {recherche_fam[0].upper()}")

        elif verif == "2":
            recherche_num = input("Entrer le numéro de téléphone à rechercher : ")
            for name, number in phonebook_stock.items():
                if recherche_num == number:
                    print(f"  Nom    : {name}\n"
                          f"-------------------"
                          f"  Numéro : {number}")


def delete_number():
    check = input('''Connaissez-vous le nom complet de la personne à supprimer ??
            1. OUI
            2. NON 

                >>> :  ''')
    stop = True
    while stop:
        if check.isdigit() or 1 <= int(check) <= 2:
            stop = False
        else:
            print(f"{check} n'est pas une valeur valable !!! ")

    if check == "1":
        name_to_delete = input("Nom complet de la personne à supprimer : ").strip().title()
        if name_to_delete in phonebook_stock:
            del phonebook_stock[name_to_delete]
            print(f"{name_to_delete} a été supprimé du répertoire.")
        else:
            print(f"{name_to_delete} n'est pas dans le répertoire.")
            time.sleep(2)

    elif check == "2":
        verif = input('''
                    1. Faire une recherche à partir du nom de famille 
                    2. Faire une recherche à partir du numéro de téléphone
                        >>> : ''')
        pause = True
        while pause:
            if verif.isdigit() or 1 <= int(verif) <= 2:
                pause = False
            else:
                print(f"{verif} n'est pas une valeur valable !!! ")
                user_input = input('Continuer ou sauter [ Y/N ] : ').lower()
                if user_input.lower() == "y":
                    print('''
                    
                    ''')
                elif user_input.lower() == "n":
                    pause = False

        if verif == "1":
            recherche_fam = input('entrer le nom de famille : ')
            for name, number in phonebook_stock.items():
                if recherche_fam in name:
                    print(f"  Nom    : {name}\n"
                          f"-------------------"
                          f"  Numéro : {number}")
                elif recherche_fam[0].lower() in name[0].lower():
                    print(f"Pas de noms correspondant a  {recherche_fam.upper()}")
                    time.sleep(2)
                    print(f"Voici tous les noms commencent par {recherche_fam[0].upper()}")
                    time.sleep(2)
                    print(f"  Nom    : {name}\n"
                          f"-------------------"
                          f"  Numéro : {number}")
                else:
                    print(f"Aucun nom ne commence par {recherche_fam[0].upper()}")

        elif verif == "2":
            recherche_num = input("Entrer le numéro de téléphone à rechercher : ")
            for name, number in phonebook_stock.items():
                if recherche_num == number:
                    print(f"  Nom    : {name}\n"
                          f"-------------------"
                          f"  Numéro : {number}")


def save_to_file():
    verif = input('''Avez-vous un fichier pour l'enregistrement ??
    1. Oui
    2. Non
    3. Quit''')
    if verif == '1':
        file_name = input('Entrer le nom du fichier : ')
        with open(file_name, "w") as fic:
            for name, number in phonebook_stock.items():
                fic.write(f"{name}: {number}\n")
            fic.write(f"\n\t Le répertoire téléphonique a été enregistrer a {temps_actuelle}")
            fic.close()
        print(f"Le répertoire téléphonique a été écrit dans le fichier {file_name}.")
        time.sleep(1)

    elif verif == '2':
        file_name = input('Entrer le nom du fichier a créer : ')
        with open(file_name, 'w') as fic:
            for name, number in phonebook_stock.items():
                fic.write(f"{name}: {number}\n")
            fic.write(f"\n\t Le répertoire téléphonique a été enregistrer a {temps_actuelle}")
        fic.close()
    elif verif == '3':
        print('')


def phonebook():
    # Fonction principale pour gérer le répertoire téléphonique
    # Boucle principale du menu
    print('Bienvenue dans le répertoire de votre téléphone')
    stop = True
    while stop:
        print('''
            1. Ajouter un numéro
            2. Supprimer un numéro
            3. Rechercher un numéro
            4. Afficher la liste des contacts
            5. Quitter\n''')
        choice = input("  >>> : ")

        # Vérification de la validité du choix
        while not choice.isdigit() or not 1 <= int(choice) <= 5:
            print("Choix invalide !!!")
            choice = input("  >>> : ")

        choice_index = int(choice)
        if choice_index == 1:
            ajouter_un_numero()
        elif choice_index == 2:
            delete_number()
        elif choice_index == 3:
            recherche_contact()
        elif choice_index == 5:
            save_to_file()
            print(". . . .. .. BYE (- o -)")
            stop = False
        elif choice_index == 4:
            verif = input('''Voulez-vous afficher :
           1. Tous les numéros
           2. Les noms et numéros''')
            i = 0
            if verif == '1':
                for number in phonebook_stock.values():
                    print(f"Numéro de téléphone{i + 1} : {number}")
                    i += 1
                print("Total des numéros est de ", i)

            elif verif == '2':
                print("Liste des contacts:")
                for name, number in phonebook_stock.items():
                    print(f"{name}: {number}")


# Appel de la fonction principale
phonebook()
