# Importation --------------------------------------------------------------------------------------
import os
import ctypes
from google import *
from tkinter import *
from tkinter import ttk
from google import genai
from dotenv import load_dotenv

from Outils import right_api
from Agent import send_message

# Loader le fichier .env ---------------------------------------------------------------------------
load_dotenv(dotenv_path=os.path.join("Ressource", ".env"))
TEST = os.getenv("TEST_CONNECTION_VARIABLE")
GEMINI_API = os.getenv("GOOGLE_KEY_API")

# Fonction -----------------------------------------------------------------------------------------
LARGEUR = 600
HAUTEUR = 400
LARGEURMIN = LARGEUR // 2
HAUTEURMIN = HAUTEUR // 2
COLONES = 10
LIGNES = 10

class Window(Tk): # Classe pour avoir une grille quand une fenetre est cree avec.
    def __init__(self ):
        super().__init__()
        for c in range(COLONES):
            self.columnconfigure(c, weight=1)
        for l in range(LIGNES):
            self.rowconfigure(l, weight=1)
def afficher_grille(app):
    """Affiche un quadrillage visible pour déboguer la grille tkinter."""
    for r in range(LIGNES):
        app.rowconfigure(r, weight=1)
        for c in range(COLONES):
            app.columnconfigure(c, weight=1)
            cellule = Frame(
                app,
                bg="white",
                highlightbackground="red",  # couleur de la bordure
                highlightthickness=1        # épaisseur de la bordure
            )
            cellule.grid(row=r, column=c, sticky="nsew")
            # Petit label pour voir les coordonnées de chaque cellule
            Label(cellule, text=f"{r},{c}", fg="red", bg="white").pack()

def main_window(app):
    # objet de la fenetre
    afficher_grille(app) # Pour le debug
    app.geometry(f"{LARGEUR}x{HAUTEUR}")
    app.title("ChatBot PyPrompt")
    app.iconbitmap("./Ressource/Images/Icon.ico")
    app.titre = Label(app, text = "ChatBot PyPrompt", font = ("Arial", 20))
    app.chat_box = Text(app, width=30, height=4)
    app.response_box = Text(app, width=40, height=15)
    app.send_button = Button(app, text = ">", command=lambda: send_message(app.chat_box.get("1.0", "end-1c"), app))
    app.menu_bar = Menu(app)
    app.param_menu = Menu(app.menu_bar)
    app.param_menu.add_command(label="Paramètres", command=lambda: parametres(app))

    # Placement des elements sur la grille
    app.titre.grid(row=0, column=2, columnspan=6)
    app.chat_box.grid(row=7, column=6, columnspan=3, rowspan=2)
    app.response_box.grid(row=1, column=6, columnspan=4, rowspan=6)
    app.send_button.grid(row=7, column=9, columnspan=2, rowspan=2)

def parametres(app):
    param_window = Toplevel(app)
    param_window.title("Paramètres")
    param_window.geometry(f"{LARGEURMIN}x{HAUTEURMIN}")

# Boucle principale de l'application
main = Window()
main_window(main)
main.mainloop()