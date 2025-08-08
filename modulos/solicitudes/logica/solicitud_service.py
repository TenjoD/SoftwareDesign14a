import json
from fastapi import APIRouter, Request, HTTPException
from modulos.solicitudes.acceso_datos.get_factory import obtener_fabrica
from modulos.solicitudes.acceso_datos.solicitud_dto import SolicitudDTO
<<<<<<< HEAD
=======
from datetime import datetime
>>>>>>> c75b52b121baee9151621703c6952b7a17960336

dao = obtener_fabrica().crear_dao()
router = APIRouter()

@router.post("/")
async def crear_solicitud(req: Request):
    data = await req.json()
<<<<<<< HEAD
    solicitud = SolicitudDTO(
        nombre=data["nombre"],
        descripcion=data["descripcion"],
        precio=float(data["precio"]),
        categoria=data["categoria"]
    )
    dao.guardar(solicitud)
    return {"mensaje": "Solicitud almacenado correctamente."}
@router.get("/")
def obtener_solicitudes():
    return [p.__dict__ for p in dao.obtener_todos()]
=======
    print("Datos recibidos:", data)  
    solicitud = SolicitudDTO(
        emp_id=data["emp_id"],
        jefe_id=data["jefe_id"],
        sol_fecha_inicio=data["sol_fecha_inicio"],
        sol_fecha_fin=data["sol_fecha_fin"],
        sol_motivo=data["sol_motivo"],
        sol_fecha_creacion=datetime.now()
    )
    dao.guardar(solicitud)
    return {"mensaje": "Solicitud almacenada correctamente."}

@router.get("/")
def obtener_solicitudes():
    return [s.__dict__ for s in dao.obtener_todos()]

>>>>>>> c75b52b121baee9151621703c6952b7a17960336
@router.get("/{id}")
def obtener_solicitud(id: int):
    solicitud = dao.obtener_por_id(id)
    if not solicitud:
<<<<<<< HEAD
        raise HTTPException(status_code=404, detail="Solicitud no encontrado")
    return solicitud.__dict__
=======
        raise HTTPException(status_code=404, detail="Solicitud no encontrada")
    return solicitud.__dict__

>>>>>>> c75b52b121baee9151621703c6952b7a17960336
@router.put("/{id}")
async def actualizar_solicitud(id: int, req: Request):
    data = await req.json()
    actualizado = SolicitudDTO(
<<<<<<< HEAD
        id=id,
        nombre=data["nombre"],
        descripcion=data["descripcion"],
        precio=float(data["precio"]),
        categoria=data["categoria"]
    )
    dao.actualizar(actualizado)
    return {"mensaje": "Solicitud actualizado"}
@router.delete("/{id}")
def eliminar_solicitud(id: int):
    dao.eliminar(id)
    return {"mensaje": "Solicitud eliminado"}
=======
        sol_id=id,
        emp_id=data["emp_id"],
        jefe_id=data["jefe_id"],
        sol_fecha_inicio=data["sol_fecha_inicio"],
        sol_fecha_fin=data["sol_fecha_fin"],
        sol_motivo=data["sol_motivo"],
        sol_fecha_creacion=datetime.now()
    )
    dao.actualizar(actualizado)
    return {"mensaje": "Solicitud actualizada correctamente."}

@router.delete("/{id}")
def eliminar_solicitud(id: int):
    dao.eliminar(id)
    return {"mensaje": "Solicitud eliminada correctamente."}
>>>>>>> c75b52b121baee9151621703c6952b7a17960336
