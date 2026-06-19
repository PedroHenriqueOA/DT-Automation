import os
from dotenv import load_dotenv, dotenv_values
from key_opener import openKey
from pandas_cpf_copying import copyCpf

load_dotenv()

# ---------------INFORMAÇÕES DO PLANEJAMENTO-----------------------------
site = "HUB-LES-03"
date_plan = "19/06/2026"
hour_plan = "0930"
workers_quantity = "6"
# ---------------------------------------------------------------------
dt_user = os.getenv("DT_USERNAME")
dt_pass = os.getenv("DT_PASSWORD")


# copyCpf()

openKey(site, date_plan, hour_plan, workers_quantity, dt_user, dt_pass)
