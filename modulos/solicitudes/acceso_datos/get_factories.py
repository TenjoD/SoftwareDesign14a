from modulos.solicitudes.configuracion.config import cargar_configuracion
from modulos.solicitudes.acceso_datos.mysql_factory import MySQLSolicitudDAOFactory
from modulos.solicitudes.acceso_datos.postgres_factory import PostgresSolicitudDAOFactory

def obtener_fabrica():
    config = cargar_configuracion()
    if config["db_engine"] == "postgres":
        return PostgresSolicitudDAOFactory()
    return MySQLSolicitudDAOFactory()