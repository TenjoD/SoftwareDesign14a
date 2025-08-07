async function listarReportes() {
    const res = await fetch("http://localhost:8000/reportes/");
    const data = await res.json();
    const lista = document.getElementById("listaReportes");
    lista.innerHTML = "";
    data.forEach(r => {
        const item = document.createElement("li");
        item.textContent = `ID: ${r.rep_id} | Empleado: ${r.emp_id} | Estado Solicitud: ${r.rep_estado_solicitud_id} | Estado Jefe: ${r.rep_estado_jefe_id} | Estado RRHH: ${r.rep_estado_rrhh_id} | Desde: ${r.rep_fecha_inicio} a ${r.rep_fecha_fin} | Creación: ${r.rep_fecha_creacion}`;
        lista.appendChild(item);
    });
}

document.getElementById("formReporte").addEventListener("submit", async function(e) {
    e.preventDefault();
    const body = {
        emp_id: parseInt(document.getElementById("emp_id").value),
        rep_estado_solicitud_id: parseInt(document.getElementById("rep_estado_solicitud_id").value),
        rep_estado_jefe_id: parseInt(document.getElementById("rep_estado_jefe_id").value),
        rep_estado_rrhh_id: parseInt(document.getElementById("rep_estado_rrhh_id").value),
        rep_fecha_inicio: document.getElementById("rep_fecha_inicio").value,
        rep_fecha_fin: document.getElementById("rep_fecha_fin").value,
        rep_fecha_creacion: document.getElementById("rep_fecha_creacion").value
    };
    const res = await fetch(API_BASE + ENDPOINTS.create, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(body)
    });
    const result = await res.json();
    if (res.ok) {
        alert(result.mensaje || "Reporte creado correctamente.");
    } else {
        alert(result.detail || "Error al crear el reporte.");
    }
    listarReportes();
    mostrarSeccion('listarReportes');
});

async function buscarReporte() {
    const id = document.getElementById("rep_id_buscar").value;
    const res = await fetch(API_BASE + ENDPOINTS.read_one.replace("{id}", id));
    if (res.ok) {
        const data = await res.json();
        document.getElementById("emp_idAccion").value = data.emp_id;
        document.getElementById("rep_estado_solicitud_idAccion").value = data.rep_estado_solicitud_id;
        document.getElementById("rep_estado_jefe_idAccion").value = data.rep_estado_jefe_id;
        document.getElementById("rep_estado_rrhh_idAccion").value = data.rep_estado_rrhh_id;
        document.getElementById("rep_fecha_inicioAccion").value = data.rep_fecha_inicio;
        document.getElementById("rep_fecha_finAccion").value = data.rep_fecha_fin;
        document.getElementById("rep_fecha_creacionAccion").value = data.rep_fecha_creacion;
        mostrarSeccion('accionesReportes');
        alert("Reporte cargado para edición.");
    } else {
        alert("Reporte no encontrado.");
    }
}

async function actualizarReporte() {
    const id = document.getElementById("rep_id_buscar").value;
    const body = {
        emp_id: parseInt(document.getElementById("emp_idAccion").value),
        rep_estado_solicitud_id: parseInt(document.getElementById("rep_estado_solicitud_idAccion").value),
        rep_estado_jefe_id: parseInt(document.getElementById("rep_estado_jefe_idAccion").value),
        rep_estado_rrhh_id: parseInt(document.getElementById("rep_estado_rrhh_idAccion").value),
        rep_fecha_inicio: document.getElementById("rep_fecha_inicioAccion").value,
        rep_fecha_fin: document.getElementById("rep_fecha_finAccion").value,
        rep_fecha_creacion: document.getElementById("rep_fecha_creacionAccion").value
    };
    const res = await fetch(API_BASE + ENDPOINTS.update.replace("{id}", id), {
        method: "PUT",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(body)
    });
    const result = await res.json();
    alert(result.mensaje || "Reporte actualizado.");
    listarReportes();
    mostrarSeccion('listarReportes');
}

async function eliminarReporte() {
    const id = document.getElementById("rep_id_buscar").value;
    const res = await fetch(API_BASE + ENDPOINTS.delete.replace("{id}", id), { method: "DELETE" });
    const result = await res.json();
    alert(result.mensaje || "Reporte eliminado.");
    listarReportes();
    mostrarSeccion('listarReportes');
}

function mostrarSeccion(id) {
    document.querySelectorAll(".seccion").forEach(s => s.style.display = "none");
    document.getElementById(id).style.display = "block";
}


listarReportes();
mostrarSeccion('crear');
