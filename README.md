# Projeto pessoal de automação DT

## Como rodar

### VENV

Ao clonar o repositorio, você vai querer criar um VENV.

```
    python -m venv .venv
```

Ativar ele

```
    .venv\Scripts\Activate.ps1
```

E então instalar os requirements

```
    pip install -r requirements.txt
```

### .ENV

Vai ser necessario criar um arquivo .ENV para rodar.

Siga esse modelo:

DT_USERNAME = ""
DT_PASSWORD = ""
DOWNLOAD_FOLDER = "C:\\Users\\~\\Downloads\\\*"
ESCALAMENTO_PATH = "C:\Users\~\Downloads\Escalamento.csv"
