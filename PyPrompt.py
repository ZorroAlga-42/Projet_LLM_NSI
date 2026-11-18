# Importation --------------------------------------------------------------------------------------
import os
import ctypes
from google import *
from tkinter import *
from tkinter import ttk
from dotenv import load_dotenv

# Loader les variables dans le fichier .env
load_dotenv(dotenv_path=os.path.join("Ressource", ".env"))
# Test des variables dans .env
Test = os.getenv("TEST_CONNECTION_VARIABLE")
if Test is None:
    print(f"[DEBUG]: Probleme avec le fichier .env")
else:
    print(f"[DEBUG]: La connection avec le .env est {Test}")

# Definition ---------------------------------------------------------------------------------------
LARGEUR = 600
HAUTEUR = 400
GEMINI_API = os.getenv("GOOGLE_KEY_API")

def send_message(query):
    API_KEY = GEMINI_API
    if query is None:
        print(f"[DEBUG]: Rien dans le champ de texte")
        return False
    if API_KEY is None:
        print(f"[DEBUG]: Vérifier la clé API dans le .env")
        return False
    print(f"[DEBUG]: Tout OK envoie du message...")
    try:
        client = genai.Client(api_key=API_KEY)
        response = client.models.generate_content(model='gemini-2.5-flash', contents=query)
        print(f"[REPONSE GEMINI]: {response.text}")
        return response.text
    except Exception as e:
        print(f"[DEBUG]: Erreur lors de l'appel à l'API : {e}")
        return False


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
B_send = Button(app_principale, text="▶️", command=lambda: send_message(chat_box.get))
Button.pack(B_send)

# Boucle principale
app_principale.mainloop()