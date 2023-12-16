def union_triee(liste1, liste2):
    resultat = []
    i, j = 0, 0

    # Parcourir les deux listes en parallèle
    while i < len(liste1) and j < len(liste2):
        if liste1[i] < liste2[j]:
            resultat.append(liste1[i])
            i += 1
        elif liste1[i] > liste2[j]:
            resultat.append(liste2[j])
            j += 1
        else:
            # Si les éléments sont égaux, ajouter un seul et avancer dans les deux listes
            resultat.append(liste1[i])
            i += 1
            j += 1

    # Ajouter les éléments restants de la première liste
    while i < len(liste1):
        resultat.append(liste1[i])
        i += 1

    # Ajouter les éléments restants de la deuxième liste
    while j < len(liste2):
        resultat.append(liste2[j])
        j += 1

    return resultat

# Exemple d'utilisation
liste1 = [3, 6, 9]
liste2 = [1, 6, 8, 12, 15]

resultat_union = union_triee(liste1, liste2)
print(resultat_union)
