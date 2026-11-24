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
GEMINI_API = os.getenv("GOOGLE_KEY_API")

# Fonction -----------------------------------------------------------------------------------------
def send_message(query, app, Api_Key):
    if query == "":
        print(f"[DEBUG]: Rien dans le champ de texte")
        return False
    if Api_Key is None:
        print(f"[DEBUG]: Vérifier la clé API dans le .env")
        return False
    print(f"[DEBUG]: Tout OK envoi du message")
    print(f"[DEBUG]: MOI: {query}")
    try:
        client = genai.Client(api_key=Api_Key)
        response = client.models.generate_content(model='gemini-3.5-flash-lite', contents=query)
        print(f"[DEBUG]: GEMINI: {response.text}")
        app.chat_box.delete("1.0", END)
        app.response_box.delete("1.0", END)
        app.response_box.insert("1.0", response.text)
        return response.text
    except Exception as error:
        print(f"[DEBUG]: Erreur lors de l'appel à l'API : {error}")
        return False
    
def Agent_use(Agent: str):
    if Agent == "Gemini":
        return "GOOGLE_KEY_API"
    if Agent == "OpenIA":
        return "OPENIA_KEY_API"
    if Agent == "Antropic":
        return "ANTROPIC_API_KEY"

