import tkinter as tk
<<<<<<< HEAD
from tkinter import ttk, messagebox
import requests
import json

# Cargar configuración desde config.json
with open("modulos/solicitudes/configuracion/config.json") as f:
    config = json.load(f)

API = config["api_base"]
ENDPOINTS = config["endpoints"]

def recargar_datos():
    for item in tree.get_children():
        tree.delete(item)
    try:
        r = requests.get(API + ENDPOINTS["read_all"])
        if r.status_code == 200:
            for s in r.json():
                tree.insert("", "end", values=(
                    s["id"], s["usuario_email"], s["descripcion"], s["estado"], s.get("fecha_creacion", "")
                ))
    except Exception as e:
        messagebox.showerror("Error", str(e))

def crear_solicitud():
    dialogo_solicitud("Crear nueva solicitud")

def editar_solicitud():
    seleccionado = tree.focus()
    if not seleccionado:
        messagebox.showwarning("Seleccionar", "Seleccione una solicitud.")
        return
    valores = tree.item(seleccionado, "values")
    dialogo_solicitud("Editar solicitud", valores)

def eliminar_solicitud():
    seleccionado = tree.focus()
    if not seleccionado:
        messagebox.showwarning("Seleccionar", "Seleccione una solicitud.")
        return
    id_sol = tree.item(seleccionado, "values")[0]
    if messagebox.askyesno("Eliminar", "¿Seguro que desea eliminar esta solicitud?"):
        try:
            r = requests.delete(API + ENDPOINTS["delete"].replace("{id}", str(id_sol)))
            if r.status_code == 200:
                recargar_datos()
                messagebox.showinfo("Éxito", "Solicitud eliminada.")
            else:
                messagebox.showerror("Error", r.text)
        except Exception as e:
            messagebox.showerror("Error", str(e))

def dialogo_solicitud(titulo, datos=None):
    ventana = tk.Toplevel(root)
    ventana.title(titulo)

    tk.Label(ventana, text="Email:").grid(row=0, column=0)
    email = tk.Entry(ventana)
    email.grid(row=0, column=1)

    tk.Label(ventana, text="Descripción:").grid(row=1, column=0)
    descripcion = tk.Entry(ventana)
    descripcion.grid(row=1, column=1)

    tk.Label(ventana, text="Estado:").grid(row=2, column=0)
    estado = tk.Entry(ventana)
    estado.grid(row=2, column=1)

    if datos:
        id_sol, email_val, desc_val, estado_val, _ = datos
        email.insert(0, email_val)
        descripcion.insert(0, desc_val)
        estado.insert(0, estado_val)

    def guardar():
        payload = {
            "usuario_email": email.get(),
            "descripcion": descripcion.get(),
            "estado": estado.get()
        }
        try:
            if datos:
                r = requests.put(API + ENDPOINTS["update"].replace("{id}", str(id_sol)), json=payload)
            else:
                r = requests.post(API + ENDPOINTS["create"], json=payload)
            if r.status_code in [200, 201]:
                recargar_datos()
                ventana.destroy()
                messagebox.showinfo("Éxito", "Operación exitosa.")
            else:
                messagebox.showerror("Error", r.text)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(ventana, text="Guardar", command=guardar).grid(row=3, columnspan=2)

# Ventana principal
root = tk.Tk()
root.title("Gestión de Solicitudes")

# Tabla
cols = ("ID", "Email", "Descripción", "Estado", "Fecha de Creación")
tree = ttk.Treeview(root, columns=cols, show="headings")
for col in cols:
    tree.heading(col, text=col)
    tree.column(col, anchor="center", width=150)
tree.pack(fill="both", expand=True, padx=10, pady=10)

# Botones CRUD
botonera = tk.Frame(root)
botonera.pack(pady=10)

tk.Button(botonera, text="Nueva", command=crear_solicitud).pack(side="left", padx=5)
tk.Button(botonera, text="Editar", command=editar_solicitud).pack(side="left", padx=5)
tk.Button(botonera, text="Eliminar", command=eliminar_solicitud).pack(side="left", padx=5)
tk.Button(botonera, text="Recargar", command=recargar_datos).pack(side="left", padx=5)

recargar_datos()
root.mainloop()
=======
from tkinter import messagebox
import requests
import json

# Cargar configuración desde el archivo config.json
with open("modulos/solicitudes/configuracion/config.json") as f:
    config = json.load(f)

