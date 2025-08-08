import tkinter as tk
from tkinter import messagebox, simpledialog
import requests
import json

# Cargar configuración desde config.json
with open("modulos/aceptaciones/configuracion/config.json") as f:
    config = json.load(f)

API = config["api_base"]
ENDPOINTS = config["endpoints"]

ventana = tk.Tk()
ventana.title("Gestión de Aceptación de Solicitudes")

# Campos comunes
tk.Label(ventana, text="ID Jefe:").grid(row=0, column=0, sticky="w")
entry_jefe_id = tk.Entry(ventana)
entry_jefe_id.grid(row=0, column=1)

# ---- Funciones ----

def ver_todas_solicitudes_jefe():
    jefe_id = entry_jefe_id.get().strip()
    if not jefe_id:
        messagebox.showerror("Error", "Debes ingresar el ID del jefe.")
        return
    url = ENDPOINTS["listar_por_jefe"].replace("{jefe_id}", jefe_id)
    try:
        r = requests.get(f"{API}{url}")
        solicitudes = r.json()
        if not solicitudes:
            messagebox.showinfo("Solicitudes", "No hay solicitudes.")
            return
        salida = "\n".join([
            f"[{s['estado'].upper()}] ID validación: {s['val_jefe_id']} | Solicitud: {s['sol_id']} | "
            f"Observaciones: {s.get('observaciones', '')} | "
            f"Empleado: {s['emp_nombre']} ({s['emp_documento']}) | "
            f"Fechas: {s['sol_fecha_inicio']} a {s['sol_fecha_fin']}"
            for s in solicitudes
        ])
        messagebox.showinfo("Todas las solicitudes", salida)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def ver_solicitudes_pendientes_jefe():
    jefe_id = entry_jefe_id.get().strip()
    if not jefe_id:
        messagebox.showerror("Error", "Debes ingresar el ID del jefe.")
        return
    url = ENDPOINTS["listar_pendientes"].replace("{jefe_id}", jefe_id)
    try:
        r = requests.get(f"{API}{url}")
        solicitudes = r.json()
        if not solicitudes:
            messagebox.showinfo("Solicitudes", "No hay solicitudes pendientes.")
            return
        salida = "\n".join([
            f"[PENDIENTE] ID validación: {s['val_jefe_id']} | Solicitud: {s['sol_id']} | "
            f"Observaciones: {s.get('observaciones', '')} | "
            f"Empleado: {s['emp_nombre']} ({s['emp_documento']}) | "
            f"Fechas: {s['sol_fecha_inicio']} a {s['sol_fecha_fin']}"
            for s in solicitudes
        ])
        messagebox.showinfo("Pendientes", salida)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def actualizar_estado():
    val_id = simpledialog.askstring("Actualizar estado", "ID de la validación a actualizar:")
    if not val_id:
        return
    estado = simpledialog.askstring("Estado", "Nuevo estado (ACEPTADO, RECHAZADO, PENDIENTE):")
    if not estado:
        return
    obs = simpledialog.askstring("Observaciones", "Ingrese observaciones:")
    payload = {
        "estado": estado.lower(),
        "observaciones": obs
    }
    url = ENDPOINTS["actualizar_estado"].replace("{val_jefe_id}", val_id)
    try:
        r = requests.put(f"{API}{url}", json=payload)
        if r.status_code == 200:
            messagebox.showinfo("Éxito", "Estado actualizado correctamente.")
        else:
            messagebox.showerror("Error", f"{r.status_code} - {r.text}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def solicitar_cambio_fecha():
    val_id = simpledialog.askstring("Cambio de fecha", "ID de la validación:")
    if not val_id:
        return
    url = ENDPOINTS["cambio_fecha"].replace("{val_jefe_id}", val_id)
    try:
        r = requests.put(f"{API}{url}")
        if r.status_code == 200:
            messagebox.showinfo("Éxito", "Solicitud marcada como pendiente por cambio de fechas.")
        else:
            messagebox.showerror("Error", f"{r.status_code} - {r.text}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# ---- Botones ----
tk.Button(ventana, text="Ver todas las solicitudes", command=ver_solicitudes_pendientes_jefe).grid(row=1, column=0, pady=5)
tk.Button(ventana, text="Ver las solicitudes pendientes", command=ver_todas_solicitudes_jefe).grid(row=1, column=1, pady=5)
tk.Button(ventana, text="Actualizar estado", command=actualizar_estado).grid(row=2, column=0, pady=5)
tk.Button(ventana, text="Solicitar cambio de fecha", command=solicitar_cambio_fecha).grid(row=2, column=1, pady=5)

ventana.mainloop()
