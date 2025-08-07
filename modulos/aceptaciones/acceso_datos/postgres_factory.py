from modulos.aceptaciones.acceso_datos.aceptacion_dao import AceptacionDAOMySQL
from modulos.aceptaciones.acceso_datos.dao_factory import AceptacionDAOFactory

class PostgresAceptacionDAOFactory(AceptacionDAOFactory):
    def crear_dao(self):
        return AceptacionDAOMySQL()