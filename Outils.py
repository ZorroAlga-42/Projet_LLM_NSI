# Importation --------------------------------------------------------------------------------------
import os
import ctypes
import json
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


# Couleur de fond --------------------------------------------------------------------------------------
def set_background(couleur, windows):
    couleurs = {
        "Blanc": "#FFFFFF",
        "Noir": "#000000",
        "Rouge": "#FF0000",
        "Vert": "#00FF00",
        "Bleu": "#0000FF",
        "Add": "#1696C0",
    }
    couleur_fond = couleurs.get(couleur, couleur)

    for window in windows:
        window.configure(bg=couleur_fond)

    os.makedirs("./Paramètre", exist_ok=True)
    with open("./Paramètre/parametres.json", "w", encoding="utf-8") as f:
        json.dump({"couleur_fond": couleur_fond}, f)
