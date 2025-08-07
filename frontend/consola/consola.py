import requests
import json

# Cargar configuración desde config.json
with open("modulos/solicitudes/configuracion/config.json") as f:
    config = json.load(f)

API = config["api_base"]
ENDPOINTS = config["endpoints"]

def menu():
    print("\n===== Menú de Solicitudes de Vacaciones =====")
    print("1. Crear nueva solicitud")
    print("2. Listar solicitudes")
    print("3. Obtener solicitud por ID")
    print("4. Actualizar solicitud")
    print("5. Eliminar solicitud")
    print("6. Salir")

def crear_solicitud():
    empleado_id = input("ID del empleado: ")
    fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ")
    fecha_fin = input("Fecha de fin (YYYY-MM-DD): ")
    motivo = input("Motivo de la solicitud: ")
    estado = input("Estado inicial (pendiente/aprobada/rechazada): ")
    
    r = requests.post(f"{API}{ENDPOINTS['create']}", json={
        "empleado_id": int(empleado_id),
        "fecha_inicio": fecha_inicio,
        "fecha_fin": fecha_fin,
        "motivo": motivo,
        "estado": estado
    })
    print(r.json())

def listar_solicitudes():
    r = requests.get(f"{API}{ENDPOINTS['read_all']}")
    for s in r.json():
        print(s)

def obtener_solicitud():
    id = input("ID de la solicitud: ")
    url = ENDPOINTS["read_one"].replace("{id}", id)
    r = requests.get(f"{API}{url}")
    print(r.json() if r.status_code == 200 else "Solicitud no encontrada.")

def actualizar_solicitud():
    id = input("ID de la solicitud a actualizar: ")
    empleado_id = input("Nuevo ID del empleado: ")
    fecha_inicio = input("Nueva fecha de inicio (YYYY-MM-DD): ")
    fecha_fin = input("Nueva fecha de fin (YYYY-MM-DD): ")
    motivo = input("Nuevo motivo: ")
    estado = input("Nuevo estado (pendiente/aprobada/rechazada): ")
    
    url = ENDPOINTS["update"].replace("{id}", id)
    r = requests.put(f"{API}{url}", json={
        "empleado_id": int(empleado_id),
        "fecha_inicio": fecha_inicio,
        "fecha_fin": fecha_fin,
        "motivo": motivo,
        "estado": estado
    })
    print(r.json())

def eliminar_solicitud():
    id = input("ID de la solicitud a eliminar: ")
    url = ENDPOINTS["delete"].replace("{id}", id)
    r = requests.delete(f"{API}{url}")
    print(r.json())

if __name__ == "__main__":
    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            crear_solicitud()
        elif opcion == "2":
            listar_solicitudes()
        elif opcion == "3":
            obtener_solicitud()
        elif opcion == "4":
            actualizar_solicitud()
        elif opcion == "5":
            eliminar_solicitud()
        elif opcion == "6":
            break
        else:
            print("Opción inválida.")


