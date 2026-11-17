# Importation --------------------------------------------------------------------------------------
import os
import ctypes
from tkinter import *
from tkinter import ttk
from google import *
from dotenv import load_dotenv

# Loader les variable dans le fichier .env
load_dotenv(dotenv_path=os.path.join("Ressource", ".env"))
# Teste des variable dans .env
Teste = os.getenv("TESTE_CONNECTION_VARIABLE")
if Teste == None:
    print(f"[DEBUG]: Problemme avec le fichier .env")
else:
    print(f"[DEBUG]: La connection avec le .env est {Teste}")

# Definition ---------------------------------------------------------------------------------------
LARGEUR = 600
HAUTEUR = 400

Gemini_API = os.getenv("GOOGLE_KEY_API")
def send_mesage(query, API_KEY):
    API_KEY = Gemini_API
    query = chat_box.get("1.0", END).strip()
    if query == None or API_KEY == "":
        print(f"[DEBUG]: Rien dans le champs de texte // Mauvaise clé api dans .env")
        return False
    print(f"[DEBUG]: Tout OK envoie du message...")
    


# Application --------------------------------------------------------------------------------------

# deffinition de la fenetre principale de l'app
app_principale = Tk() # Def que app_principale est un fenetre
app_principale.title("PyPrompt")
app_principale.iconbitmap("./Ressource/Images/Icon.ico")
app_principale.geometry(f"{LARGEUR}x{HAUTEUR}") # Dimantion de cette fenetre

# Titre de l'applicaion
titre = Label(app_principale, text = "ChatBot PyPrompt", font = ("Arial", 20))
titre.pack(pady= 20)

chat_box = Entry(app_principale, width=30, font="Arial")
chat_box.pack()

# Boucle principale
app_principale.mainloop()