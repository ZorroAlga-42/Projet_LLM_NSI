# Importation --------------------------------------------------------------------------------------
import os
import ctypes
import json
from google import *
from tkinter import *
from tkinter import ttk
from google import genai
from dotenv import load_dotenv

from Outils import right_api, set_background
from Agent import send_message, Agent_use

# Loader le fichier .env ---------------------------------------------------------------------------
load_dotenv(dotenv_path=os.path.join("Ressource", ".env"))
TEST = os.getenv("TEST_CONNECTION_VARIABLE")

Agents = ["Gemini", "OpenAI", "Anthropic"]
KEY_API_USE = os.getenv(Agent_use(Agents[0]))

# Fonction -----------------------------------------------------------------------------------------
LARGEUR = 600
HAUTEUR = 400
LARGEURMIN = LARGEUR // 2
HAUTEURMIN = HAUTEUR // 2
COLONES = 10
LIGNES = 10
Couleurs = ["Blanc", "Noir", "Rouge", "Vert", "Bleu", "Add"]

class Window(Tk): # Classe pour avoir une grille quand une fenetre est cree avec.
    def __init__(self ):
        super().__init__()
        for c in range(COLONES):
            self.columnconfigure(c, weight=1)
        for l in range(LIGNES):
            self.rowconfigure(l, weight=1)

def afficher_grille(app):
    """Affiche un quadrillage visible pour débuguer la grille tkinter."""
    for r in range(LIGNES):
        app.rowconfigure(r, weight=1)
        for c in range(COLONES):
            app.columnconfigure(c, weight=1)
            cellule = Frame(app, bg="white", highlightbackground="red", highlightthickness=1)
            cellule.grid(row=r, column=c, sticky="nsew")
            Label(cellule, text=f"{r},{c}", fg="red", bg="white").pack()

def main_window(app):
    # objet de la fenetre
    #afficher_grille(app) # Pour le debug
    app.geometry(f"{LARGEUR}x{HAUTEUR}")
    app.title("ChatBot PyPrompt")
    app.iconbitmap("./Ressource/Images/Icon.ico")
    app.titre = Label(app, text = "ChatBot PyPrompt", font = ("Arial", 20))
    app.chat_box = Text(app, width=30, height=4, font=("Arial", 12))
    app.response_box = Text(app, width=40, height=15, font=("Arial", 12))
    app.send_button = Button(app, text = ">", command=lambda: send_message(app.chat_box.get("1.0", "end-1c"),
                                                                           app, KEY_API_USE))
    app.menu_bar = Menu(app)
    app.param_menu = Menu(app.menu_bar)
    app.config(menu=app.menu_bar)
    app.menu_bar.add_cascade(label="Options", menu=app.param_menu)
    app.param_menu.add_command(label="Paramètres", command=lambda: parametres(app))

    # Placement des elements sur la grille
    app.titre.grid(row=0, column=2, columnspan=6)
    app.chat_box.grid(row=7, column=6, columnspan=3, rowspan=2)
    app.response_box.grid(row=1, column=6, columnspan=4, rowspan=6)
    app.send_button.grid(row=7, column=9, columnspan=2, rowspan=2)

def parametres(app):
    root = app
    app = Toplevel(root)
    #afficher_grille(app) # Pour le debug
    app.title("Paramètres")
    app.iconbitmap("./Ressource/Images/Parametre.ico")
    app.geometry(f"{LARGEURMIN}x{HAUTEURMIN}")
    app.selec_agent = ttk.Combobox(app, values=Agents, state="readonly", font=("Arial", 12))
    app.api_box = Entry(app, width=25, font=("Arial", 12))
    app.save_api = Button(app, text="Save", command=lambda: right_api(app.api_box.get(),
                                                                      Agent_use(app.selec_agent.get())))
    app.color_app = ttk.Combobox(app, values=Couleurs, state="readonly", font=("Arial", 12))
    app.color_app.current(0)
    app.color_save = Button(
        app,
        text="Save",
        command=lambda: set_background(
            app.color_app.get(),
            [root] + [
                window for window in root.winfo_children()
                if isinstance(window, Toplevel)],),)

    # Placement des elements sur la grille
    app.api_box.grid(row=1, column=1, columnspan=7, rowspan=2)
    app.save_api.grid(row=1, column=8, columnspan=2, rowspan=2)
    app.selec_agent.grid(row=3, column=1, columnspan=7)
    app.color_app.grid(row=3, column=8, columnspan=2, rowspan=2)
    app.color_save.grid(row=3, column=10, columnspan=2, rowspan=2)

# Boucle principale de l'application
main = Window()
main_window(main)
main.mainloop()