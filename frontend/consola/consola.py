import json

# Cargar configuración desde config.json
with open("modulos/Reportes/configuracion/config.json") as f:
    config = json.load(f)

API = config["api_base"]
ENDPOINTS = config["endpoints"]

def menu():
    print("\n===== Menú de Reportes =====")
    print("1. Crear nuevo reporte")
    print("2. Listar reportes")
    print("3. Obtener reporte por ID")
    print("4. Actualizar reporte")
    print("5. Eliminar reporte")
    print("6. Salir")

def crear_reporte():
    empleado_id = input("ID del empleado: ")
    fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ")
    fecha_fin = input("Fecha de fin (YYYY-MM-DD): ")
    motivo = input("Motivo del reporte: ")
    estado = input("Estado inicial (pendiente/aprobada/rechazada): ")

    r = requests.post(f"{API}{ENDPOINTS['create']}", json={
        "empleado_id": int(empleado_id),
        "fecha_inicio": fecha_inicio,
        "fecha_fin": fecha_fin,
        "motivo": motivo,
        "estado": estado
    })
    print(r.json())

def listar_reportes():
    r = requests.get(f"{API}{ENDPOINTS['read_all']}")
    for s in r.json():
        print(s)

def obtener_reporte():
    id = input("ID del reporteQ: ")
    url = ENDPOINTS["read_one"].replace("{id}", id)
    r = requests.get(f"{API}{url}")
    print(r.json() if r.status_code == 200 else "Reporte no encontrado.")

def actualizar_reporte():
    id = input("ID del reporte a actualizar: ")
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

def eliminar_reporte():
    id = input("ID del reporte a eliminar: ")
    url = ENDPOINTS["delete"].replace("{id}", id)
    r = requests.delete(f"{API}{url}")
    print(r.json())

if __name__ == "__main__":
    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            crear_reporte()
        elif opcion == "2":
            listar_reportes()
        elif opcion == "3":
            obtener_reporte()
        elif opcion == "4":
            actualizar_reporte()
        elif opcion == "5":
            eliminar_reporte()
        elif opcion == "6":
            break
        else:
            print("Opción inválida.")


