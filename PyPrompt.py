# Importation --------------------------------------------------------------------------------------
from tkinter import *


LARGEUR = 600
HAUTEUR = 400
# deffinition de la fenetre principale de l'app
app_principale = Tk()
app_principale.title("PyPrompt")
app_principale.geometry(f"{LARGEUR}x{HAUTEUR}")

# Titre de l'applicaion
titre = Label(app_principale, text = "ChatBot PyPrompt", font = ("Arial", 20))
titre.pack(pady= 20)

# Teste d'implemantation d'un bouton
Bouton_Teste = Button(app_principale, text = "Teste")
Bouton_Teste.pack()

# Boucle principale
app_principale.mainloop()