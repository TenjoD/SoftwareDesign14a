import requests
import json

# Cargar configuración desde config.json
with open("modulos/aceptaciones/configuracion/config.json") as f:
    config = json.load(f)

API = config["api_base"]
ENDPOINTS = config["endpoints"]

def menu():
    print("\n===== Menú de Aceptación de Solicitudes =====")
    print("1. Ver solicitudes PENDIENTES del jefe")
    print("2. Ver TODAS las solicitudes asignadas al jefe")
    print("3. Actualizar estado y observaciones")
    print("4. Solicitar cambio de fecha")
    print("5. Salir")

def ver_todas_solicitudes_jefe():
    jefe_id = input("Ingrese su ID de jefe: ")
    url = ENDPOINTS["listar_por_jefe"].replace("{jefe_id}", jefe_id)
    r = requests.get(f"{API}{url}")
    try:
        solicitudes = r.json()
        if not solicitudes:
            print("No hay solicitudes.")
        for s in solicitudes:
            print(f"[{s['estado'].upper()}] ID validación: {s['val_jefe_id']} | Solicitud: {s['sol_id']} | | Observaciones: {s['observaciones']} |"
                  f"Empleado: {s['emp_nombre']} ({s['emp_documento']}) | Fechas: {s['sol_fecha_inicio']} a {s['sol_fecha_fin']}")
    except Exception:
        print(r.status_code, r.text)
        

def ver_solicitudes_pendientes_jefe():
    jefe_id = input("Ingrese su ID de jefe: ")
    url = ENDPOINTS["listar_pendientes"].replace("{jefe_id}", jefe_id)
    r = requests.get(f"{API}{url}")
    try:
        solicitudes = r.json()
        if not solicitudes:
            print("No hay solicitudes pendientes.")
        for s in solicitudes:
            print(f"[PENDIENTE] ID validación: {s['val_jefe_id']} | Solicitud: {s['sol_id']} | Observaciones: {s['observaciones']} | "
                  f"Empleado: {s['emp_nombre']} ({s['emp_documento']}) | Fechas: {s['sol_fecha_inicio']} a {s['sol_fecha_fin']}")
    except Exception:
        print("Error al obtener pendientes:", r.status_code, r.text)

def actualizar_estado():
    val_id = input("ID de la validación a actualizar: ")
    estado = input("Nuevo estado (ACEPTADO, RECHAZADO, PENDIENTE): ").lower()
    obs = input("Observaciones: ")

    payload = {
        "estado": estado,
        "observaciones": obs
    }

    url = ENDPOINTS["actualizar_estado"].replace("{val_jefe_id}", val_id)
    r = requests.put(f"{API}{url}", json=payload)

    try:
        print(r.json())
    except Exception:
        print("Error al actualizar:", r.status_code, r.text)

def solicitar_cambio_fecha():
    val_id = input("ID de la validación para solicitar cambio de fecha: ")
    url = ENDPOINTS["cambio_fecha"].replace("{val_jefe_id}", val_id)
    r = requests.put(f"{API}{url}")

    try:
        print(r.json())
    except Exception:
        print("Error al solicitar cambio:", r.status_code, r.text)

if __name__ == "__main__":
    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            ver_todas_solicitudes_jefe()
        elif opcion == "2":
            ver_solicitudes_pendientes_jefe()
        elif opcion == "3":
            actualizar_estado()
        elif opcion == "4":
            solicitar_cambio_fecha()
        elif opcion == "5":
            break
        else:
            print("Opción inválida.")
