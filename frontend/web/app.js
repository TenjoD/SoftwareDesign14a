async function listarComentarios() {
    const res = await fetch("http://localhost:8000/comentarios/");
    const data = await res.json();
    const lista = document.getElementById("lista");
    lista.innerHTML = "";
    data.forEach(c => {
        const item = document.createElement("li");
        item.textContent = `ID: ${c.id} - ${c.usuario_email} - ${c.texto} (${c.calificacion} (${c.fecha_creacion}))`;
        lista.appendChild(item);
    });
}

document.getElementById("formComentario").addEventListener("submit", async function(e) {
    e.preventDefault();
    const body = {
        texto: document.getElementById("texto").value,
        usuario_email: document.getElementById("email").value,
        calificacion: parseInt(document.getElementById("calificacion").value)
    };
    await fetch(API_BASE + ENDPOINTS.create, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(body)
    });
    alert("Comentario creado.");
    listarComentarios();
    mostrarSeccion('lista');
});

async function buscarComentario() {
    const id = document.getElementById("idBuscar").value;
    const res = await fetch(API_BASE + ENDPOINTS.read_one.replace("{id}", id));
    if (res.ok) {
        const data = await res.json();
        document.getElementById("textoAccion").value = data.texto;
        document.getElementById("emailAccion").value = data.usuario_email;
        document.getElementById("calificacionAccion").value = data.calificacion;
        mostrarSeccion('acciones');
        alert("Comentario cargado para edición.");
    } else {
        alert("Comentario no encontrado.");
    }
}

async function actualizarComentario() {
    const id = document.getElementById("idBuscar").value;
    const body = {
        texto: document.getElementById("textoAccion").value,
        usuario_email: document.getElementById("emailAccion").value,
        calificacion: parseInt(document.getElementById("calificacionAccion").value)
    };
    const res = await fetch(API_BASE + ENDPOINTS.update.replace("{id}", id), {
        method: "PUT",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(body)
    });
    const result = await res.json();
    alert(result.mensaje || "Actualizado");
    listarComentarios();
    mostrarSeccion('lista');
}

async function eliminarComentario() {
    const id = document.getElementById("idBuscar").value;
    const res = await fetch(API_BASE + ENDPOINTS.delete.replace("{id}", id), { method: "DELETE" });
    const result = await res.json();
    alert(result.mensaje || "Eliminado");
    listarComentarios();
    mostrarSeccion('lista');
}

function mostrarSeccion(id) {
    document.querySelectorAll(".seccion").forEach(s => s.style.display = "none");
    document.getElementById(id).style.display = "block";
}






async function listarProductos() {
    const res = await fetch(API_BASE + ENDPOINTS.read_all);
    const data = await res.json();
    const lista = document.getElementById("listaProductos");
    lista.innerHTML = "";
    data.forEach(p => {
        const item = document.createElement("li");
        item.textContent = `ID: ${p.id} - ${p.nombre} - ${p.descripcion} (${p.precio} - ${p.categoria})`;
        lista.appendChild(item);
    });
}

document.getElementById("formProducto").addEventListener("submit", async function(e) {
    e.preventDefault();
    const body = {
        nombre: document.getElementById("nombreProducto").value,
        descripcion: document.getElementById("descripcionProducto").value,
        precio: parseFloat(document.getElementById("precioProducto").value),
        categoria: document.getElementById("categoriaProducto").value
    };
    await fetch(API_BASE + ENDPOINTS.create, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(body)
    });
    alert("Producto creado.");
    listarProductos();
    mostrarSeccion('lista');
});

async function buscarProducto() {
    const id = document.getElementById("idBuscar").value;
    const res = await fetch(API_BASE + ENDPOINTS.read_one.replace("{id}", id));
    if (res.ok) {
        const data = await res.json();
        document.getElementById("nombreProducto").value = data.nombre;
        document.getElementById("descripcionProducto").value = data.descripcion;
        document.getElementById("precioProducto").value = data.precio;
        document.getElementById("categoriaProducto").value = data.categoria;
        mostrarSeccion('acciones');
        alert("Producto cargado para edición.");
    } else {
        alert("Producto no encontrado.");
    }
}

async function actualizarProducto() {
    const id = document.getElementById("idBuscar").value;
    const body = {
        nombre: document.getElementById("nombreProducto").value,
        descripcion: document.getElementById("descripcionProducto").value,
        precio: parseFloat(document.getElementById("precioProducto").value),
        categoria: document.getElementById("categoriaProducto").value 
    };
    const res = await fetch(API_BASE + ENDPOINTS.update.replace("{id}", id), {
        method: "PUT",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(body)
    });
    const result = await res.json();
    alert(result.mensaje || "Actualizado");
    listarProductos();
    mostrarSeccion('lista');
}

async function eliminarProducto() {
    const id = document.getElementById("idBuscar").value;
    const res = await fetch(API_BASE + ENDPOINTS.delete.replace("{id}", id), { method: "DELETE" });
    const result = await res.json();
    alert(result.mensaje || "Eliminado");
    listarProductos ();
    mostrarSeccion('lista');
}

function mostrarSeccion(id) {
    document.querySelectorAll(".seccion").forEach(s => s.style.display = "none");
    document.getElementById(id).style.display = "block";
}


listarProductos();
mostrarSeccion('crear');
