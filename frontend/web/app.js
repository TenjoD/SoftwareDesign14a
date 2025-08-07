async function listarSolicitudes() {
    const res = await fetch("http://localhost:8000/comentarios/");
    const data = await res.json();
    const lista = document.getElementById("listaSolicitudes");
    lista.innerHTML = "";
    data.forEach(s => {
        const item = document.createElement("li");
        item.textContent = `ID: ${s.id} | Empleado: ${s.emp_id} | Jefe: ${s.jefe_id} | Motivo: ${s.sol_motivo} | ${s.sol_fecha_inicio} a ${s.sol_fecha_fin}`;
        lista.appendChild(item);
    });
}


document.getElementById("formSolicitud").addEventListener("submit", async function(e) {
    e.preventDefault();
    const body = {
        emp_id: parseInt(document.getElementById("emp_id").value),
        jefe_id: parseInt(document.getElementById("jefe_id").value),
        sol_fecha_inicio: document.getElementById("sol_fecha_inicio").value,
        sol_fecha_fin: document.getElementById("sol_fecha_fin").value,
        sol_motivo: document.getElementById("sol_motivo").value
    };
    await fetch(API_BASE + ENDPOINTS.create, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(body)
    });
    alert("Solicitud creada correctamente.");
    listarSolicitudes();
    mostrarSeccion('listarSolicitudes');
});

async function buscarSolicitud() {
    const id = document.getElementById("sol_id_buscar").value;
    const res = await fetch(API_BASE + ENDPOINTS.read_one.replace("{id}", id));
    if (res.ok) {
        const data = await res.json();
        document.getElementById("emp_idAccion").value = data.emp_id;
        document.getElementById("jefe_idAccion").value = data.jefe_id;
        document.getElementById("sol_fecha_inicioAccion").value = data.sol_fecha_inicio;
        document.getElementById("sol_fecha_finAccion").value = data.sol_fecha_fin;
        document.getElementById("sol_motivoAccion").value = data.sol_motivo;
        mostrarSeccion('accionesSolicitud');
        alert("Solicitud cargada para edición.");
    } else {
        alert("Solicitud no encontrada.");
    }
}

async function actualizarSolicitud() {
    const id = document.getElementById("sol_id_buscar").value;
    const body = {
        emp_id: parseInt(document.getElementById("emp_idAccion").value),
        jefe_id: parseInt(document.getElementById("jefe_idAccion").value),
        sol_fecha_inicio: document.getElementById("sol_fecha_inicioAccion").value,
        sol_fecha_fin: document.getElementById("sol_fecha_finAccion").value,
        sol_motivo: document.getElementById("sol_motivoAccion").value
    };
    const res = await fetch(API_BASE + ENDPOINTS.update.replace("{id}", id), {
        method: "PUT",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(body)
    });
    const result = await res.json();
    alert(result.mensaje || "Solicitud actualizada.");
    listarSolicitudes();
    mostrarSeccion('listarSolicitudes');
}

async function eliminarSolicitud() {
    const id = document.getElementById("sol_id_buscar").value;
    const res = await fetch(API_BASE + ENDPOINTS.delete.replace("{id}", id), { method: "DELETE" });
    const result = await res.json();
    alert(result.mensaje || "Solicitud eliminada.");
    listarSolicitudes();
    mostrarSeccion('listarSolicitudes');
}

function mostrarSeccion(id) {
    document.querySelectorAll(".seccion").forEach(s => s.style.display = "none");
    document.getElementById(id).style.display = "block";
}


listarProductos();
mostrarSeccion('crear');
