from modulos.aceptaciones.acceso_datos.aceptacion_dao import AceptacionDAOMySQL
from modulos.aceptaciones.acceso_datos.dao_factory import AceptacionDAOFactory

class MySQLAceptacionDAOFactory(AceptacionDAOFactory):
    def crear_dao(self):
        return AceptacionDAOMySQL()