import os
from dotenv import load_dotenv, dotenv_values
from key_opener import openKey
from pandas_cpf_copying import copyCpf
import keyboard

load_dotenv()

# ---------------INFORMAÇÕES DO PLANEJAMENTO-----------------------------
site = "HUB-LGO-03"
date_plan = "22/06/2026"
hour_plan = "0700"
workers_quantity = "4"
# ---------------------------------------------------------------------
dt_user = os.getenv("DT_USERNAME")
dt_pass = os.getenv("DT_PASSWORD")
download_directory = os.getenv("DOWNLOAD_FOLDER")
escalamento_path = os.getenv("ESCALAMENTO_PATH")

# -----------------Chama função para copiar cpf ao presssionar SHIFT + Q-----------------------
keyboard.add_hotkey("shift+q", lambda: copyCpf(download_directory, escalamento_path))

# copyCpf(download_directory, escalamento_path)

# -----------------Chama função para abrir chave ao pressionar SHIFT + O + K-----------------------
keyboard.add_hotkey(
    "shift+o+k",
    lambda: openKey(site, date_plan, hour_plan, workers_quantity, dt_user, dt_pass),
)
keyboard.wait()
