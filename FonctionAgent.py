# Importation --------------------------------------------------------------------------------------
import os
import ctypes
from google import *
from tkinter import *
from tkinter import ttk
from dotenv import load_dotenv

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
    print(f"[DEBUG]: Tout OK envoi du message: {query}")
    try:
        client = ganei.Client(api_key=API_KEY)
        response = client.models.generate_content(model='gemini-2.5-flash', contents=query)
        print(f"[REPONSE GEMINI]: {response.text}")
        return response.text
    except Exception as error:
        print(f"[DEBUG]: Erreur lors de l'appel à l'API : {error}")
        return False