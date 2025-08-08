from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from modulos.solicitudes.logica.solicitud_service  import router as solicitudes_router
<<<<<<< HEAD
from modulos.reportes.logica.reporte_service  import router as reportes_router
=======
from modulos.aceptaciones.logica.aceptacion_service import router as aceptaciones_router

>>>>>>> c75b52b121baee9151621703c6952b7a17960336

app = FastAPI(title="API Gateway")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(solicitudes_router, prefix="/solicitudes")
<<<<<<< HEAD
app.include_router(reportes_router, prefix="/reportes")
=======
app.include_router(aceptaciones_router, prefix="/aceptaciones")



>>>>>>> c75b52b121baee9151621703c6952b7a17960336
