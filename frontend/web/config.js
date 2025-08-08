const API_BASE = "http://localhost:8000";
const ENDPOINTS = {
<<<<<<< HEAD
    create: "/reportes",
    read_all: "/reportes",
    read_one: "/reportes/{id}",
    update: "/reportes/{id}",
    delete: "/reportes/{id}",
=======
    
>>>>>>> c75b52b121baee9151621703c6952b7a17960336

    create_solicitud: "/solicitudes",
    read_all_solicitudes: "/solicitudes",
    read_one_solicitud: "/solicitudes/{id}",
    update_solicitud: "/solicitudes/{id}",
    delete_solicitud: "/solicitudes/{id}"

};
<<<<<<< HEAD
=======

const ENDPOINTS_JEFE = {
    listar_pendientes: "/aceptaciones?jefe_id={jefe_id}",
    listar_por_jefe: "/aceptaciones/all?jefe_id={jefe_id}",
    actualizar_estado: "/aceptaciones/actualizar?val_jefe_id={val_jefe_id}",
    cambio_fecha: "/aceptaciones/cambio-fecha?val_jefe_id={val_jefe_id}"
};
>>>>>>> c75b52b121baee9151621703c6952b7a17960336
