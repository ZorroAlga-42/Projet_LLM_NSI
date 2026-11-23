# Importation --------------------------------------------------------------------------------------
from Main import GEMINI_API
from Main import Main_Window

# Fonction -----------------------------------------------------------------------------------------
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
        Main_Window.chat_box.delete(0, END)
        Main_Window.responce_box.delete(0, END)
        Main_Window.responce_box.insert(0, response.text)
        return response.text
    except Exception as error:
        print(f"[DEBUG]: Erreur lors de l'appel à l'API : {error}")
        return False