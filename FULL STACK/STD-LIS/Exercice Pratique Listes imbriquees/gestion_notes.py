# Liste des étudiants
etudiants = ["Alice", "Jean", "Marie"]

# Notes des étudiants
notes = [
    [15, 12, 18],
    [10, 14, 16],
    [17, 13, 19]
]

# Noms des matières
matieres = ["Mathématiques", "Informatique", "Français"]

# Affichage des résultats
for i in range(len(etudiants)):

    print("\nÉtudiant :", etudiants[i])

    for j in range(len(matieres)):
        print(matieres[j], ":", notes[i][j])

    # Calcul de la moyenne
    moyenne = sum(notes[i]) / len(notes[i])

    print("Moyenne :", round(moyenne, 2))

    # Détermination du résultat
    if moyenne >= 10:
        print("Résultat : Admis")
    else:
        print("Résultat : Ajourné")