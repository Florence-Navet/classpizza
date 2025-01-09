class Pizza():
    def __init__(self, base, prix, taille, style, piment, ingredients):
        self.base = base
        self.prix = prix
        self.taille = taille
        self.style = style
        self.piment = piment
        self.ingredients = ingredients

    """
        ajouter_ingredients:
        input=string (ex: si c'était un dictionnaire en entrée, on mettrait dict(int, string, float))
        output="return" ici rien
    """
    def ajouter_ingredients(self, nouvel_ingredient):
        if nouvel_ingredient == "ananas":
            raise ValueError("Les ananas ne vont pas sur la pizza !")
        self.ingredients.append(nouvel_ingredient)
        self.prix = self.prix + 1

    def servir(self, table):
        print("J'amène la pizza à la table", table)

    def livre(self, adresse):
        print("Je livre la pizza à l'adresse :", adresse)

"""___________________Paramètres d'entrée______________________"""

base = input("Quelle base voulez-vous ? (tomate/blanche) ? ").lower()
taille = input("Quelle taille de pizza voulez-vous ? (moyenne/grande) ? ").lower()
style = input("Quel style voulez-vous ? (classique/calzone) ? ").lower()
piment = input("Voulez-vous du piment ? (oui/non) ").lower()
ingredients = input("Quels ingrédients voulez-vous ? ").lower()
choix = input("Voulez-vous une livraison ou être servi à table (livraison/table) ? ").lower()

# Déterminer la taille de la pizza (30 par défaut pour 'moyenne')
if taille == "grande":
    taille = 34
else:
    taille = 30

ingredients = ingredients.split(" , ")

if piment == "oui":
    ingredients.append("piment")

prix = 6 + len(ingredients)

pizza = Pizza(
    base=base,
    prix=prix,
    taille=taille,
    style=style,
    piment=piment,
    ingredients=ingredients,
)

"""______________Début de code__________________"""

print("Ingrédients :", pizza.ingredients)
print("Prix initial :", pizza.prix, "€")


#livraison ou service à table
if choix == "livraison":
    pizza.prix += 5
    adresse = input("Veuillez entrer votre adresse de livraison : ")
    pizza.livre(adresse)
    print(f"Prix final avec livraison : {pizza.prix} €")
elif choix == "table":
    table = input("Entrez le numéro de votre table : ")
    pizza.servir(table)
    print(f"Prix final : {pizza.prix} €")
else:
    print("Choix non valide. À récupérer en caisse.")
    print(f"Le prix final est de : {pizza.prix} €")
