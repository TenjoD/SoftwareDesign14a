from fastapi import APIRouter, Request, HTTPException
from modulos.aceptaciones.acceso_datos.aceptacion_dao import AceptacionDAOMySQL
from modulos.aceptaciones.acceso_datos.aceptacion_dto import AceptacionDTO

router = APIRouter()
dao = AceptacionDAOMySQL()
@router.get("/")
def obtener_solicitudes_pendientes_del_jefe(jefe_id: int):
    return dao.listar_validaciones_pendientes_por_jefe(jefe_id)

@router.get("/all")
def obtener_solicitudes_del_jefe(jefe_id: int):
    return dao.listar_validaciones_por_jefe(jefe_id)

@router.put("/actualizar")
async def actualizar_validacion(val_jefe_id: int, req: Request):
    data = await req.json()
    estado = data.get("estado", "").strip().upper() 
    observaciones = data.get("observaciones", "").strip()
    
    if estado not in ["PENDIENTE", "ACEPTADO", "RECHAZADO"]:
        raise HTTPException(status_code=400, detail="Estado no válido. Usa: PENDIENTE, ACEPTADO, RECHAZADO.")
    
    dao.actualizar_estado_y_observaciones(val_jefe_id, estado, observaciones)
    return {"mensaje": "Estado actualizado correctamente."}


@router.put("/cambio-fecha")
def solicitar_cambio_fecha(val_jefe_id: int):
    dao.marcar_como_pendiente(val_jefe_id, "Cambio de fechas solicitado por el jefe.")
    return {"mensaje": "Solicitud marcada como pendiente por cambio de fechas."}
