# Importation --------------------------------------------------------------------------------------
import os
import ctypes
from google import *
from tkinter import *
from tkinter import ttk
from FonctionAgent import send_message

# Definition ---------------------------------------------------------------------------------------
LARGEUR = 600
HAUTEUR = 400

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
B_send = Button(app_principale, text="▶️", command=lambda: send_message(chat_box.get()))
Button.pack(B_send)

# Boucle principale
app_principale.mainloop()