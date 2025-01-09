class Voiture:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee

    def klaxonner(self):
        print("Tut tut !")

cybertruck = Voiture(marque="Tesla", modele="Cybertruck", annee=2023)
corolla = Voiture(marque="Toyota", modele="Corolla", annee=2022)

# print(cybertruck.marque)
# cybertruck.klaxonner()
# print(cybertruck.annee)
# cybertruck.annee = 2024
# print(cybertruck.annee)

# toutes les attributions avec l'instance de cybertruck
# print(dir(cybertruck))

Voiture.klaxonner(cybertruck)
