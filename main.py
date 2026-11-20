# Importation --------------------------------------------------------------------------------------
import os
import ctypes
from google import *
from tkinter import *
from tkinter import ttk
from google import genai
from dotenv import load_dotenv

# Loader le fichier .env ---------------------------------------------------------------------------
load_dotenv(dotenv_path=os.path.join("Ressource", ".env"))
TEST = os.getenv("TEST_CONNECTION_VARIABLE")
GEMINI_API = os.getenv("GOOGLE_KEY_API")

# Fonction -----------------------------------------------------------------------------------------
LARGEUR = 600
HAUTEUR = 400
LARGEURMIN = LARGEUR // 2
HAUTEURMIN = HAUTEUR // 2

class Window(Tk): # Classe pour avoir une grille quand une fenetre est cree avec.
    def __init__(self):
        super().__init__()
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

def main_window(app):
    app.geometry(f"{LARGEUR}x{HAUTEUR}")
    app.title("ChatBot PyPrompt")
    app.iconbitmap("./Ressource/Images/Icon.ico")
    app.titre = Label(app, text = "ChatBot PyPrompt", font = ("Arial", 20))
    app.titre.grid(row=10, column=0, columnspan=2, pady=10)

# Boucle principale de l'application
main = Window()
main_window(main)
main.mainloop()