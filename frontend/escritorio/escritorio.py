import tkinter as tk
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
