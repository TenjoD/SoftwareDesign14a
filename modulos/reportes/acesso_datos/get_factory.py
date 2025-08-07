from modulos.reportes.configuracion.config import cargar_configuracion
from modulos.reportes.acesso_datos.mysql_factory import MySQLReporteDAOFactory
from modulos.reportes.acesso_datos.postgres_factory import PostgresReporteDAOFactory

def obtener_fabrica():
    config = cargar_configuracion()
    if config["db_engine"] == "postgres":
        return PostgresReporteDAOFactory()
    return MySQLReporteDAOFactory()