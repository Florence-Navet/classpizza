moyenne_eleve = float (input("Veuillez entrez votre moyenne :"))

if moyenne_eleve < 21:
        print(f"{moyenne_eleve} impossible")

        if 12 <=  moyenne_eleve < 14:
                print(f"Votre {moyenne_eleve} est assez bien")
        elif  14 < moyenne_eleve  <=16:
                print(f"Votre {moyenne_eleve} est bien")
        elif 16 < moyenne_eleve <=18:
                print(f"Votre {moyenne_eleve} est très bien")
        elif moyenne_eleve > 18:
                print(f"Votre {moyenne_eleve} reçoit les félicitations du jury")
        else:
                print(f"Vous êtes recalés !!")
else:
        print("Vous n'aurez pas de moyenne")

