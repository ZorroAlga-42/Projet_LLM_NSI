# Importation --------------------------------------------------------------------------------------
import os
import ctypes
from google import *
from tkinter import *
from tkinter import ttk
from google import genai
from dotenv import load_dotenv

# Fonction -----------------------------------------------------------------------------------------
def right_api(cle):
    with open(".env", "w", encoding="utf-8") as fichier:
        fichier.write(f"API_KEY={cle}\n")
        print(f"[DEBUG] La clé {cle} a été écrite dans le fichier .env")
