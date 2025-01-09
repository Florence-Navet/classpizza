nb_vies = 7
mot_mystere = "python"
mot_public = '_' * len(mot_mystere)

while nb_vies > 0 and mot_public != mot_mystere:
    lettre = input('Entrez votre lettre : ').lower()  # Pour accepter majuscules et minuscules

    if lettre in mot_mystere:
        # Mettre à jour `mot_public` avec la lettre trouvée
        mot_public = ''.join(
            [lettre if mot_mystere[i] == lettre else mot_public[i] for i in range(len(mot_mystere))]
        )
        print(f"Bonne lettre ! Le mot est maintenant : {mot_public}")
    else:
        nb_vies -= 1
        print(f"Mauvaise lettre. Il vous reste {nb_vies} vies.")

# Résultat final
if mot_public == mot_mystere:
    print(f"Bravo ! Vous avez trouvé le mot mystère : {mot_public}")
else:
    print(f"Dommage, vous avez perdu ! Le mot mystère était : {mot_mystere}")