API_BASE = config["api_base"]
ENDPOINTS = config["endpoints"]

# Interfaz de usuario
ventana = tk.Tk()
ventana.title("Gestión de Solicitudes de Vacaciones")

tk.Label(ventana, text="ID Empleado:").grid(row=0, column=0)
emp_id = tk.Entry(ventana)
emp_id.grid(row=0, column=1)

tk.Label(ventana, text="ID Jefe:").grid(row=1, column=0)
jefe_id = tk.Entry(ventana)
jefe_id.grid(row=1, column=1)

tk.Label(ventana, text="Fecha Inicio (YYYY-MM-DD):").grid(row=2, column=0)
fecha_inicio = tk.Entry(ventana)
fecha_inicio.grid(row=2, column=1)

tk.Label(ventana, text="Fecha Fin (YYYY-MM-DD):").grid(row=3, column=0)
fecha_fin = tk.Entry(ventana)
fecha_fin.grid(row=3, column=1)

tk.Label(ventana, text="Motivo:").grid(row=4, column=0)
motivo = tk.Entry(ventana)
motivo.grid(row=4, column=1)

tk.Label(ventana, text="ID Solicitud (para actualizar/eliminar):").grid(row=5, column=0)
sol_id = tk.Entry(ventana)
sol_id.grid(row=5, column=1)

def guardar():
    payload = {
        "emp_id": int(emp_id.get()),
        "jefe_id": int(jefe_id.get()),
        "sol_fecha_inicio": fecha_inicio.get(),
        "sol_fecha_fin": fecha_fin.get(),
        "sol_motivo": motivo.get()
    }
    try:
        r = requests.post(API_BASE + ENDPOINTS["create_solicitud"], json=payload)
        if r.status_code in [200, 201]:
            messagebox.showinfo("Éxito", "Solicitud guardada correctamente.")
        else:
            messagebox.showerror("Error", f"Error al guardar solicitud: {r.status_code}\n{r.text}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def actualizar():
    id_val = sol_id.get()
    if not id_val:
        messagebox.showerror("Error", "Debes ingresar el ID de la solicitud.")
        return
    payload = {
        "emp_id": int(emp_id.get()),
        "jefe_id": int(jefe_id.get()),
        "sol_fecha_inicio": fecha_inicio.get(),
        "sol_fecha_fin": fecha_fin.get(),
        "sol_motivo": motivo.get()
    }
    url = API_BASE + ENDPOINTS["update_solicitud"].replace("{id}", id_val)
    try:
        r = requests.put(url, json=payload)
        if r.status_code == 200:
            messagebox.showinfo("Éxito", "Solicitud actualizada.")
        else:
            messagebox.showerror("Error", f"No se pudo actualizar: {r.status_code}\n{r.text}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def eliminar():
    id_val = sol_id.get()
    if not id_val:
        messagebox.showerror("Error", "Debes ingresar el ID de la solicitud.")
        return
    url = API_BASE + ENDPOINTS["delete_solicitud"].replace("{id}", id_val)
    try:
        r = requests.delete(url)
        if r.status_code == 200:
            messagebox.showinfo("Éxito", "Solicitud eliminada.")
        else:
            messagebox.showerror("Error", f"No se pudo eliminar: {r.status_code}\n{r.text}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def listar():
    try:
        r = requests.get(API_BASE + ENDPOINTS["read_all_solicitud"])
        if r.status_code == 200:
            datos = r.json()
            salida = "\n".join([
                f"{d['sol_id']} - {d['emp_id']} - {d['sol_fecha_inicio']} → {d['sol_fecha_fin']} ({d['sol_motivo']})"
                for d in datos
            ])
            messagebox.showinfo("Solicitudes", salida if salida else "Sin solicitudes.")
        else:
            messagebox.showerror("Error", f"No se pudo obtener la lista: {r.status_code}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Botones
tk.Button(ventana, text="Guardar", command=guardar).grid(row=6, column=0)
tk.Button(ventana, text="Actualizar", command=actualizar).grid(row=6, column=1)
tk.Button(ventana, text="Eliminar", command=eliminar).grid(row=7, column=0)
tk.Button(ventana, text="Listar", command=listar).grid(row=7, column=1)

ventana.mainloop()

>>>>>>> c75b52b121baee9151621703c6952b7a17960336
