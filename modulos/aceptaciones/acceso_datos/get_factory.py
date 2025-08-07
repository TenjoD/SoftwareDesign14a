from modulos.aceptaciones.configuracion.config import cargar_configuracion
from modulos.aceptaciones.acceso_datos.mysql_factory import MySQLAceptacionDAOFactory
from modulos.aceptaciones.acceso_datos.postgres_factory import PostgresAceptacionDAOFactory

def obtener_fabrica():
    config = cargar_configuracion()
    if config["db_engine"] == "postgres":
        return PostgresAceptacionDAOFactory()
    return MySQLAceptacionDAOFactory()