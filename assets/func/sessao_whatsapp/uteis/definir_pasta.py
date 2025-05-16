import os

def definir_pasta(client):
    PROFILE_DIR = os.path.expanduser(f"~/.whatsapp_automation_profile_{client}")  # Altere conforme necessario
    return PROFILE_DIR