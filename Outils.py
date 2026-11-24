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


# Couleur de fond --------------------------------------------------------------------------------------
def set_background_color(color):
    try:
        ctypes.windll.user32.SetSysColors(1, ctypes.pointer(ctypes.c_int(15)), ctypes.pointer(ctypes.c_int(int(color[1:], 16))))
    except Exception as e:
        print(f"[DEBUG]: Erreur lors du changement de couleur de fond : {e}")

def set_background(fenetre, couleur):
    fenetre.configure(bg=couleur)
    