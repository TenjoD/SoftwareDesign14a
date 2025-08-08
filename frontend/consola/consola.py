<<<<<<< HEAD
import json

# Cargar configuración desde config.json
with open("modulos/Reportes/configuracion/config.json") as f:
=======
import requests
import json

# Cargar configuración desde config.json
with open("modulos/solicitudes/configuracion/config.json") as f:
>>>>>>> c75b52b121baee9151621703c6952b7a17960336
    config = json.load(f)

API = config["api_base"]
ENDPOINTS = config["endpoints"]

def menu():
<<<<<<< HEAD
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
=======
    print("\n===== Menú de Solicitudes de Vacaciones =====")
    print("1. Crear nueva solicitud")
    print("2. Listar solicitudes")
    print("3. Obtener solicitud por ID")
    print("4. Actualizar solicitud")
    print("5. Eliminar solicitud")
    print("6. Salir")

def crear_solicitud():
    try:
        sol_id = int(input("ID de la solicitud:"))
        emp_id = int(input("ID del empleado: "))
        jefe_id = int(input("ID del jefe: "))
        fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ")
        fecha_fin = input("Fecha de fin (YYYY-MM-DD): ")
        motivo = input("Motivo de la solicitud: ")

        payload = {
            "sol_id": sol_id,
            "emp_id": emp_id,
            "jefe_id": jefe_id,
            "sol_fecha_inicio": fecha_inicio,
            "sol_fecha_fin": fecha_fin,
            "sol_motivo": motivo
        }

        r = requests.post(f"{API}{ENDPOINTS['create_solicitud']}", json=payload)

        try:
            print(r.json())
        except Exception:
            print("Error al interpretar la respuesta. Código:", r.status_code)
            print("Respuesta:", r.text)
    except ValueError:
        print("⚠️ Error: Los IDs deben ser números.")

def listar_solicitudes():
    r = requests.get(f"{API}{ENDPOINTS['read_all_solicitud']}")
    try:
        solicitudes = r.json()
        if not solicitudes:
            print("No hay solicitudes registradas.")
        for s in solicitudes:
            print(f"ID: {s['sol_id']} | Empleado: {s['emp_id']} | Jefe: {s['jefe_id']} | "
                  f"Inicio: {s['sol_fecha_inicio']} | Fin: {s['sol_fecha_fin']} | Motivo: {s['sol_motivo']}")
    except Exception:
        print("Error al obtener solicitudes:", r.status_code, r.text)

def obtener_solicitud():
    id = input("ID de la solicitud: ")
    url = ENDPOINTS["read_one_solicitud"].replace("{id}", id)
    r = requests.get(f"{API}{url}")
    try:
        print(r.json())
    except Exception:
        print("Solicitud no encontrada o error:", r.status_code, r.text)

def actualizar_solicitud():
    try:
        sol_id = input("ID de la solicitud a actualizar: ")
        emp_id = int(input("Nuevo ID del empleado: "))
        jefe_id = int(input("Nuevo ID del jefe: "))
        fecha_inicio = input("Nueva fecha de inicio (YYYY-MM-DD): ")
        fecha_fin = input("Nueva fecha de fin (YYYY-MM-DD): ")
        motivo = input("Nuevo motivo: ")

        payload = {
            "sol_id": sol_id,
            "emp_id": emp_id,
            "jefe_id": jefe_id,
            "sol_fecha_inicio": fecha_inicio,
            "sol_fecha_fin": fecha_fin,
            "sol_motivo": motivo
        }

        url = ENDPOINTS["update_solicitud"].replace("{id}", id)
        r = requests.put(f"{API}{url}", json=payload)

        try:
            print(r.json())
        except Exception:
            print("Error al actualizar:", r.status_code, r.text)
    except ValueError:
        print("⚠️ Error: Los IDs deben ser números.")

def eliminar_solicitud():
    id = input("ID de la solicitud a eliminar: ")
    url = ENDPOINTS["delete_solicitud"].replace("{id}", id)
    r = requests.delete(f"{API}{url}")
    try:
        print(r.json())
    except Exception:
        print("Error al eliminar:", r.status_code, r.text)
>>>>>>> c75b52b121baee9151621703c6952b7a17960336

if __name__ == "__main__":
    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
<<<<<<< HEAD
            crear_reporte()
        elif opcion == "2":
            listar_reportes()
        elif opcion == "3":
            obtener_reporte()
        elif opcion == "4":
            actualizar_reporte()
        elif opcion == "5":
            eliminar_reporte()
=======
            crear_solicitud()
        elif opcion == "2":
            listar_solicitudes()
        elif opcion == "3":
            obtener_solicitud()
        elif opcion == "4":
            actualizar_solicitud()
        elif opcion == "5":
            eliminar_solicitud()
>>>>>>> c75b52b121baee9151621703c6952b7a17960336
        elif opcion == "6":
            break
        else:
            print("Opción inválida.")
<<<<<<< HEAD


=======
>>>>>>> c75b52b121baee9151621703c6952b7a17960336
