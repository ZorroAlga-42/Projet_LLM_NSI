# Importation --------------------------------------------------------------------------------------
import os
import ctypes
from google import *
from tkinter import *
from tkinter import ttk
from google import genai
from dotenv import load_dotenv

# Fonction -----------------------------------------------------------------------------------------
def right_api(cle, who):
    chemin = "./Ressource/.env"
    try:
        with open(chemin, "r", encoding="utf-8") as f:
            lignes = f.readlines()
    except FileNotFoundError:
        lignes = []
    trouve = False
    for i, ligne in enumerate(lignes):
        if ligne.startswith(f"{who} = "):
            lignes[i] = f"{who} = {cle}\n"
            trouve = True
            break
    if not trouve:
        lignes.append(f"{who} = {cle}\n")
    with open(chemin, "w", encoding="utf-8") as f:
        f.writelines(lignes)
