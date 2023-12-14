def ajouter_numero(table_association):
    nom = input('entrer votre nom : ').upper()
    prenom = input('entrer votre prenom : ').capitalize()
    numero = int(input('entrer votre numero de telephone : '))
    nom = nom + ' ' + prenom
    numero = str(numero)
    table_association.update({nom: numero})
    

def afficher_repertoire(t):
    for name in t:
        print(f"{name} : {t[name]}")


def repertoire_telephonique():
    print("Salut bienvenue dans le repertoire telephonique")
    print()
    table_association = {'Arnaud Hien': '74-11-66-19'}
    print(table_association)
    verif = True
    while verif:
        choix_users = int(
            input("1-Ajouter un numero\n2-supprimer un numero\n3-Rechecher un numero\n4-Afficher les numero "
                  "telephonique\n5-Arrenter le programme\v\n\t"))
        if choix_users == 1:
            ajouter_numero(table_association)
        elif choix_users == 4:
            afficher_repertoire(table_association)
        elif choix_users == 2:
            if table_association is None:
                print("Désolé le répertoire téléphonique est vide ")
            else:
                name = input('Entrer le nom a retirer du repertoire: \t').upper()
                try:
                    table_association.pop(name)
                except KeyError:
                    print(f"Le {name} saisie n'est pas present dans le repertoire !!")
        elif choix_users == 3:
            name = input('Entrer le nom a rechercher : \t').upper()
            print(table_association.get(name, f'{name} n\'est pas present dans le repertoire !!'))
        elif choix_users == 5:
            print("Fin du programme .. . .....")
            verif = False


repertoire_telephonique()
"""
trie()
li = [1.2, 12, 2, 7, 8, 8, 68]
values = ['a', 'b', 'c', 'd']
print(values)
values.extend(['z', 'e', 'f'])
print(values)
values.extend("bono")
print(values)
values.append("bonjour")
print(values)
values.reverse()
print(values)
values.sort()
print(values)
values = [['a', 'b', 'c'], ['d', 'e', 'f']]
other_values = values.copy()
print(other_values)
values.append('g')
print(other_values)
values.append(['h', 'i', 'j'])
print(values)
print(other_values)"""
"""phonebook = {'Alice': '0633432380', 'Bob': '0663621029', 'Alex': '0714381809'}
print(phonebook['Bob'])
del phonebook['Alice']
print(phonebook)
print(phonebook.get('nono', 'absent'))
phonebook.pop('Bob')
print(phonebook)
phonebook.update({'arnaud': '74116619', 'kiki': '646304633'})
print(phonebook)
print(phonebook.pop('violet', 'pas presente'))
phonebook.setdefault('arnaud', '55555555')
print(phonebook)
mybook = phonebook
print(mybook)"""
