# Importation --------------------------------------------------------------------------------------
import os
from tkinter import *
from dotenv import load_dotenv

# Loader les variable dans le fichier .env
load_dotenv(dotenv_path=os.path.join("Resource", ".env"))
# Teste des variable dasn .env
Teste = os.getenv("TESTE_CONNECTION_VARIABLE")
if Teste == None:
    print(f"Problemme avec le fichier .env")
else:
    print(f"La connection avec le .env est {Teste}")

# Application --------------------------------------------------------------------------------------
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