# Importation --------------------------------------------------------------------------------------
import os
import ctypes
from google import *
from tkinter import *
from tkinter import ttk
from google import genai
from dotenv import load_dotenv


# Definition ---------------------------------------------------------------------------------------
LARGEUR = 600
HAUTEUR = 400
LARGEURMIN = LARGEUR // 2
HAUTEURMIN = HAUTEUR // 2

class Window(Tk):
    def __init__(self):
        super().__init__()
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(99, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(99, weight=1)

# Loader les variables dans le fichier .env
load_dotenv(dotenv_path=os.path.join("Ressource", ".env"))
GEMINI_API = os.getenv("GOOGLE_KEY_API")

# Test des variables dans .env
Test = os.getenv("TEST_CONNECTION_VARIABLE")
if Test is None:
    print(f"[DEBUG]: Probleme avec le fichier .env")
else:
    print(f"[DEBUG]: La connection avec le .env est {Test}")

def send_message(query):
    API_KEY = GEMINI_API
    if query == "":
        print(f"[DEBUG]: Rien dans le champ de texte")
        return False
    if API_KEY is None:
        print(f"[DEBUG]: Vérifier la clé API dans le .env")
        return False
    print(f"[DEBUG]: Tout OK envoi du message")
    print(f"[DEBUG]: MOI: {query}")
    try:
        client = genai.Client(api_key=API_KEY)
        response = client.models.generate_content(model='gemini-3.5-flash-lite', contents=query)
        print(f"[DEBUG]: GEMINI: {response.text}")
        Main_Window.chat_box.delete(0, END)
        return response.text
    except Exception as error:
        print(f"[DEBUG]: Erreur lors de l'appel à l'API : {error}")
        return False

def show_main_app(app):
    app.geometry(f"{LARGEUR}x{HAUTEUR}")
    app.titre = Label(app, text = "ChatBot PyPrompt", font = ("Arial", 20))
    app.titre.grid(row=0, column=49)
    app.chat_box = Entry(app, width=30, font="Arial")
    app.chat_box.grid(row=99, column=98)
    app.Button_send = Button(app, text="▶️", command=lambda: send_message(app.chat_box.get()))
    app.Button_send.grid(row=99, column=99)
    menu_bar = Menu(app)
    menu_bar.add_command(label="Paramètres", command=lambda: show_parametre()) # Bouton Paramètres
    app.config(menu=menu_bar)

def show_parametre():
    Param_Window = Window()
    Param_Window.title("Paramètres")
    Param_Window.geometry(f"{LARGEURMIN}x{HAUTEURMIN}")
    Param_Window.iconbitmap("./Ressource/Images/Parametre.ico")

# Application --------------------------------------------------------------------------------------
Main_Window = Window()
show_main_app(Main_Window)
# Boucle principale
Main_Window.mainloop()