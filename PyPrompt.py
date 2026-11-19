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
LARGEURMIN = 300
HAUTEURMIN = 200

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
        chat_box.delete(0, END)
        return response.text
    except Exception as error:
        print(f"[DEBUG]: Erreur lors de l'appel à l'API : {error}")
        return False

def show_parametre():
    window_param = Tk()
    window_param.title("Paramètres")
    window_param.geometry(f"{LARGEURMIN}x{HAUTEURMIN}")


# Application --------------------------------------------------------------------------------------

# definition de la fenetre principale de l'app
app_principale = Tk() # Def que app_principale est un fenetre
app_principale.title("PyPrompt")
app_principale.iconbitmap("./Ressource/Images/Icon.ico")
app_principale.geometry(f"{LARGEUR}x{HAUTEUR}") # Dimension de cette fenetre

# Titre de l'applicaion
titre = Label(app_principale, text = "ChatBot PyPrompt", font = ("Arial", 20))
titre.pack(pady=20)

chat_box = Entry(app_principale, width=30, font="Arial")
chat_box.pack()
Button_send = Button(app_principale, text="▶️", command=lambda: send_message(chat_box.get()))
Button.pack(Button_send)
menu_bar = Menu(app_principale)
menu_bar.add_command(label="Paramètres", command=lambda: show_parametre()) # Bouton Paramètres
app_principale.config(menu=menu_bar)

# Boucle principale
app_principale.mainloop()