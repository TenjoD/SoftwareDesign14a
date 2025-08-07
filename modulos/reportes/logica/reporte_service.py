import json
from fastapi import APIRouter, Request, HTTPException
from modulos.reportes.acesso_datos.get_factory import obtener_fabrica
from modulos.reportes.acesso_datos.reporte_dto import ReporteDTO

dao = obtener_fabrica().crear_dao()
router = APIRouter()

@router.post("/")
async def crear_reporte(req: Request):
    data = await req.json()
    reporte = ReporteDTO(
        emp_id=data["emp_id"],
        rep_estado_solicitud_id=data["rep_estado_solicitud_id"],
        rep_estado_jefe_id=data["rep_estado_jefe_id"],
        rep_estado_rrhh_id=data["rep_estado_rrhh_id"],
        rep_fecha_inicio=data["rep_fecha_inicio"],
        rep_fecha_fin=data["rep_fecha_fin"],
        rep_fecha_creacion=data.get("rep_fecha_creacion", None)
    )
    dao.guardar(reporte)
    return {"mensaje": "Reporte almacenado correctamente."}
@router.get("/")
def obtener_reportes():
    return [p.__dict__ for p in dao.obtener_todos()]
@router.get("/{id}")
def obtener_reporte(id: int):
    reporte = dao.obtener_por_id(id)
    if not reporte:
        raise HTTPException(status_code=404, detail="Reporte no encontrado")
    return reporte.__dict__
@router.put("/{id}")
async def actualizar_reporte(id: int, req: Request):
    data = await req.json()
    actualizado = ReporteDTO(
        rep_id=id,
        emp_id=data["emp_id"],
        rep_estado_solicitud_id=data["rep_estado_solicitud_id"],    
        rep_estado_jefe_id=data["rep_estado_jefe_id"],
        rep_estado_rrhh_id=data["rep_estado_rrhh_id"],  
        rep_fecha_inicio=data["rep_fecha_inicio"],
        rep_fecha_fin=data["rep_fecha_fin"],
        rep_fecha_creacion=data.get("rep_fecha_creacion", None)
    )
    dao.actualizar(actualizado)
    return {"mensaje": "Reporte actualizado"}
@router.delete("/{id}")
def eliminar_reporte(id: int):
    dao.eliminar(id)
    return {"mensaje": "Reporte eliminado"}
