# configuracion/config.py

import json

def cargar_configuracion(path="modulos/solicitudes/configuracion/config.json"):
    with open(path) as f:
        return json.load(f)
