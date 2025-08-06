import json
from fastapi import APIRouter, Request, HTTPException
from modulos.solicitudes.acceso_datos.get_factory import obtener_fabrica
from modulos.solicitudes.acceso_datos.solicitud_dto import SolicitudDTO

dao = obtener_fabrica().crear_dao()
router = APIRouter()

@router.post("/")
async def crear_solicitud(req: Request):
    data = await req.json()
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
@router.get("/{id}")
def obtener_solicitud(id: int):
    solicitud = dao.obtener_por_id(id)
    if not solicitud:
        raise HTTPException(status_code=404, detail="Solicitud no encontrado")
    return solicitud.__dict__
@router.put("/{id}")
async def actualizar_solicitud(id: int, req: Request):
    data = await req.json()
    actualizado = SolicitudDTO(
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
