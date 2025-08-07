from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from modulos.solicitudes.logica.solicitud_service  import router as solicitudes_router
from modulos.aceptaciones.logica.aceptacion_service import router as aceptaciones_router


app = FastAPI(title="API Gateway")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(solicitudes_router, prefix="/solicitudes")
app.include_router(aceptaciones_router, prefix="/aceptaciones")



